"""

    Performance Test: Dataplane Throughput Test: VLAN Mode
    pytest -m "dataplane_tests and vlan"

"""
import os
import pytest
import allure

pytestmark = [pytest.mark.vlan, pytest.mark.dataplane_tests, pytest.mark.wpa2_personal]

setup_params_general = {
    "mode": "VLAN",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "wpa2_personal_dataplane_2g", "appliedRadios": ["2G"], "security_key": "something",
             "vlan": 100},
            {"ssid_name": "wpa2_personal_dataplane_5g", "appliedRadios": ["5G"], "security_key": "something",
             "vlan": 100}]},
    "rf": {},
    "radius": False
}


@allure.feature("Dataplane Tests")
@allure.parent_suite("Dataplane Tests")
@allure.suite(suite_name="WPA2 Personal Security")
@allure.sub_suite(sub_suite_name="VLAN Mode")
@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_configuration")
class TestDataplaneThroughputVLAN(object):
    """Dataplane THroughput VLAN Mode
       pytest -m "dataplane_tests and wpa2_personal and vlan"
    """

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-3673", name="WIFI-3673")
    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @allure.title("Test for TCP UDP Download 2.4 GHz")
    def test_tcp_upd_wpa2_personal_vlan_2g_band(self, get_test_library, get_dut_logs_per_test_case,
                                                get_test_device_logs, client_type,
                                                get_target_object,
                                                num_stations, setup_configuration):
        """Dataplane THroughput VLAN Mode
           pytest -m "dataplane_tests and vlan and wpa2_personal and twog"
        """
        profile_data = {"ssid_name": "wpa2_personal_dataplane_2g", "appliedRadios": ["2G"], "security_key": "something",
             "vlan": 100}
        ssid_name = profile_data["ssid_name"]
        security = "wpa2"
        security_key = profile_data["security_key"]
        mode = "VLAN"
        band = "twog"
        vlan = [100]
        influx_tags = "dataplane-tcp-udp-vlan-wpa2_personal-2.4G"
        get_test_library.dataplane_throughput_test(ssid=ssid_name, security=security, passkey=security_key,
                                                   num_sta=1, mode=mode,
                                                   band=band, vlan_id=vlan,
                                                   instance_name="TIP_DPT_DPT_WPA2_2G_VLAN",
                                                   influx_tags=influx_tags, move_to_influx=False,
                                                   dut_data=setup_configuration
                                                   )

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-3674", name="WIFI-3674")
    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @allure.title("Test for TCP UDP Download 5 GHz")
    def test_tcp_upd_wpa2_personal_vlan_5g_band(self, get_test_library, get_dut_logs_per_test_case,
                                                get_test_device_logs, client_type,
                                                get_target_object,
                                                num_stations, setup_configuration):
        """Dataplane THroughput VLAN Mode
           pytest -m "dataplane_tests and vlan and wpa2_personal and fiveg"
        """
        profile_data = {"ssid_name": "wpa2_personal_dataplane_5g", "appliedRadios": ["5G"], "security_key": "something",
             "vlan": 100}
        ssid_name = profile_data["ssid_name"]
        security = "wpa2"
        security_key = profile_data["security_key"]
        mode = "VLAN"
        band = "fiveg"
        vlan = [100]
        influx_tags = "dataplane-tcp-udp-vlan-wpa2_personal-5G"
        get_test_library.dataplane_throughput_test(ssid=ssid_name, security=security, passkey=security_key,
                                                   num_sta=1, mode=mode,
                                                   band=band, vlan_id=vlan,
                                                   instance_name="TIP_DPT_DPT_WPA2_5G_VLAN",
                                                   influx_tags=influx_tags, move_to_influx=False,
                                                   dut_data=setup_configuration
                                                   )
