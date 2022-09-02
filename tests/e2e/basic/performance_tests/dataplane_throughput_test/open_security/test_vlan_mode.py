"""

    Performance Test: Dataplane Throughput Test: VLAN Mode
    pytest -m "dataplane_throughput_test and vlan"

"""
import os
import pytest
import allure

pytestmark = [pytest.mark.vlan, pytest.mark.dataplane_throughput_test]

setup_params_general = {
    "mode": "VLAN",
    "ssid_modes": {
        "open": [
            {"ssid_name": "ssid_open_2g", "appliedRadios": ["2G"], "vlan": 100},
            {"ssid_name": "ssid_open_5g", "appliedRadios": ["5G"], "vlan": 100}]},
    "rf": {},
    "radius": False
}


@allure.suite("performance")
@allure.feature("VLAN MODE open security and Dataplane Throughput Test")
@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_configuration")
class TestDataplaneThroughputVLAN(object):
    """Dataplane THroughput VLAN Mode
       pytest -m "dataplane_throughput_test and open and VLAN"
    """

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-3673", name="WIFI-3673")
    @pytest.mark.open
    @pytest.mark.twog
    def test_tcp_upd_open_vlan_2g_band(self, get_test_library, get_dut_logs_per_test_case,
                                       get_test_device_logs,
                                       get_target_object,
                                       num_stations):
        """Dataplane THroughput VLAN Mode
           pytest -m "dataplane_throughput_test and VLAN and open and twog"
        """
        profile_data = setup_params_general["ssid_modes"]["open"][0]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "open"
        mode = "VLAN"
        band = "twog"
        vlan = [100]
        influx_tags = "dataplane-tcp-udp-vlan-open-2.4G"
        get_test_library.dataplane_throughput_test(ssid=ssid_name, security=security,
                                                   num_sta=1, mode=mode,
                                                   band=band, vlan_id=vlan,
                                                   instance_name="TIP_DPT_DPT_OPEN_2G_VLAN",
                                                   influx_tags=influx_tags, move_to_influx=False,
                                                   )

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-3674", name="WIFI-3674")
    @pytest.mark.open
    @pytest.mark.fiveg
    def test_tcp_upd_open_vlan_5g_band(self, get_test_library, get_dut_logs_per_test_case,
                                       get_test_device_logs,
                                       get_target_object,
                                       num_stations):
        """Dataplane THroughput VLAN Mode
           pytest -m "dataplane_throughput_test and VLAN and open and fiveg"
        """
        profile_data = setup_params_general["ssid_modes"]["open"][1]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "open"
        mode = "VLAN"
        band = "fiveg"
        vlan = [100]
        influx_tags = "dataplane-tcp-udp-vlan-open-5G"
        get_test_library.dataplane_throughput_test(ssid=ssid_name, security=security,
                                                   num_sta=1, mode=mode,
                                                   band=band, vlan_id=vlan,
                                                   instance_name="TIP_DPT_DPT_OPEN_5G_VLAN",
                                                   influx_tags=influx_tags, move_to_influx=False,
                                                   )

