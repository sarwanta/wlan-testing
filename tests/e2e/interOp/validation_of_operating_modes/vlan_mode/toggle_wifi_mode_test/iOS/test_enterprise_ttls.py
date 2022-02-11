from logging import exception
import io
import unittest
import warnings
from perfecto.test import TestResultFactory
import pytest
import sys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import string
import sys
import allure

if 'perfecto_libs' not in sys.path:
    sys.path.append(f'../libs/perfecto_libs')

from iOS_lib import closeApp, openApp, get_WifiIPAddress_iOS, ForgetWifiConnection, ping_deftapps_iOS, \
    Toggle_AirplaneMode_iOS, set_APconnMobileDevice_iOS, verify_APconnMobileDevice_iOS, Toggle_WifiMode_iOS, tearDown,\
    verifyUploadDownloadSpeediOS, get_ip_add_eap_ios, get_ip_add_check_ios, wifi_connect_eap, wifi_disconnect_and_forget

pytestmark = [pytest.mark.regression, pytest.mark.interop, pytest.mark.ios, pytest.mark.interop_ios, pytest.mark.client_reconnect
              , pytest.mark.vlan, pytest.mark.enterprise, pytest.mark.ToggleWifiMode]

setup_params_enterprise = {
    "mode": "VLAN",
    "ssid_modes": {
        "wpa2_enterprise": [
            {"ssid_name": "ssid_wpa2_eap_2g", "appliedRadios": ["2G"], "vlan": 100},
            {"ssid_name": "ssid_wpa2_eap_5g", "appliedRadios": ["5G"], "vlan": 100}],
        "wpa3_enterprise": [
            {"ssid_name": "ssid_wpa3_eap_2g", "appliedRadios": ["2G"], "vlan": 100},
            {"ssid_name": "ssid_wpa3_eap_5g", "appliedRadios": ["5G"], "vlan": 100}],
        "wpa_enterprise": [
            {"ssid_name": "ssid_wpa_eap_2g", "appliedRadios": ["2G"], "vlan": 100},
            {"ssid_name": "ssid_wpa_eap_5g", "appliedRadios": ["5G"], "vlan": 100}]},

    "rf": {},
    "radius": True
}
for sec_modes in setup_params_enterprise['ssid_modes'].keys():
    for i in range(len(setup_params_enterprise['ssid_modes'][sec_modes])):
        N = 3
        rand_string = (''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=N)))+str(int(time.time_ns())%10000)
        setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] = setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] + "_"+ rand_string

@allure.suite(suite_name="interop regression")
@allure.sub_suite(sub_suite_name="VLAN Mode EAP Client ReConnect : Suite-A")
@pytest.mark.suiteA
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_enterprise],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestToggleWifiModeVLANModeEnterpriseTTLSSuiteA(object):
    """ SuiteA Enterprise Test Cases
        pytest -m "client_reconnect and nat and enterprise and ttls and interop and suiteA"
    """

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6639", name="WIFI-6639")
    @pytest.mark.wpa2_enterprise
    @pytest.mark.fiveg
    def test_ToggleWifiMode_5g_WPA2_Eap_VLAN(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):
        profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][1]
        ssidName = profile_data["ssid_name"]
        ssidPassword = ["BLANK"]
        print("SSID_NAME: " + ssidName)
        # print ("SSID_PASS: " + ssidPassword)
        ttls_passwd = radius_info["password"]
        identity = radius_info['user']
        get_vif_state.append(ssidName)
        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_iOS[1]
        driver = setup_perfectoMobile_iOS[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_add_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_WifiMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = get_ip_add_check_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6640", name="WIFI-6640")
    @pytest.mark.twog
    @pytest.mark.wpa2_enterprise
    def test_ToggleWifiMode_2g_WPA2_Eap_VLAN(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):

        profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][0]
        ssidName = profile_data["ssid_name"]
        ssidPassword = ["BLANK"]
        # ssidPassword = profile_data["security_key"]
        print("SSID_NAME: " + ssidName)
        # print ("SSID_PASS: " + ssidPassword)
        ttls_passwd = radius_info["password"]
        identity = radius_info['user']
        get_vif_state.append(ssidName)
        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_iOS[1]
        driver = setup_perfectoMobile_iOS[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_add_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_WifiMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = get_ip_add_check_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6641", name="WIFI-6641")
    @pytest.mark.wpa3_enterprise
    @pytest.mark.fiveg
    def test_ToggleWifiMode_5g_WPA3_Eap_VLAN(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):
        """ wpa2 enterprise 5g
            pytest -m "client_connect and bridge and enterprise and ttls and wpa_enterprise and fiveg"
        """
        profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][1]
        ssidName = profile_data["ssid_name"]
        ssidPassword = ["BLANK"]
        # ssidPassword = profile_data["security_key"]
        print("SSID_NAME: " + ssidName)
        # print ("SSID_PASS: " + ssidPassword)
        ttls_passwd = radius_info["password"]
        identity = radius_info['user']
        get_vif_state.append(ssidName)
        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_iOS[1]
        driver = setup_perfectoMobile_iOS[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_add_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS,
                                                 connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_WifiMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = get_ip_add_check_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6642", name="WIFI-6642")
    @pytest.mark.twog
    @pytest.mark.wpa3_enterprise
    def test_ToggleWifiMode_2g_WPA3_Eap_VLAN(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):

        profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][0]
        ssidName = profile_data["ssid_name"]
        ssidPassword = ["BLANK"]
        # ssidPassword = profile_data["security_key"]
        print("SSID_NAME: " + ssidName)
        # print ("SSID_PASS: " + ssidPassword)
        ttls_passwd = radius_info["password"]
        identity = radius_info['user']
        get_vif_state.append(ssidName)
        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_iOS[1]
        driver = setup_perfectoMobile_iOS[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_add_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_WifiMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = get_ip_add_check_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6637", name="WIFI-6637")
    @pytest.mark.wpa_enterprise
    @pytest.mark.fiveg
    def test_ToggleWifiMode_5g_WPA_Eap_VLAN(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):
        """ wpa enterprise 5g
            pytest -m "client_connect and bridge and enterprise and ttls and wpa_enterprise and fiveg"
        """
        profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][1]
        ssidName = profile_data["ssid_name"]
        ssidPassword = ["BLANK"]
        print("SSID_NAME: " + ssidName)
        # print ("SSID_PASS: " + ssidPassword)
        ttls_passwd = radius_info["password"]
        identity = radius_info['user']
        get_vif_state.append(ssidName)
        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_iOS[1]
        driver = setup_perfectoMobile_iOS[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_add_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_WifiMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = get_ip_add_check_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6638", name="WIFI-6638")
    @pytest.mark.twog
    @pytest.mark.wpa_enterprise
    def test_ToggleWifiMode_2g_WPA_Eap_VLAN(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):

        profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][0]
        ssidName = profile_data["ssid_name"]
        ssidPassword = ["BLANK"]
        # ssidPassword = profile_data["security_key"]
        print("SSID_NAME: " + ssidName)
        # print ("SSID_PASS: " + ssidPassword)
        ttls_passwd = radius_info["password"]
        identity = radius_info['user']
        get_vif_state.append(ssidName)
        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_iOS[1]
        driver = setup_perfectoMobile_iOS[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_add_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_WifiMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = get_ip_add_check_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False