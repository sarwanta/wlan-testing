"""

    Performance Test: Country code along with Channel and Channel-width Test: Bridge Mode
    pytest -m "country_code and Bridge"

"""


import os
import pytest
import allure

pytestmark = [pytest.mark.country_code, pytest.mark.bridge, pytest.mark.wpa2, pytest.mark.united_states]

setup_params_general1 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 36},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-36)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel36(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel36
    @allure.title("Test for bandwidth 40 and channel 36")
    def test_client_bridge_wpa2_chn36_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel36"
        """
        profile_data = setup_params_general1["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general1['rf']['5G']['channel']
        channel_width = setup_params_general1['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general2 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 44},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-44)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel44(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel44
    @allure.title("Test for bandwidth 40 and channel 44")
    def test_client_bridge_wpa2_chn44_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel44"
        """
        profile_data = setup_params_general2["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general2['rf']['5G']['channel']
        channel_width = setup_params_general2['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general3 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 52},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-52)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel52(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel52
    @allure.title("Test for bandwidth 40 and channel 52")
    def test_client_bridge_wpa2_chn52_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel52"
        """
        profile_data = setup_params_general3["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general3['rf']['5G']['channel']
        channel_width = setup_params_general3['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general4 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 60},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-60)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel60(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel60
    @allure.title("Test for bandwidth 40 and channel 60")
    def test_client_bridge_wpa2_chn60_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel60"
        """
        profile_data = setup_params_general4["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general4['rf']['5G']['channel']
        channel_width = setup_params_general4['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general5 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 100},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-100)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel100(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel100
    @allure.title("Test for bandwidth 40 and channel 100")
    def test_client_bridge_wpa2_chn100_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel100"
        """
        profile_data = setup_params_general5["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general5['rf']['5G']['channel']
        channel_width = setup_params_general5['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general6 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 108},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-108)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel108(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel108
    @allure.title("Test for bandwidth 40 and channel 108")
    def test_client_bridge_wpa2_chn108_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel108"
        """
        profile_data = setup_params_general6["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general6['rf']['5G']['channel']
        channel_width = setup_params_general6['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general7 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 116},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-116)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel116(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel116
    @allure.title("Test for bandwidth 40 and channel 116")
    def test_client_bridge_wpa2_chn116_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel116"
        """
        profile_data = setup_params_general7["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general7['rf']['5G']['channel']
        channel_width = setup_params_general7['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general8 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 108},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-124)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel124(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel124
    @allure.title("Test for bandwidth 40 and channel 124")
    def test_client_bridge_wpa2_chn124_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel124"
        """
        profile_data = setup_params_general8["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general8['rf']['5G']['channel']
        channel_width = setup_params_general8['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general9 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 132},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-132)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel132(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel132
    @allure.title("Test for bandwidth 40 and channel 132")
    def test_client_bridge_wpa2_chn132_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel132"
        """
        profile_data = setup_params_general9["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general9['rf']['5G']['channel']
        channel_width = setup_params_general9['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general10 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 140},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-140)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel140(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel140
    @allure.title("Test for bandwidth 40 and channel 140")
    def test_client_bridge_wpa2_chn140_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel140"
        """
        profile_data = setup_params_general10["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general10['rf']['5G']['channel']
        channel_width = setup_params_general10['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general11 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 149},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-149)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel149(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel149
    @allure.title("Test for bandwidth 40 and channel 149")
    def test_client_bridge_wpa2_chn149_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel149"
        """
        profile_data = setup_params_general11["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general11['rf']['5G']['channel']
        channel_width = setup_params_general11['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


setup_params_general12 = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [{"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
                          ]},
    "rf": {"5G":
        {'band': '5G',
        'country': 'US',
        'channel-mode': 'VHT',
        'channel-width': 40,
        "channel": 157},
        "2G":
        {'band': '2G',
        'country': 'US',
        "channel-mode": "VHT",
        'channel-width': 40,
        "channel": 1}
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
@allure.suite("BRIDGE Mode(40 MHz)")
@allure.sub_suite("US country code (Channel-157)")
@pytest.mark.usefixtures("setup_configuration")
class TestCountryUS40Mhz5GChannel157(object):
    """Country code along with Channel and Channel-width Test Bridge mode
       pytest -m "country_code and Bridge"
    """
    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-2546", name="WIFI-6938")
    @pytest.mark.wpa2_personal
    @pytest.mark.fourtyMhz
    @pytest.mark.fiveg
    @pytest.mark.channel157
    @allure.title("Test for bandwidth 40 and channel 157")
    def test_client_bridge_wpa2_chn157_40Mhz_US_5g(self, get_test_library, setup_configuration):
        """Country code Bridge Mode
           pytest -m "country_code and fourtyMhz and wpa2 and fiveg and channel157"
        """
        profile_data = setup_params_general12["ssid_modes"]["wpa2_personal"][0]
        ssid = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        channel = setup_params_general12['rf']['5G']['channel']
        channel_width = setup_params_general12['rf']['5G']['channel-width']

        result = get_test_library.country_code_channel_division(ssid=ssid, security=security, passkey=security_key,
                                                       band=band,  vlan_id=vlan, channel=channel, mode=mode,
                                                       channel_width=channel_width,country_num=840,
                                                       country='United States(US)', dut_data=setup_configuration)
        if result:
            assert True
        else:
            assert False


