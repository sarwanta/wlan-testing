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
    verifyUploadDownloadSpeediOS, get_ip_address_eap_ios

pytestmark = [pytest.mark.sanity, pytest.mark.interop, pytest.mark.ios, pytest.mark.interop_ios, pytest.mark.client_connect
              ,pytest.mark.interop_uc_sanity, pytest.mark.vlan, pytest.mark.enterprise]

setup_params_enterprise = {
    "mode": "VLAN",
    "ssid_modes": {
        "wpa2_enterprise": [
            {"ssid_name": "ssid_wpa2_eap_2g_vlan", "appliedRadios": ["2G"], "vlan": 100},
            {"ssid_name": "ssid_wpa2_eap_5g_vlan", "appliedRadios": ["5G"], "vlan": 100}],
        "wpa3_enterprise": [
            {"ssid_name": "ssid_wpa3_eap_2g_vlan", "appliedRadios": ["2G"], "vlan": 100},
            {"ssid_name": "ssid_wpa3_eap_5g_vlan", "appliedRadios": ["5G"], "vlan": 100}],
        "wpa_enterprise": [
            {"ssid_name": "ssid_wpa_eap_2g_vlan", "appliedRadios": ["2G"], "vlan": 100},
            {"ssid_name": "ssid_wpa_eap_5g_vlan", "appliedRadios": ["5G"], "vlan": 100}]},

    "rf": {},
    "radius": True
}
class TestUniqueSSIDEnterpriseVLANiOS(object):

    @pytest.mark.unique_ssid_enterprise_vlan_ios
    def test_unique_ssid_enterprise_vlan_ios(self):
        for sec_modes in setup_params_enterprise['ssid_modes'].keys():
            for i in range(len(setup_params_enterprise['ssid_modes'][sec_modes])):
                N = 3
                rand_string = (''.join(random.choices(string.ascii_uppercase +
                                                      string.digits, k=N))) + str(int(time.time_ns()) % 10000)
                setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] = \
                    setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] + "_" + rand_string
            assert True

# for sec_modes in setup_params_enterprise['ssid_modes'].keys():
#     for i in range(len(setup_params_enterprise['ssid_modes'][sec_modes])):
#         N = 3
#         rand_string = (''.join(random.choices(string.ascii_uppercase +
#                                      string.digits, k=N)))+str(int(time.time_ns())%10000)
#         setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] = setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] + "_"+ rand_string

@allure.suite(suite_name="interop sanity")
@allure.sub_suite(sub_suite_name="Vlan Mode EAP Client Connect : Suite-A")
@pytest.mark.suiteA
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_enterprise],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestBridgeModeEnterpriseTTLSSuiteA(object):
    """ SuiteA Enterprise Test Cases
        pytest -m "client_connect and vlan and enterprise and ttls and interop and suiteA"
    """

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-4703", name="WIFI-4703")
    @pytest.mark.wpa2_enterprise
    @pytest.mark.fiveg
    def test_ClientConnect_5g_WPA2_Eap_Vlan(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):
        """ wpa2 enterprise 5g
            pytest -m "client_connect and vlan and enterprise and ttls and wpa_enterprise and fiveg"
        """
        profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][1]
        ssidName = profile_data["ssid_name"]
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
        ip, is_internet = get_ip_address_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS,
                                                 connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-4702", name="WIFI-4702")
    @pytest.mark.twog
    @pytest.mark.wpa2_enterprise
    def test_ClientConnect_2g_WPA2_Eap_Vlan(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):

        profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][0]
        ssidName = profile_data["ssid_name"]
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
        ip, is_internet = get_ip_address_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-4707", name="WIFI-4707")
    @pytest.mark.wpa3_enterprise
    @pytest.mark.fiveg
    def test_ClientConnect_5g_WPA3_Eap_Vlan(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):
        """ wpa2 enterprise 5g
            pytest -m "client_connect and vlan and enterprise and ttls and wpa_enterprise and fiveg"
        """
        profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][1]
        ssidName = profile_data["ssid_name"]
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
        ip, is_internet = get_ip_address_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS,
                                                 connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-4706", name="WIFI-4706")
    @pytest.mark.twog
    @pytest.mark.wpa3_enterprise
    def test_ClientConnect_2g_WPA3_Eap_Vlan(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):

        profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][0]
        ssidName = profile_data["ssid_name"]
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
        ip, is_internet = get_ip_address_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-4706", name="WIFI-4706")
    @pytest.mark.wpa_enterprise
    @pytest.mark.fiveg
    def test_ClientConnect_5g_WPA_Eap_Vlan(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):
        """ wpa enterprise 5g
            pytest -m "client_connect and vlan and enterprise and ttls and wpa_enterprise and fiveg"
        """
        profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][1]
        ssidName = profile_data["ssid_name"]
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
        ip, is_internet = get_ip_address_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS,
                                                 connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-4705", name="WIFI-4705")
    @pytest.mark.twog
    @pytest.mark.wpa_enterprise
    def test_ClientConnect_2g_WPA_Eap_Vlan(self, request, get_vif_state, get_ToggleAirplaneMode_data
                                       , setup_perfectoMobile_iOS, radius_info, get_ap_logs):

        profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][0]
        ssidName = profile_data["ssid_name"]
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
        ip, is_internet = get_ip_address_eap_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False