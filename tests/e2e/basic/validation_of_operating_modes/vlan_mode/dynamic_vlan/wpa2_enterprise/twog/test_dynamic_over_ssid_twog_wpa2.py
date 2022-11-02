"""

   Dynamic_Vlan: VLAN Mode
    pytest -m "dynamic_vlan_tests and wpa2_enterprise and vlan"

"""

import allure
import pytest
import importlib
import logging

lf_library = importlib.import_module("configuration")
DYNAMIC_VLAN_RADIUS_SERVER_DATA = lf_library.DYNAMIC_VLAN_RADIUS_SERVER_DATA
DYNAMIC_VLAN_RADIUS_ACCOUNTING_DATA = lf_library.DYNAMIC_VLAN_RADIUS_ACCOUNTING_DATA

pytestmark = [pytest.mark.dynamic_vlan_tests,
              pytest.mark.vlan,
              pytest.mark.ow_sanity_lf]

setup_params_general = {
    "mode": "VLAN",
    "ssid_modes": {
        "wpa2_enterprise": [
            {"ssid_name": "ssid_wpa2e_2g", "appliedRadios": ["2G"],
             "security_key": "something",
             "radius_auth_data": DYNAMIC_VLAN_RADIUS_SERVER_DATA,
             "radius_acc_data": DYNAMIC_VLAN_RADIUS_ACCOUNTING_DATA,
             "vlan": 100
             }]},
    "rf": {},
    "radius": True
}


@allure.parent_suite("Dynamic VLAN Test")
@allure.suite("WPA2 Enterprise Security")
@allure.sub_suite("2.4 GHz Band")
@allure.feature("Dynamic VLAN Test")
@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_configuration")
class TestDynamicVlanOverSsid2GWpa2(object):

    @pytest.mark.dynamic_precedence_over_ssid
    @pytest.mark.wpa2_enterprise
    @pytest.mark.twog
    @allure.title("Verify that Dynamic VLAN takes precedence over configured SSID VLAN")
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5705", name="WIFI-5705")
    def test_dynamic_precedence_over_ssid_vlan_2g_wpa2(self, get_test_library, get_dut_logs_per_test_case,
                                get_test_device_logs, num_stations, setup_configuration, check_connectivity):
        """
                To Verify that Dynamic VLAN takes precedence over configured SSID VLAN
              Unique Marker:  pytest -m "dynamic_precedence_over_ssid and wpa2_enterprise and vlan"

        """

        profile_data = setup_params_general["ssid_modes"]["wpa2_enterprise"]
        ssid_name = profile_data[0]["ssid_name"]
        mode = "VLAN"
        security = "wpa2"
        extra_secu = []
        band = "twog"
        vlan = [100,200]
        ttls_passwd = "passwordB"
        eap = "TTLS"
        identity = "userB"
        val = ""
        port_resources = list(get_test_library.lanforge_data['wan_ports'].keys())[0].split('.')

        passes, result = get_test_library.enterprise_client_connectivity_test(ssid=ssid_name, security=security,
                                                                  extra_securities=extra_secu,
                                                                  vlan_id=vlan, mode=mode, band=band, eap=eap, 
                                                                  ttls_passwd=ttls_passwd, ieee80211w=0, 
                                                                  identity=identity, num_sta=1, dut_data=setup_configuration)

        station_ip = get_test_library.station_data[list(get_test_library.station_data.keys())[0]]['ip']
        eth_ssid_vlan_ip = get_test_library.json_get("/port/" + port_resources[0] + "/" + port_resources[1] +
                                               "/" + port_resources[2] + "." + str(vlan[0]))["interface"]["ip"]
        eth_radius_vlan_ip = get_test_library.json_get("/port/" + port_resources[0] + "/" + port_resources[1] +
                                        "/" + port_resources[2] + "." + str(vlan[1]))["interface"]["ip"]
        eth_ip = get_test_library.json_get("/port/" + port_resources[0] + "/" + port_resources[1] +
                                   "/" + port_resources[2])["interface"]["ip"]

        sta_ip_1 = station_ip.split('.')
        eth_vlan_ip_1 = eth_radius_vlan_ip.split('.')
        logging.info(f"station ip...{sta_ip_1}\neth.{vlan[0]}...{eth_ssid_vlan_ip}\neth.{vlan[1]}...{eth_radius_vlan_ip}"
                     f"\neth_upstream_ip...{eth_ip}")
        if sta_ip_1[0] == "0":
            assert False, result
        elif eth_vlan_ip_1[0] == "0":
            assert False, result
        for i, j in zip(sta_ip_1[0:2], eth_vlan_ip_1[0:2]):
            if i != j:
                val = False
            else:
                val = True
        if val:
            assert True, result
        elif not val:
            assert False, result