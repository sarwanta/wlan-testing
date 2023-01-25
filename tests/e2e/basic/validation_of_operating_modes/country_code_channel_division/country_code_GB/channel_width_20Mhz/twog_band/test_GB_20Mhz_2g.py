"""

    Performance Test: Country code along with Channel and Channel-width Test: Bridge Mode
    pytest -m "country_code and Bridge"

"""


import os
import pytest
import allure

pytestmark = [pytest.mark.country_code, pytest.mark.bridge, pytest.mark.wpa2, pytest.mark.united_kingdom]

setup_params_general1 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 1}
           },
    "radius": False
}


@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general1],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-1)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel1(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel1
    @allure.title("Test for bandwidth 20 and channel 1")
    def test_client_bridge_wpa2_chn1_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel1"
        """
        profile_data = setup_params_general1["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general1['rf']['2G']['channel']
        channel_width = setup_params_general1['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general2 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 2}
           },
    "radius": False
}


@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general2],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-2)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel2(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel2
    @allure.title("Test for bandwidth 20 and channel 2")
    def test_client_bridge_wpa2_chn2_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel2"
        """
        profile_data = setup_params_general2["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general2['rf']['2G']['channel']
        channel_width = setup_params_general2['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general3 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 3}
           },
    "radius": False
}


@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general3],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-3)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel3(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel3
    @allure.title("Test for bandwidth 20 and channel 3")
    def test_client_bridge_wpa2_chn3_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel3"
        """
        profile_data = setup_params_general3["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general3['rf']['2G']['channel']
        channel_width = setup_params_general3['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general4 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 4}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general4],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-4)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel4(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel4
    @allure.title("Test for bandwidth 20 and channel 4")
    def test_client_bridge_wpa2_chn4_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel4"
        """
        profile_data = setup_params_general4["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general4['rf']['2G']['channel']
        channel_width = setup_params_general4['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general5 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 5}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general5],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-5)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel5(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel5
    @allure.title("Test for bandwidth 20 and channel 5")
    def test_client_bridge_wpa2_chn5_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel5"
        """
        profile_data = setup_params_general5["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general5['rf']['2G']['channel']
        channel_width = setup_params_general5['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general6 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 6}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general6],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-6)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel6(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel6
    @allure.title("Test for bandwidth 20 and channel 6")
    def test_client_bridge_wpa2_chn6_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel6"
        """
        profile_data = setup_params_general6["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general6['rf']['2G']['channel']
        channel_width = setup_params_general6['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general7 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 7}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general7],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-7)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel7(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel7
    @allure.title("Test for bandwidth 20 and channel 7")
    def test_client_bridge_wpa2_chn7_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel7"
        """
        profile_data = setup_params_general7["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general7['rf']['2G']['channel']
        channel_width = setup_params_general7['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general8 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 8}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general8],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-8)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel8(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel8
    @allure.title("Test for bandwidth 20 and channel 8")
    def test_client_bridge_wpa2_chn8_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel8"
        """
        profile_data = setup_params_general8["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general8['rf']['2G']['channel']
        channel_width = setup_params_general8['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general9 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 9}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general9],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-9)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel9(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel9
    @allure.title("Test for bandwidth 20 and channel 9")
    def test_client_bridge_wpa2_chn9_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel9"
        """
        profile_data = setup_params_general9["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general9['rf']['2G']['channel']
        channel_width = setup_params_general9['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general10 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 10}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general10],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-10)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel10(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel10
    @allure.title("Test for bandwidth 20 and channel 10")
    def test_client_bridge_wpa2_chn10_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel10"
        """
        profile_data = setup_params_general10["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general10['rf']['2G']['channel']
        channel_width = setup_params_general10['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general11 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 11}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general11],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-11)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel11(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel11
    @allure.title("Test for bandwidth 20 and channel 11")
    def test_client_bridge_wpa2_chn11_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel11"
        """
        profile_data = setup_params_general11["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general11['rf']['2G']['channel']
        channel_width = setup_params_general11['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general12 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 12}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general12],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-12)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel12(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel12
    @allure.title("Test for bandwidth 20 and channel 12")
    def test_client_bridge_wpa2_chn12_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel12"
        """
        profile_data = setup_params_general12["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general12['rf']['2G']['channel']
        channel_width = setup_params_general12['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general13 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
                          {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {
        "5G":
        {'band': '5G',
        'country': 'GB',
        "channel-mode": "VHT",
        'channel-width': 20,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'GB',
        'channel-mode': 'VHT',
        'channel-width': 20,
        "channel": 13}
           },
    "radius": False
}

@pytest.mark.parametrize(
    'setup_configuration',
    [setup_params_general13],
    indirect=True,
    scope="class"
)
@allure.feature("Channel vs Country Code")
@allure.parent_suite("Country Code Tests")
@allure.suite("BRIDGE Mode(20 MHz)")
@allure.sub_suite("GB country code (Channel-13)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryGB20Mhz2GChannel13(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.twentyMhz
    @pytest.mark.twog
    @pytest.mark.channel13
    @allure.title("Test for bandwidth 20 and channel 13")
    def test_client_bridge_wpa2_chn13_20Mhz_GB_2g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and twentyMhz and wpa2 and twog and channel13"
        """
        profile_data = setup_params_general13["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        channel = setup_params_general13['rf']['2G']['channel']
        channel_width = setup_params_general13['rf']['2G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=826,
                                                       country='United Kingdom(GB)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False
