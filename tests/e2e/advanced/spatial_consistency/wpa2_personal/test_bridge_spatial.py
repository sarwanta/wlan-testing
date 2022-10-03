import pytest
import allure
import os
import time
import pandas as pd

pytestmark = [pytest.mark.advance, pytest.mark.spatial_consistency, pytest.mark.bridge, pytest.mark.report]

setup_params_general = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
            {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}
        ]
    },
    "rf": {
        "5G":{
            "channel-width": 80},
        "2G":{
            "channel-width": 20}
    },
    "radius": False
}
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class Test_SpatialConsistency_Bridge(object):

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5052", name="WIFI-5052")
    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @pytest.mark.degree0to360
    @pytest.mark.nss1_10db
    def test_dl_udp_nss1_wpa2_personal_2g_10db(self, lf_tools, lf_test, station_names_twog,
                                                create_lanforge_chamberview_dut, get_configuration ):
        print("Cleanup existing clients and traffic")
        lf_tools.reset_scenario()
        lf_test.Client_disconnect(clean_l3_traffic=True)
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_twog, vlan_id=vlan)
        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 1'], ['attenuator: ' + str(ser_no[0])], ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 100'],['attenuations2: 100'],['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_twog, mode=mode, download_rate="100%",
                                        instance_name="SPATIAL_NSS1_RVR1",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                              pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = "kpi.csv"
            pass_value = {"strong": 45}
            atn, deg = [10], [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330]  #
            if kpi in entries:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    start, thrpt_val, pass_fail = 0, {}, []
                    for i in pass_value:
                        count = 0
                        for j in range(start, len(kpi_val), len(atn)):
                            thrpt_val[f"{atn[start]}atn-{deg[count]}deg"] = kpi_val[j][0]
                            if kpi_val[j][0] >= pass_value[i]:
                                pass_fail.append("PASS")
                            else:
                                pass_fail.append("FAIL")
                            count += 1
                        # start += 6
                    print(thrpt_val, "\n", pass_fail)
                    if "FAIL" in pass_fail:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
                    else:
                        print("Test passed successfully")
                        assert True
                    # if float(str(kpi_val[0])[1:-1]) > float(45):
                    #     print("Test passed successfully")
                    #     assert True
                    # else:
                    #     print("Test failed due to lesser value")
                    #     assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5070", name="WIFI-5070")
    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @pytest.mark.degree0to360
    @pytest.mark.nss2_10db
    def test_dl_udp_nss2_wpa2_personal_2g_10db(self, lf_tools, lf_test, station_names_twog,
                                                create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_twog, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 2'], ['attenuator: ' + str(ser_no[0])], ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 100'], ['attenuations2: 100'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_twog, mode=mode,
                                        instance_name="SPATIAL_NSS2_RVR1",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(90):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5069", name="WIFI-5069")
    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @pytest.mark.nss1_38db
    @pytest.mark.degree0to360
    def test_dl_udp_nss1_wpa2_personal_2g_38db(self, lf_tools, lf_test, station_names_twog,
                                                create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_twog, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 1'],['attenuator: ' + str(ser_no[0])], ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 380'], ['attenuations2: 380'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_twog, mode=mode,
                                        instance_name="SPATIAL_NSS1_RVR1_Degree60",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break

            print("Test Completed... Cleaning up Stations")
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(45):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5068", name="WIFI-5068")
    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @pytest.mark.nss2_38db
    @pytest.mark.degree0to360
    def test_dl_udp_nss2_wpa2_personal_2g_38db(self, lf_tools, lf_test, station_names_twog,
                                                 create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_twog, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 2'], ['attenuator: ' + str(ser_no[0])], ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 380'], ['attenuations2: 380'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_twog, mode=mode,
                                        instance_name="SPATIAL_NSS2_RVR1_Degree60",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(90):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5063", name="WIFI-5063")
    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @pytest.mark.nss1_48db
    @pytest.mark.degree0to360
    def test_dl_udp_nss1_wpa2_personal_2g_48db(self, lf_tools, lf_test, station_names_twog,
                                                  create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_twog, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 1'], ['attenuator: ' + str(ser_no[0])],
               ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 480'], ['attenuations2: 480'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_twog, mode=mode,
                                        instance_name="SPATIAL_NSS1_RVR1_Degree120_twog_10db",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(45):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5062", name="WIFI-5062")
    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @pytest.mark.nss2_48db
    @pytest.mark.degree0to360
    def test_dl_udp_nss2_wpa2_personal_2g_48db(self, lf_tools, lf_test, station_names_twog,
                                                  create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_twog, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 2'], ['attenuator: ' + str(ser_no[0])],
               ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 480'], ['attenuations2: 480'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_twog, mode=mode,
                                        instance_name="SPATIAL_NSS2_RVR1_Degree120_twog_10db",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(90):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"


    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5067", name="WIFI-5067")
    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @pytest.mark.nss1_10db
    @pytest.mark.degree0to360
    def test_dl_udp_nss1_wpa2_personal_5g_10db(self, lf_tools, lf_test, station_names_fiveg,
                                                create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][1]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_fiveg, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 1'], ['attenuator: ' + str(ser_no[0])],
               ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 100'], ['attenuations2: 100'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_fiveg, mode=mode,
                                        instance_name="SPATIAL_NSS1_RVR1",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 5G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(250):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5066", name="WIFI-5066")
    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @pytest.mark.nss2_10db
    @pytest.mark.degree0to360
    def test_dl_udp_nss2_wpa2_personal_5g_10db(self, lf_tools, lf_test, station_names_fiveg,
                                                create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][1]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_fiveg, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 2'], ['attenuator: ' + str(ser_no[0])],
               ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 100'], ['attenuations2: 100'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_fiveg, mode=mode,
                                        instance_name="SPATIAL_NSS2_RVR1_Degree0_fiveg",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(500):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5065", name="WIFI-5065")
    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @pytest.mark.nss1_25db
    @pytest.mark.degree0to360
    def test_dl_udp_nss1_wpa2_personal_5g_25db(self, lf_tools, lf_test, station_names_fiveg,
                                                 create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][1]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_fiveg, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 1'], ['attenuator: ' + str(ser_no[0])],
               ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 250'], ['attenuations2: 250'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_fiveg, mode=mode,
                                        instance_name="SPATIAL_NSS1_RVR1_Degree60_fiveg",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(250):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5064", name="WIFI-5064")
    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @pytest.mark.nss2_25db
    @pytest.mark.degree0to360
    def test_dl_udp_nss2_wpa2_personal_5g_25db(self, lf_tools, lf_test, station_names_fiveg,
                                                 create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][1]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_fiveg, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 2'], ['attenuator: ' + str(ser_no[0])],
               ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 250'], ['attenuations2: 250'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_fiveg, mode=mode,
                                        instance_name="SPATIAL_NSS2_RVR1_Degree60_fiveg_10db",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range Test - UDP 2.4G")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(500):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5059", name="WIFI-5059")
    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @pytest.mark.nss1_35db
    @pytest.mark.degree0to360
    def test_dl_udp_nss1_wpa2_personal_5g_35db(self, lf_tools, lf_test, station_names_fiveg,
                                                 create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][1]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_fiveg, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 1'], ['attenuator: ' + str(ser_no[0])], ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 350'], ['attenuations2: 350'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_fiveg, mode=mode,
                                        instance_name="SPATIAL_NSS1_RVR1_Degree120_fiveg_10db",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range ")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(250):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"

    @allure.testcase(url="https://telecominfraproject.atlassian.net/browse/WIFI-5058", name="WIFI-5058")
    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @pytest.mark.nss2_35db
    @pytest.mark.degree0to360
    def test_dl_udp_nss2_wpa2_personal_5g_35db(self, lf_tools, lf_test, station_names_fiveg,
                                                  create_lanforge_chamberview_dut, get_configuration):
        lf_tools.reset_scenario()
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][1]
        ssid_name = profile_data["ssid_name"]
        security_key = profile_data["security_key"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "fiveg"
        vlan = 1
        dut_name = create_lanforge_chamberview_dut
        station = lf_test.Client_Connect(ssid=ssid_name, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_fiveg, vlan_id=vlan)

        ser_no = lf_test.attenuator_serial()
        print(ser_no)
        val = [['modes: Auto'], ['pkts: MTU'], ['directions: DUT Transmit'], ['traffic_types:UDP'],
               ['bandw_options: AUTO'], ['spatial_streams: 2'],['attenuator: ' + str(ser_no[0])], ['attenuator2: ' + str(ser_no[1])],
               ['attenuations: 350'], ['attenuations2: 350'], ['chamber: DUT-Chamber'], ['tt_deg: 0..+60..300']]
        if station:
            rvr_o = lf_test.ratevsrange(station_name=station_names_fiveg, mode=mode,
                                        instance_name="SPATIAL_NSS2_RVR1_Degree120_fiveg_10db",
                                        vlan_id=vlan, dut_name=dut_name, raw_lines=val)
            report_name = rvr_o.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]
            print("report name ", report_name)
            entries = os.listdir("../reports/" + report_name + '/')
            print("entries", entries)
            lf_tools.attach_report_graphs(report_name=report_name,
                                          pdf_name="Rate vs Range ")
            lf_test.Client_disconnect(clear_all_sta=True, clean_l3_traffic=True)
            print("Test Completed... Cleaning up Stations")
            kpi = False
            for i in entries:
                if "kpi.csv" in i:
                    kpi = i
                    break
            if kpi:
                kpi_val = lf_tools.read_kpi_file(column_name=["numeric-score"], dir_name=report_name)
                print(kpi_val)
                if str(kpi_val) == "empty":
                    print("Throughput value from kpi.csv is empty, Test failed")
                    allure.attach(name="CSV Data", body="Throughput value from kpi.csv is empty, Test failed")
                    assert False, "Throughput value from kpi.csv is empty, Test failed"
                else:
                    allure.attach(name="CSV Data", body="Throughput value : " + str(kpi_val))
                    if float(str(kpi_val[0])[1:-1]) > float(500):
                        print("Test passed successfully")
                        assert True
                    else:
                        print("Test failed due to lesser value")
                        assert False, "Test failed due to lesser value"
            else:
                print("csv file does not exist, Test failed")
                allure.attach(name="CSV Data", body="csv file does not exist")
                assert False, "csv file does not exist"
        else:
            print("Test failed due to no station ip")
            assert False, "Test failed due to no station ip"







