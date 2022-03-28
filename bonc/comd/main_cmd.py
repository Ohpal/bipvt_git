import os, sys
import time
import datetime
import struct

import comd.var
import comd.control_ui
import comd.read_cmd
import db.pg_connect

import ui.error_Activity
import comd.openweather

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

bipvt_before_time = ''
weather_trigger = False

def now_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now


def error_len():
    cnt = db.sqlite_connect.error_count()
    return cnt


def mainLoop():
    # data select time
    d_time = now_time()

    # 메인화면 시간 표시
    try:
        comd.control_ui.main_timer()
    except:
        pass

    # 통신 확인
    try:
        comd.control_ui.set_connect_ui()
    except:
        pass

    # 화면 데이터 표시
    try:
        if comd.var.bipvt_connect_status:
            bipvt_datas = comd.var.bipvt_temp_data

            # BIPVT 데이터에 시간 넣음
            d_time = now_time()
            insolation = bipvt_datas[0]
            outer_temp = bipvt_datas[1]
            outer_humi = bipvt_datas[2]
            wind_speed = bipvt_datas[4]
            wind_direct = bipvt_datas[5]
            rain_amount = bipvt_datas[7]
            today_rain_amount = bipvt_datas[8]
            bipvt_inside_temp1 = bipvt_datas[26]
            bipvt_inside_temp2 = bipvt_datas[28]
            bipvt_inside_temp3 = bipvt_datas[30]
            bipvt_inner_temp = bipvt_datas[26]
            bipvt_inner_humi = bipvt_datas[27]
            bipvt_outer_temp = round(float((bipvt_datas[26] + bipvt_datas[28] + bipvt_datas[30])/3), 1)
            bipvt_outer_humi = round(float((bipvt_datas[27] + bipvt_datas[29] + bipvt_datas[31])/3), 1)
            exchanger_outer_temp = bipvt_datas[30]
            exchanger_outer_humi = bipvt_datas[31]
            inside_temp = bipvt_datas[17]
            inside_humi = bipvt_datas[18]
            fan_status = 'ON' if bipvt_datas[32] or bipvt_datas[34] else 'OFF'
            damper_status1 = 'ON' if bipvt_datas[20] > 0 else 'OFF'
            damper_status2 = 'ON' if bipvt_datas[21] > 0 else 'OFF'
            damper_status3 = 'ON' if bipvt_datas[22] > 0 else 'OFF'
            exchanger_status = 'ON' if bipvt_datas[19] else 'OFF'
            pv_power = bipvt_datas[46] + bipvt_datas[48]
            pv_power_total = bipvt_datas[47] + bipvt_datas[49]
            storage_power = bipvt_datas[42]
            storage_power_total = bipvt_datas[43]
            heatpump_power = bipvt_datas[38]
            heatpump_power_total = bipvt_datas[39]
            buffer_power = bipvt_datas[40]
            buffer_power_total = bipvt_datas[41]
            heatline_power = bipvt_datas[52] + bipvt_datas[54] + bipvt_datas[56] + bipvt_datas[58] + bipvt_datas[60]
            heatline_power_total = bipvt_datas[53] + bipvt_datas[55] + bipvt_datas[57] + bipvt_datas[59] + bipvt_datas[61]
            dhw_power = bipvt_datas[50]
            dhw_power_total = bipvt_datas[51]
            load_power = storage_power + heatpump_power + buffer_power + heatline_power + dhw_power
            load_power_total = storage_power_total + heatpump_power_total + buffer_power_total + heatline_power_total + dhw_power_total
            t4_temp = bipvt_datas[9]
            t5_temp = bipvt_datas[10]
            t13_temp = bipvt_datas[11]
            t16_temp = bipvt_datas[12]

            fm3_flux = bipvt_datas[13]
            fm4_flux = bipvt_datas[14]
            fm5_flux = bipvt_datas[15]
            fm6_flux = bipvt_datas[16]

            bipvt_packet = [
                d_time,
                insolation,
                outer_temp,
                outer_humi,
                wind_speed,
                wind_direct,
                rain_amount,
                today_rain_amount,
                bipvt_inside_temp1,
                bipvt_inside_temp2,
                bipvt_inside_temp3,
                bipvt_inner_temp,
                bipvt_inner_humi,
                bipvt_outer_temp,
                bipvt_outer_humi,
                exchanger_outer_temp,
                exchanger_outer_humi,
                inside_temp,
                inside_humi,
                fan_status,
                damper_status1,
                damper_status2,
                damper_status3,
                exchanger_status,
                pv_power,
                pv_power_total,
                storage_power,
                storage_power_total,
                heatpump_power,
                heatpump_power_total,
                buffer_power,
                buffer_power_total,
                heatline_power,
                heatline_power_total,
                dhw_power,
                dhw_power_total,
                t4_temp,
                t5_temp,
                t13_temp,
                t16_temp,
                fm3_flux,
                fm4_flux,
                fm5_flux,
                fm6_flux
            ]
            print(bipvt_packet)
            comd.var.bipvt_read = True
        else:
            comd.var.bipvt_read = False
            insolation = ' - '
            outer_temp = ' - '
            outer_humi = ' - '
            wind_speed = ' - '
            wind_direct = ' - '
            rain_amount = ' - '
            today_rain_amount = ' - '
            bipvt_inside_temp1 = ' - '
            bipvt_inside_temp2 = ' - '
            bipvt_inside_temp3 = ' - '
            bipvt_inner_temp = ' - '
            bipvt_inner_humi = ' - '
            bipvt_outer_temp = ' - '
            bipvt_outer_humi = ' - '
            exchanger_outer_temp = ' - '
            exchanger_outer_humi = ' - '
            inside_temp = ' - '
            inside_humi = ' - '
            fan_status = ' - '
            damper_status1 = ' - '
            damper_status2 = ' - '
            damper_status3 = ' - '
            exchanger_status = ' - '
            pv_power = ' - '
            pv_power_total = ' - '
            storage_power = ' - '
            storage_power_total = ' - '
            heatpump_power = ' - '
            heatpump_power_total = ' - '
            buffer_power = ' - '
            buffer_power_total = ' - '
            heatline_power = ' - '
            heatline_power_total = ' - '
            dhw_power = ' - '
            dhw_power_total = ' - '
            load_power = ' - '
            load_power_total = ' - '
            t4_temp = ' - '
            t5_temp = ' - '
            t13_temp = ' - '
            t16_temp = ' - '
            fm3_flux = ' - '
            fm4_flux = ' - '
            fm5_flux = ' - '
            fm6_flux = ' - '

    except Exception as ex:
        comd.var.bipvt_read = False
        print('BIPVT READ Error : ', ex)

    try:
        if comd.var.heatpump_connect_status:
            heatpump_read_datas = comd.read_cmd.heatpump_read_data()
            storage_inner_temp = heatpump_read_datas.getRegister(0) * 0.1
            storage_outer_temp = heatpump_read_datas.getRegister(1) * 0.1
            dhw_inner_temp = heatpump_read_datas.getRegister(2) * 0.1
            dhw_outer_temp = heatpump_read_datas.getRegister(3) * 0.1
            dhw_tank_temp = heatpump_read_datas.getRegister(4) * 0.1
            buffer_inner_temp = heatpump_read_datas.getRegister(5) * 0.1
            buffer_tank_temp = heatpump_read_datas.getRegister(6) * 0.1

            heatpump_mode_datas = comd.read_cmd.heatpump_mode_data()

            heatpump_modes = heatpump_mode_datas.getRegister(0)
            heatpump_statuss = heatpump_mode_datas.getRegister(1)

            if heatpump_modes == 0:
                heatpump_mode = '냉방'
            elif heatpump_modes == 1:
                heatpump_mode = '난방'
            elif heatpump_modes == 2:
                heatpump_mode = '급탕'
            elif heatpump_modes == 3:
                heatpump_mode = '제상'
            else:
                heatpump_mode = '대기'

            if heatpump_statuss == 0:
                heatpump_status = '운전대기'
            elif heatpump_statuss == 1:
                heatpump_status = '운전중'
            elif heatpump_statuss == 2:
                heatpump_status = '알람정지'
            elif heatpump_statuss == 4:
                heatpump_status = '원격정지'
            elif heatpump_statuss == 5:
                heatpump_status = '예약정지'
            elif heatpump_statuss == 6:
                heatpump_status = '접점정지'
            elif heatpump_statuss == 7:
                heatpump_status = '버튼정지'
            elif heatpump_statuss == 9:
                heatpump_status = '제상운전'
            elif heatpump_statuss == 10:
                heatpump_status = '급탕운전'
            else:
                heatpump_status = '운전대기'

            heatpump_read_status = comd.read_cmd.heatpump_read_status()
            heatpump_fault_status = 'Fault' if heatpump_read_status.bits[0] else 'OK'
            heatpump_control = 'ON' if heatpump_read_status.bits[1] else 'OFF'

            heatpump_packet = [
                d_time,
                storage_inner_temp,
                storage_outer_temp,
                dhw_inner_temp,
                dhw_outer_temp,
                dhw_tank_temp,
                buffer_inner_temp,
                buffer_tank_temp,
                heatpump_mode,
                heatpump_status,
                heatpump_fault_status,
                heatpump_control
            ]
            comd.var.heatpump_read = True
            print(heatpump_packet)
        else:
            comd.var.heatpump_read = False
            storage_inner_temp = ' - '
            storage_outer_temp = ' - '
            dhw_inner_temp = ' - '
            dhw_outer_temp = ' - '
            dhw_tank_temp = ' - '
            buffer_inner_temp = ' - '
            buffer_tank_temp = ' - '
            heatpump_mode = ' - '
            heatpump_status = ' - '
            heatpump_fault_status = ' - '
            heatpump_control = ' - '
    except Exception as ex:
        comd.var.heatpump_read = False
        print('HeatPump READ Error : ', ex)

    # Get Weather Data
    try:
        global weather_trigger
        get_weather_time = time.localtime()
        get_weather_time = '%02d:%02d' % (get_weather_time.tm_min, get_weather_time.tm_sec)

        if get_weather_time == '00:00':
            weather_data = comd.openweather.get_weather()
            db.pg_connect.weather_insert(weather_data)

    except Exception as ex:
        print('Weather Read Error : ', ex)

    # # Control TEMS
    # try:
    #     control_time = time.localtime()
    #     control_time = '%02d:%02d' %(control_time.tm_hour, control_time.tm_min)
    #
    #     start_time = comd.var.schedule_start
    #     end_time = comd.var.schedule_end
    #     schedule_check = comd.var.schedule_checking

        # if comd.var.heatpump_connect_status and comd.var.bipvt_connect_status:
        #     if comd.var.auto_mode:
        #         print('auto')
        #         auto_drive(insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp, heatpump_out_temp, heatpump_modes, storage_temp, dhw_temp)
        #
        #     elif comd.var.reserve_mode:
        #         for i in range(4):
        #             if (start_time[i] <= control_time <= end_time[i]) and schedule_check[i] is True:
        #                 print('Reserve Now')
        #                 # auto_drive(insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp, heatpump_out_temp, heatpump_modes, storage_temp, dhw_temp)
        #                 comd.var.reserve_trigger = True
        #             elif start_time[i] > end_time[i] and schedule_check[i] is True:
        #                 if start_time[i] <= control_time <= '23:59' or '00:00' <= control_time <= end_time[i] and schedule_check[i] is True:
        #                     print('S>E Reserve Now')
        #                     auto_drive(insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp, heatpump_out_temp, heatpump_modes, storage_temp, dhw_temp)
        #                     comd.var.reserve_trigger = True
        #                 else:
        #                     if comd.var.reserve_trigger:
        #                         print('reserve Stop')
        #                         comd.read_cmd.stop_mode()
        #                     else:
        #                         print('reserve Waiting...')
        #             else:
        #                 if not comd.var.reserve_trigger:
        #                     print('reserve Waiting...')
        #
        #                 if comd.var.reserve_trigger:
        #                     print('reserve Stop')
        #                     comd.read_cmd.stop_mode()
    #         elif comd.var.manual_mode:
    #             print('manual')
    #         else:
    #             print('stop Mode')
    #
    # except Exception as ex:
    #     # print('TEMS Control ERROR >> ', ex)
    #     pass

    try:
        if comd.var.bipvt_read:
            header_data = db.pg_connect.total_power_select()
            pv_today = pv_power_total - header_data[1]
            load_today = load_power_total - (header_data[2] + header_data[3] + header_data[4] + header_data[5] + header_data[6])

            comd.control_ui.set_header_data(pv_today, pv_power_total, load_today, load_power_total)
    except Exception as ex:
        print('set_header_ui Error >> ', ex)

    try:
        if comd.var.bipvt_read:
            comd.control_ui.set_bipvt_data(insolation, bipvt_inner_temp, bipvt_outer_temp, outer_temp, outer_humi, wind_speed, bipvt_inside_temp1, bipvt_inside_temp2, bipvt_inside_temp3, inside_temp, inside_humi,
                                       damper_status1, fan_status, exchanger_status, pv_power, storage_power, buffer_power, heatpump_power, dhw_power)
    except Exception as ex:
        print('set_bipvt_ui Error >> ', ex)

    try:
        if comd.var.heatpump_read:
            comd.control_ui.set_heatpump_data(storage_inner_temp, storage_outer_temp, dhw_inner_temp, dhw_outer_temp, dhw_tank_temp, buffer_inner_temp, buffer_tank_temp, heatpump_mode, heatpump_status, heatpump_fault_status, heatpump_control)
    except Exception as ex:
        print('set_heatpump_ui Error >> ', ex)

    try:
        if comd.var.bipvt_read:
            comd.control_ui.control_activity_data(inside_temp)
    except Exception as ex:
        print('set_control_activity_data Error >> ', ex)

    try:
        comd.control_ui.set_control_mode()
    except Exception as ex:
        print('set_control_ui Error >> ', ex)

    try:
        comd.control_ui.set_heatpump_mode(heatpump_mode)
    except Exception as ex:
        print('set_heatpump-mode_ui Error >> ', ex)

    try:
        comd.control_ui.setheatpump_control(heatpump_control)
    except Exception as ex:
        print('set_heatpump_control_ui Error >> ', ex)
    #
    # # try:
    # #     comd.control_ui.set_manual_mode(damper_status, fan_status, exchanger_status, buffer_status, doublecoil_status, dhw_status, storage_status, heatpump_status, heatpump_modes)
    # # except Exception as ex:
    # #     print('set_manual_mode_ui Error >> ', ex)
    #
    # try:
    #     comd.control_ui.set_line_ui(damper_status, fan_status, exchanger_status, buffer_status, doublecoil_status, dhw_status, storage_status, heatpump_status, heatpump_modes)
    # except Exception as ex:
    #     print('set_line_ui Error >> ', ex)

    try:
        global bipvt_before_time
        if comd.var.bipvt_connect_status and comd.var.bipvt_read:
            if (bipvt_packet[0] != bipvt_before_time) and (bipvt_packet[2] != 0 and bipvt_packet[3] != 0):
                db.pg_connect.data_insert(bipvt_packet)
                try:
                    db.pg_connect.heatpump_insert(heatpump_packet)
                except:
                    print('heatpump insert ERR')
                bipvt_before_time = bipvt_packet[0]
            else:
                pass
    except Exception as ex:
        print('DB insert ERROR >> ', ex)

    # Update Weather Data
    try:
        weather_select = db.pg_connect.weather_select()
        comd.control_ui.set_weather_ui(weather_select)

    except Exception as ex:
        print('Weather Select Error : ', ex)


def auto_drive(insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp, heatpump_out_temp, heatpump_modes, storage_temp, dhw_temp):
    if float(insolation) >= float(comd.var.insolation_value):
        comd.read_cmd.fan_on()
    else:
        comd.read_cmd.fan_off()

    if float(bipvt_inner_temp) >= float(comd.var.inner_temp_value):
        comd.read_cmd.damper_on()
    else:
        comd.read_cmd.damper_off()

    if float(bipvt_outer_temp) >= float(buffer_tank_temp) and comd.var.fan_state:
        comd.read_cmd.exchanger_on()
        comd.read_cmd.buffer_on()
    else:
        comd.read_cmd.exchanger_off()
        comd.read_cmd.buffer_off()

    # 냉방모드
    if heatpump_modes == 0:
        comd.read_cmd.storage_on()
        comd.read_cmd.dhw_off()
        comd.var.hot_mode = False
        if float(storage_temp) <= float(comd.var.cool_value):
            comd.read_cmd.heatpump_off()
        else:
            comd.read_cmd.heatpump_on()

    # 난방모드
    if heatpump_modes == 1:
        comd.read_cmd.storage_on()
        comd.read_cmd.dhw_off()
        comd.var.hot_mode = True
        if float(storage_temp) >= float(comd.var.hot_value):
            comd.read_cmd.heatpump_off()
        else:
            comd.read_cmd.heatpump_on()

    # 급탕모드
    if heatpump_modes == 2:
        comd.read_cmd.dhw_on()
        comd.read_cmd.storage_off()
        comd.var.hot_mode = False
        if float(dhw_temp) >= float(comd.var.dhw_value):
            comd.read_cmd.heatpump_off()
        else:
            comd.read_cmd.heatpump_on()