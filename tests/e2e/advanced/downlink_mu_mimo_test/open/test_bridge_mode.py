"""

    Performance Test: Downlink MU-MIMO Test: Bridge Mode
    pytest -m "downlink_mu_mimo and bridge and open and fiveg"

"""
import os
import pytest
import allure

pytestmark = [pytest.mark.advance, pytest.mark.downlink_mu_mimo, pytest.mark.bridge, pytest.mark.open, pytest.mark.report]

setup_params_general = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "open": [
            {"ssid_name": "mu-mimo-open-5g", "appliedRadios": ["5G"]},
            {"ssid_name": "mu-mimo-open-2g", "appliedRadios": ["2G"]}
        ]
    },
    "rf": {
        "5G": {
            "band": '5G',
            "channel": 149,
            "channel-width": 80
        },
        "2G": {
            "band": '2G',
            "channel": 11,
            "channel-width": 20
        }
    },
    "radius": False
}


@allure.suite("performance")
@allure.feature("BRIDGE MODE open security and Downlink MU_MIMO Test")
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestMuMimoBridge(object):
    """
    Downlink MU-MIMO Test: Bridge Mode
    pytest -m downlink_mu_mimo and bridge
    """

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-10086", name="WIFI-10086")
    @pytest.mark.open
    @pytest.mark.fiveg
    def test_mu_mimo_open_bridge_5g(self, lf_tools, lf_test, create_lanforge_chamberview_dut):
        """
            Downlink MU-MIMO Test: Bridge Mode
            pytest -m downlink_mu_mimo and bridge and open and fiveg
            """
        dut_name = create_lanforge_chamberview_dut
        mode = "BRIDGE"
        vlan = 1
        dut_5g, dut_2g = "", ""
        radios_2g, radios_5g, radios_ax = [], [], []
        data = lf_tools.json_get(_req_url="/port?fields=alias,port,mode")
        data = data['interfaces']
        port, port_data = "", []
        for i in data:
            for j in i:
                if i[j]['mode'] != '':
                    port_data.append(i)

        for item in range(len(port_data)):
            for p in port_data[item]:
                temp = port_data[item][p]['port'].split('.')
                temp = list(map(int, temp))
                temp = list(map(str, temp))
                port = ".".join(temp)
                if port_data[item][p]['mode'] == '802.11bgn-AC':
                    radios_2g.append(port + " " + port_data[item][p]['alias'])
                if port_data[item][p]['mode'] == '802.11an-AC':
                    radios_5g.append(port + " " + port_data[item][p]['alias'])
                if port_data[item][p]['mode'] == '802.11abgn-AX':
                    radios_ax.append(port + " " + port_data[item][p]['alias'])

        print(lf_tools.dut_idx_mapping)
        for i in lf_tools.dut_idx_mapping:
            if lf_tools.dut_idx_mapping[i][3] == "5G":
                dut_5g = dut_name + ' ' + lf_tools.dut_idx_mapping[i][0] + ' ' + lf_tools.dut_idx_mapping[i][4] + ' (1)'
                print(dut_5g)
            if lf_tools.dut_idx_mapping[i][3] == "2G":
                dut_2g = dut_name + ' ' + lf_tools.dut_idx_mapping[i][0] + ' ' + lf_tools.dut_idx_mapping[i][4] + ' (2)'
                print(dut_2g)
        mimo_obj = lf_test.downlink_mu_mimo(radios_2g=radios_2g, radios_5g=radios_5g, radios_ax=radios_ax, mode=mode,
                                            vlan_id=vlan, dut_name=dut_name, dut_5g=dut_5g, dut_2g=dut_2g, skip_2g=True,
                                            skip_5g=False)
        report_name = mimo_obj.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
        lf_tools.attach_report_graphs(report_name=report_name, pdf_name="Downlink MU-MIMO Test")
        result = lf_tools.read_kpi_file(column_name=["pass/fail"], dir_name=report_name)
        allure.attach.file(source="../reports/" + report_name + "/kpi.csv",
                           name="Downlink_MU_MIMO_info", attachment_type=allure.attachment_type.CSV)
        if result[0][0] == "PASS":
            assert True
        else:
            assert False

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-10087", name="WIFI-10087")
    @pytest.mark.open
    @pytest.mark.twog
    def test_mu_mimo_open_bridge_2g(self, lf_tools, lf_test, create_lanforge_chamberview_dut):
        """
            Downlink MU-MIMO Test: Bridge Mode
            pytest -m downlink_mu_mimo and bridge and open and twog
            """
        print('lf tool')
        dut_name = create_lanforge_chamberview_dut
        mode = "BRIDGE"
        vlan = 1
        dut_5g, dut_2g = "", ""
        radios_2g, radios_5g, radios_ax = [], [], []
        data = lf_tools.json_get(_req_url="/port?fields=alias,port,mode")
        data = data['interfaces']
        port, port_data = "", []
        for i in data:
            for j in i:
                if i[j]['mode'] != '':
                    port_data.append(i)

        for item in range(len(port_data)):
            for p in port_data[item]:
                temp = port_data[item][p]['port'].split('.')
                temp = list(map(int, temp))
                temp = list(map(str, temp))
                port = ".".join(temp)
                print(port)
                if port_data[item][p]['mode'] == '802.11bgn-AC':
                    radios_2g.append(port + " " + port_data[item][p]['alias'])
                if port_data[item][p]['mode'] == '802.11an-AC':
                    radios_5g.append(port + " " + port_data[item][p]['alias'])
                if port_data[item][p]['mode'] == '802.11abgn-AX':
                    radios_ax.append(port + " " + port_data[item][p]['alias'])

        print(lf_tools.dut_idx_mapping)
        for i in lf_tools.dut_idx_mapping:
            if lf_tools.dut_idx_mapping[i][3] == "5G":
                dut_5g = dut_name + ' ' + lf_tools.dut_idx_mapping[i][0] + ' ' + lf_tools.dut_idx_mapping[i][
                    4] + ' (1)'
                print(dut_5g)
            if lf_tools.dut_idx_mapping[i][3] == "2G":
                dut_2g = dut_name + ' ' + lf_tools.dut_idx_mapping[i][0] + ' ' + lf_tools.dut_idx_mapping[i][
                    4] + ' (2)'
                print(dut_2g)
        mimo_obj = lf_test.downlink_mu_mimo(radios_2g=radios_2g, radios_5g=radios_5g, radios_ax=radios_ax,
                                            mode=mode,
                                            vlan_id=vlan, dut_name=dut_name, dut_5g=dut_5g, dut_2g=dut_2g,
                                            skip_2g=False,
                                            skip_5g=True)
        report_name = mimo_obj.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
        lf_tools.attach_report_graphs(report_name=report_name, pdf_name="Downlink MU-MIMO Test")
        result = lf_tools.read_kpi_file(column_name=["pass/fail"], dir_name=report_name)
        if result[0][0] == "PASS":
            assert True
        else:
            assert False

