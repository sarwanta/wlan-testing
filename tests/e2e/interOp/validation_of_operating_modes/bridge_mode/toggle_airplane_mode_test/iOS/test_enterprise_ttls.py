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

if 'perfecto_interop' not in sys.path:
    sys.path.append(f'../libs/perfecto_interop')

from iOS_lib import closeApp, openApp, get_WifiIPAddress_iOS, ForgetWifiConnection, ping_deftapps_iOS, \
    Toggle_AirplaneMode_iOS, set_APconnMobileDevice_iOS, verify_APconnMobileDevice_iOS, Toggle_WifiMode_iOS, tearDown,\
    verifyUploadDownloadSpeediOS, gets_ip_add_eap_and_does_not_forget_ssid_ios, gets_ip_add_for_checking_and_forgets_ssid_ios, wifi_connect_eap, wifi_disconnect_and_forget

pytestmark = [pytest.mark.regression, pytest.mark.interop, pytest.mark.ios, pytest.mark.interop_ios, pytest.mark.client_reconnect
              , pytest.mark.bridge, pytest.mark.enterprise, pytest.mark.ToggleAirplaneMode]

setup_params_enterprise = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_enterprise": [
            {"ssid_name": "ssid_wpa2_eap_2g", "appliedRadios": ["2G"]},
            {"ssid_name": "ssid_wpa2_eap_5g", "appliedRadios": ["5G"]}],
        "wpa3_enterprise": [
            {"ssid_name": "ssid_wpa3_eap_2g", "appliedRadios": ["2G"]},
            {"ssid_name": "ssid_wpa3_eap_5g", "appliedRadios": ["5G"]}],
        "wpa_enterprise": [
            {"ssid_name": "ssid_wpa_eap_2g", "appliedRadios": ["2G"]},
            {"ssid_name": "ssid_wpa_eap_5g", "appliedRadios": ["5G"]}]},

    "rf": {},
    "radius": True
}
for sec_modes in setup_params_enterprise['ssid_modes'].keys():
    for i in range(len(setup_params_enterprise['ssid_modes'][sec_modes])):
        N = 3
        rand_string = (''.join(random.choices(string.ascii_uppercase +
                                     string.digits, k=N)))+str(int(time.time_ns())%10000)
        setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] = setup_params_enterprise['ssid_modes'][sec_modes][i]['ssid_name'] + "_"+ rand_string

@allure.suite(suite_name="interop Regression")
@allure.sub_suite(sub_suite_name="Bridge Mode EAP Client ReConnect : Suite-A")
@pytest.mark.suiteA
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_enterprise],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestToggleAirplaneModeBridgeModeEnterpriseTTLSSuiteA(object):
    """ SuiteA Enterprise Test Cases
        pytest -m "client_reconnect and bridge and enterprise and ttls and interop and suiteA"
    """

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6545", name="WIFI-6545")
    @pytest.mark.wpa2_enterprise
    @pytest.mark.fiveg
    def test_ToggleAirplaneMode_5g_WPA2_Eap_Bridge(self, request, get_vif_state, get_ToggleAirplaneMode_data
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
        ip, is_internet = gets_ip_add_eap_and_does_not_forget_ssid_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_AirplaneMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = gets_ip_add_for_checking_and_forgets_ssid_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6546", name="WIFI-6546")
    @pytest.mark.twog
    @pytest.mark.wpa2_enterprise
    def test_ToggleAirplaneMode_2g_WPA2_Eap_Bridge(self, request, get_vif_state, get_ToggleAirplaneMode_data
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
        ip, is_internet = gets_ip_add_eap_and_does_not_forget_ssid_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_AirplaneMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = gets_ip_add_for_checking_and_forgets_ssid_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6547", name="WIFI-6547")
    @pytest.mark.wpa3_enterprise
    @pytest.mark.fiveg
    def test_ToggleAirplaneMode_5g_WPA3_Eap_Bridge(self, request, get_vif_state, get_ToggleAirplaneMode_data
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
        ip, is_internet = gets_ip_add_eap_and_does_not_forget_ssid_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS,
                                                 connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_AirplaneMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = gets_ip_add_for_checking_and_forgets_ssid_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6548", name="WIFI-6548")
    @pytest.mark.twog
    @pytest.mark.wpa3_enterprise
    def test_ToggleAirplaneMode_2g_WPA3_Eap_Bridge(self, request, get_vif_state, get_ToggleAirplaneMode_data
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
        ip, is_internet = gets_ip_add_eap_and_does_not_forget_ssid_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_AirplaneMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = gets_ip_add_for_checking_and_forgets_ssid_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6543", name="WIFI-6543")
    @pytest.mark.wpa_enterprise
    @pytest.mark.fiveg
    def test_ToggleAirplaneMode_5g_WPA_Eap_Bridge(self, request, get_vif_state, get_ToggleAirplaneMode_data
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
        ip, is_internet = gets_ip_add_eap_and_does_not_forget_ssid_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_AirplaneMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = gets_ip_add_for_checking_and_forgets_ssid_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-6544", name="WIFI-6544")
    @pytest.mark.twog
    @pytest.mark.wpa_enterprise
    def test_ToggleAirplaneMode_2g_WPA_Eap_Bridge(self, request, get_vif_state, get_ToggleAirplaneMode_data
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
        ip, is_internet = gets_ip_add_eap_and_does_not_forget_ssid_ios(request, ssidName, identity, ttls_passwd, setup_perfectoMobile_iOS, connData)

        if is_internet:
            if ip:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + "with Internet, couldn't get IP address")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))

            # wifi_connect(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
            Toggle_AirplaneMode_iOS(request, setup_perfectoMobile_iOS, connData)
            ip_check, is_internet_check = gets_ip_add_for_checking_and_forgets_ssid_ios(request, ssidName, ssidPassword,
                                                               setup_perfectoMobile_iOS, connData)
            if (ip_check == ip):
                assert True
            else:
                assert False
        else:
            allure.attach(name="Connection Status: ", body=str("No Internet access"))
            assert False
