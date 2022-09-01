import json
import logging
import os
import string
import sys
import random

import allure
import pytest
from _pytest.fixtures import SubRequest
from typing import Any, Callable, Optional

ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
ALLUREDIR_OPTION = '--alluredir'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
log_filename = "logs/pytest_logs.log"
os.makedirs(os.path.dirname(log_filename), exist_ok=True)
file_handler = logging.FileHandler(log_filename, mode="w", encoding=None, delay=False)

try:
    import importlib

    sys.path.append("../tests")
    imports = importlib.import_module("imports")
    target = imports.target
    lf_libs = imports.lf_libs
    lf_tests = imports.lf_tests
    scp_file = imports.scp_file
    perfecto_interop = imports.perfecto_interop
    android_tests = imports.android_tests
    ios_tests = imports.ios_tests
    configuration = importlib.import_module("configuration")
    CONFIGURATION = configuration.CONFIGURATION
except ImportError as e:
    print(e)
    sys.exit("Python Import Error: " + str(e))


def pytest_addoption(parser):
    """pytest addoption function: contains ini objects and options"""
    parser.addini("controller_url", type='string', help="controller_url_parameter_override", default="0")
    parser.addini(name="firmware", type='string', help="AP Firmware build URL", default="0")

    parser.addoption(
        "--testbed",
        # nargs="+",
        default="basic-01",
        help="AP Model which is needed to test"
    )
    parser.addoption(
        "--num_stations",
        default=1,
        help="Number of Stations"
    )
    parser.addoption(
        "--device",
        # nargs="+",
        default="lanforge",
        help="Test Traffic Generator which can be used,  lanforge | perfecto"
    )

    parser.addoption(
        "--skip-env",
        action="store_true",
        default=False,
        help="skip adding to env data"
    )

    parser.addoption(
        "--use-perfecto-android",
        action="store_true",
        default=False,
        help="Use Interop Android Test Package for tests"
    )

    parser.addoption(
        "--use-perfecto-ios",
        action="store_true",
        default=False,
        help="Use Interop IoS Test Package for tests"
    )


@pytest.fixture(scope="session")
def get_lab_info():
    yield configuration


@pytest.fixture(scope="session")
def selected_testbed(request):
    """yields the testbed option selection"""
    current_testbed = request.config.getoption("--testbed")
    yield current_testbed


@pytest.fixture(scope="session")
def num_stations(request):
    """yields the testbed option selection"""
    num_stations = request.config.getoption("--num_stations")
    yield num_stations


@pytest.fixture(scope="session")
def get_security_flags():
    """used to get the essential markers on security and band"""
    # Add more classifications as we go
    security = ["open", "wpa", "wep", "wpa2_personal", "wpa3_personal", "wpa3_personal_mixed",
                "wpa_wpa2_enterprise_mixed", "wpa2_eap", "wpa2_only_eap",
                "wpa_wpa2_personal_mixed", "wpa_enterprise", "wpa2_enterprise", "wpa3_enterprise_mixed",
                "wpa3_enterprise", "twog", "fiveg", "sixg", "fiveg_lower", "fiveg_upper", "radius"]
    yield security


@pytest.fixture(scope="session")
def get_markers(request, get_security_flags):
    """used to get the markers on the selected test case class, used in setup_profiles"""
    session = request.node
    markers = list()
    security = get_security_flags
    data = dict()
    for item in session.items:
        data[item] = []
        print(item.iter_markers())
        for j in item.iter_markers():
            for i in security:
                if j.name == i:
                    if j.name == "twog":
                        data[item].append("2G")
                        continue
                    if j.name == "fiveg":
                        data[item].append("5G")
                        continue
                    if j.name == "sixg":
                        data[item].append("6G")
                        continue
                    if j.name == "fiveg_lower":
                        data[item].append("5G-lower")
                        continue
                    if j.name == "fiveg_upper":
                        data[item].append("5G-upper")
                        continue
                    data[item].append(j.name)
            print(j.name)
            markers.append(j.name)
    print(data)
    yield data


@pytest.fixture(scope="session")
def get_target_object(request, get_testbed_details, add_allure_environment_property: Callable) -> None:
    """yields the testbed option selection"""
    t_object = None
    try:
        t_object = target(controller_data=get_testbed_details["controller"], target=get_testbed_details["target"],
                          device_under_tests_info=get_testbed_details["device_under_tests"])
        if not request.config.getoption("--skip-env"):
            if get_testbed_details["target"] == "tip_2x":
                t_object.setup_environment_properties(add_allure_environment_property=
                                                      add_allure_environment_property)

    except Exception as e:
        t_object = None
        logging.error(
            "Exception is setting up Target Library Object: " + str(e) + " Check the lab_info.json for the Data and ")
        pytest.exit("Exception is setting up Target Library Object: " + str(e))

    def teardown_target():
        if t_object is not None:
            t_object.teardown_objects()

    request.addfinalizer(teardown_target)
    yield t_object


@pytest.fixture(scope="session")
def get_testbed_details(selected_testbed, request):
    """yields the selected testbed information from lab info file (configuration.py)"""
    if request.config.getini("controller_url") != "0":
        CONFIGURATION[selected_testbed]["controller"]["url"] = request.config.getini("controller_url")
    if request.config.getini("firmware") != "0":
        version = request.config.getini("firmware")
        version_list = version.split(",")
        for i in range(len(CONFIGURATION[selected_testbed]["access_point"])):
            CONFIGURATION[selected_testbed]["access_point"][i]["version"] = version_list[0]
    allure.attach(name="Testbed Details", body=str(json.dumps(CONFIGURATION[selected_testbed], indent=2)),
                  attachment_type=allure.attachment_type.JSON)
    yield CONFIGURATION[selected_testbed]


@pytest.fixture(scope="session")
def get_controller_version(fixtures_ver, run_lf, cc_1):
    version = ""
    if not run_lf and not cc_1:
        version = fixtures_ver.get_sdk_version()
        print(version)
    yield version


@pytest.fixture(scope="session")
def get_dut_versions(fixtures_ver, run_lf, cc_1):
    version = ""
    if not run_lf and not cc_1:
        version = fixtures_ver.get_sdk_version()
        print(version)
    yield version


@pytest.fixture(scope="session")
def is_test_library_perfecto_android(request):
    interop = request.config.getoption("--use-perfecto-android")
    yield interop


@pytest.fixture(scope="session")
def is_test_library_perfecto_ios(request):
    interop = request.config.getoption("--use-perfecto-ios")
    yield interop


@pytest.fixture(scope="session")
def get_test_library(get_testbed_details, is_test_library_perfecto_android, is_test_library_perfecto_ios):
    if is_test_library_perfecto_android:
        obj = android_tests()
    elif is_test_library_perfecto_ios:
        obj = ios_tests()
    else:
        obj = lf_tests(lf_data=get_testbed_details["traffic_generator"],
                       dut_data=get_testbed_details["device_under_tests"],
                       log_level=logging.DEBUG,
                       run_lf=False,
                       influx_params=None)
    yield obj


@pytest.fixture(scope="session")
def execution_number(request):
    number = int(request.param)
    print(number)
    mode = "NAT-WAN"
    if number == 0:
        mode = "NAT-WAN"
    if number == 1:
        mode = "NAT-LAN"
    yield mode


@pytest.fixture(scope='session', autouse=True)
def add_allure_environment_property(request: SubRequest) -> Optional[Callable]:
    environment_properties = dict()

    def maker(key: str, value: Any):
        environment_properties.update({key: value})

    yield maker

    alluredir = request.config.getoption(ALLUREDIR_OPTION)

    if not alluredir or not os.path.isdir(alluredir) or not environment_properties:
        return

    allure_env_path = os.path.join(alluredir, ALLURE_ENVIRONMENT_PROPERTIES_FILE)

    with open(allure_env_path, 'w') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        _f.write(data)


@pytest.fixture(scope="function")
def get_dut_logs_per_test_case(request, get_testbed_details, get_target_object):
    S = 9
    instance_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    for i in range(len(get_testbed_details["device_under_tests"])):
        get_target_object.get_dut_library_object().run_generic_command(cmd="logger start testcase: " + instance_name,
                                                                       idx=i)

    def collect_logs():
        for i in range(len(get_testbed_details["device_under_tests"])):
            get_target_object.get_dut_library_object().run_generic_command(
                cmd="logger stop testcase: " + instance_name,
                idx=i)
            ap_logs = get_target_object.get_dut_library_object().get_logread(
                start_ref="start testcase: " + instance_name,
                stop_ref="stop testcase: " + instance_name)
            allure.attach(name='Logs - ' + get_testbed_details["device_under_tests"][i]["identifier"],
                          body=str(ap_logs))

    request.addfinalizer(collect_logs)


@pytest.fixture(scope="function")
def get_test_device_logs(request, get_testbed_details, get_target_object):
    ip = get_testbed_details["traffic_generator"]["details"]["manager_ip"]
    port = get_testbed_details["traffic_generator"]["details"]["ssh_port"]

    def collect_logs_tg():
        log_0 = "/home/lanforge/lanforge_log_0.txt"
        log_1 = "/home/lanforge/lanforge_log_1.txt"
        obj = scp_file(ip=ip, port=port, username="root", password="lanforge", remote_path=log_0,
                       local_path=".")
        obj.pull_file()
        allure.attach.file(source="lanforge_log_0.txt",
                           name="lanforge_log_0")
        obj = scp_file(ip=ip, port=port, username="root", password="lanforge", remote_path=log_1,
                       local_path=".")
        obj.pull_file()
        allure.attach.file(source="lanforge_log_1.txt",
                           name="lanforge_log_1")

    request.addfinalizer(collect_logs_tg)
