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

before_time = ''

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
            bipvt_datas = comd.read_cmd.bipvt_read_data()

            pv_power = bipvt_datas.getRegister(0) * 0.1
            pv_voltage = bipvt_datas.getRegister(1) * 0.1
            pv_current = bipvt_datas.getRegister(2) * 0.1
            insolation = bipvt_datas.getRegister(3)
            bipvt_inner_temp = bipvt_datas.getRegister(4)
            bipvt_outer_temp = bipvt_datas.getRegister(5)
            buffer_tank_temp = bipvt_datas.getRegister(6)
            bipvt_fault = bipvt_datas.getRegister(7)

            bipvt_inner_temp = (((0 - (bipvt_inner_temp ^ 0xffff)) - 1) * 0.1) if bipvt_inner_temp > 32768 else bipvt_inner_temp * 0.1
            bipvt_outer_temp = (((0 - (bipvt_outer_temp ^ 0xffff)) - 1) * 0.1) if bipvt_outer_temp > 32768 else bipvt_outer_temp * 0.1
            buffer_tank_temp = (((0 - (buffer_tank_temp ^ 0xffff)) - 1) * 0.1) if buffer_tank_temp > 32768 else buffer_tank_temp * 0.1

            bipvt_status = comd.read_cmd.bipvt_read_status()
            damper_status = 'ON' if bipvt_status.bits[0] else 'OFF'
            fan_status = 'ON' if bipvt_status.bits[1] else 'OFF'
            exchanger_status = 'ON' if bipvt_status.bits[2] else 'OFF'
            buffer_status = 'ON' if bipvt_status.bits[3] else 'OFF'

            pv_power = '{0:0.1f}'.format(pv_power)
            pv_voltage = '{0:0.1f}'.format(pv_voltage)
            pv_current = '{0:0.1f}'.format(pv_current)
            insolation = '{0:0.1f}'.format(insolation)
            bipvt_inner_temp = '{0:0.1f}'.format(bipvt_inner_temp)
            bipvt_outer_temp = '{0:0.1f}'.format(bipvt_outer_temp)
            buffer_tank_temp = '{0:0.1f}'.format(buffer_tank_temp)


            # 태양광 전력 0~1000 사이 측정
            if not 0 <= float(pv_power) <= 1000:
                db.sqlite_connect.error_insert('태양광전력', '데이터 측정범위 에러@'+pv_power, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '태양광전력', '데이터 측정범위 에러@'+pv_power))
                raise Exception('Out of Range 전력 >> ', pv_power)

            # 태양광 전압 0~1000 사이 측정
            if not 0 <= float(pv_voltage) <= 1000:
                db.sqlite_connect.error_insert('태양광전압', '데이터 측정범위 에러@'+pv_voltage, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '태양광전압', '데이터 측정범위 에러@'+pv_voltage))
                raise Exception('Out of Range 전압 >> ', pv_voltage)

            # 태양광 전류 0~1000 사이 측정
            if not 0 <= float(pv_current) <= 1000:
                db.sqlite_connect.error_insert('태양광전류', '데이터 측정범위 에러@'+pv_current, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '태양광전류', '데이터 측정범위 에러@'+pv_current))
                raise Exception('Out of Range 전류 >> ', pv_current)

            # 일사량 0~9999 사이 측정
            if not 0 <= float(insolation) <= 9999:
                db.sqlite_connect.error_insert('조도', '데이터 측정범위 에러@'+insolation, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '조도', '데이터 측정범위 에러@'+insolation))
                raise Exception('Out of Range 조도 >> ', pv_current)

            # BIPVT 입구온도 -200~200 사이 측정
            if not - 200 <= float(bipvt_inner_temp) <= 200:
                db.sqlite_connect.error_insert('BIPVT 입구온도', '데이터 측정범위 에러@'+bipvt_inner_temp, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), 'BIPVT 입구온도', '데이터 측정범위 에러@'+bipvt_inner_temp))
                raise Exception('Out of Range 입구온도 >> ', bipvt_inner_temp)

            # BIPVT 출구온도 -200~200 사이 측정
            if not - 200 <= float(bipvt_outer_temp) <= 200:
                db.sqlite_connect.error_insert('BIPVT 출구온도', '데이터 측정범위 에러@'+bipvt_outer_temp, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), 'BIPVT 출구온도', '데이터 측정범위 에러@'+bipvt_outer_temp))
                raise Exception('Out of Range 출구온도 ', bipvt_outer_temp)

            # 버퍼탱크 온도 -200~200 사이 측정
            if not - 200 <= float(buffer_tank_temp) <= 200:
                db.sqlite_connect.error_insert('버퍼탱크 온도', '데이터 측정범위 에러@'+buffer_tank_temp, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '버퍼탱크 온도', '데이터 측정범위 에러@'+buffer_tank_temp))
                raise Exception('Out of Range 버퍼탱크온도 ', buffer_tank_temp)

            packet = [
                'PVT',
                d_time,
                pv_power,
                pv_voltage,
                pv_current,
                insolation,
                bipvt_inner_temp,
                bipvt_outer_temp,
                buffer_tank_temp,
                bipvt_fault,
                damper_status,
                fan_status,
                exchanger_status,
                buffer_status
            ]

            comd.var.bipvt_read = True

            print(packet)
        else:
            comd.var.bipvt_read = True
            pv_power = ' - '
            pv_voltage = ' - '
            pv_current = ' - '
            insolation = ' - '
            bipvt_inner_temp = ' - '
            bipvt_outer_temp = ' - '
            buffer_tank_temp = ' - '
            bipvt_fault = ' - '
            damper_status = ' - '
            fan_status = ' - '
            exchanger_status = ' - '
            buffer_status = ' - '

    except Exception as ex:
        comd.var.bipvt_read = False
        print('BIPVT READ Error : ', ex)

    try:
        if comd.var.heatpump_connect_status:
            heatpump_read_datas = comd.read_cmd.heatpump_read_data()
            heatpump_power = heatpump_read_datas.getRegister(0) * 0.1
            dhw_temp = heatpump_read_datas.getRegister(1)
            heatpump_out_temp = heatpump_read_datas.getRegister(2)
            storage_temp = heatpump_read_datas.getRegister(3)
            heatpump_status = heatpump_read_datas.getRegister(4)
            heatpump_modes = heatpump_read_datas.getRegister(5)
            heatpump_fault = heatpump_read_datas.getRegister(6)

            dhw_temp = (((0 - (dhw_temp ^ 0xffff)) - 1) * 0.1) if dhw_temp > 32768 else dhw_temp * 0.1
            heatpump_out_temp = (((0 - (heatpump_out_temp ^ 0xffff)) - 1) * 0.1) if heatpump_out_temp > 32768 else heatpump_out_temp * 0.1
            storage_temp = (((0 - (storage_temp ^ 0xffff)) - 1) * 0.1) if storage_temp > 32768 else storage_temp * 0.1

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

            heatpump_read_status = comd.read_cmd.heatpump_read_status()
            doublecoil_status = 'ON' if heatpump_read_status.bits[0] else 'OFF'
            heatpump_status = 'ON' if heatpump_read_status.bits[1] else 'OFF'
            dhw_status = 'ON' if heatpump_read_status.bits[2] else 'OFF'
            storage_status = 'ON' if heatpump_read_status.bits[3] else 'OFF'

            heatpump_power = '{0:0.1f}'.format(heatpump_power)
            dhw_temp = '{0:0.1f}'.format(dhw_temp)
            heatpump_out_temp = '{0:0.1f}'.format(heatpump_out_temp)
            storage_temp = '{0:0.1f}'.format(storage_temp)

            if not 0 <= float(heatpump_power) <= 1000:
                db.sqlite_connect.error_insert('히트펌프 전력사용량', '데이터 측정범위 에러@'+heatpump_power, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '히트펌프 전력사용량', '데이터 측정범위 에러@'+heatpump_power))
                raise Exception('Out of Range >> ', heatpump_power)

            if not -200 <= float(dhw_temp) <= 200:
                db.sqlite_connect.error_insert('온수탱크 온도', '데이터 측정범위 에러@'+dhw_temp, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '온수탱크 온도', '데이터 측정범위 에러@'+dhw_temp))
                raise Exception('Out of Range >> ', dhw_temp)

            if not -200 <= float(heatpump_out_temp) <= 200:
                db.sqlite_connect.error_insert('외기온도', '데이터 측정범위 에러@'+heatpump_out_temp, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '외기온도', '데이터 측정범위 에러@'+heatpump_out_temp))
                raise Exception('Out of Range >> ', heatpump_out_temp)

            if not -200 <= float(storage_temp) <= 200:
                db.sqlite_connect.error_insert('저장탱크 온도', '데이터 측정범위 에러@'+storage_temp, now_time())
                ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                   values=(now_time(), '저장탱크 온도', '데이터 측정범위 에러@'+storage_temp))
                raise Exception('Out of Range >> ', storage_temp)

            heatpump_packet = [
                'HeatPump',
                d_time,
                heatpump_power,
                dhw_temp,
                heatpump_out_temp,
                storage_temp,
                heatpump_status,
                heatpump_mode,
                heatpump_fault,
                doublecoil_status,
                dhw_status,
                storage_status
            ]

            comd.var.heatpump_read = True

            print(heatpump_packet)

        else:
            comd.var.heatpump_read = True
            heatpump_power = ' - '
            dhw_temp = ' - '
            heatpump_out_temp = ' - '
            storage_temp = ' - '
            heatpump_status = ' - '
            heatpump_mode = ' - '
            heatpump_modes = ' - '
            heatpump_fault = ' - '
            doublecoil_status = ' - '
            dhw_status = ' - '
            storage_status = ' - '
    except Exception as ex:
        comd.var.heatpump_read = False
        print('HeatPump READ Error : ', ex)

    # Get Weather Data
    try:
        get_weather_time = time.localtime()
        get_weather_time = '%02d:%02d' %(get_weather_time.tm_min, get_weather_time.tm_sec)

        if get_weather_time == '00:00':
            weather_data = comd.openweather.get_weather()
            db.pg_connect.weather_insert(weather_data)

    except Exception as ex:
        print('Weather Read Error : ', ex)

    # Control TEMS
    try:
        control_time = time.localtime()
        control_time = '%02d:%02d' %(control_time.tm_hour, control_time.tm_min)

        start_time = '%s:%s' %(comd.var.start_hour, comd.var.start_min)
        end_time = '%s:%s' %(comd.var.end_hour, comd.var.end_min)
        if comd.var.heatpump_connect_status and comd.var.bipvt_connect_status:

            if comd.var.auto_mode:
                print('auto')
                auto_drive(insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp, heatpump_out_temp, heatpump_modes, storage_temp, dhw_temp)

            elif comd.var.reserve_mode:
                if start_time <= control_time <= end_time:
                    print('Reserve Now')
                    auto_drive(insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp, heatpump_out_temp, heatpump_modes, storage_temp, dhw_temp)
                    comd.var.reserve_trigger = True
                elif start_time > end_time:
                    if start_time <= control_time <= '23:59' or '00:00' <= control_time <= end_time:
                        print('S>E Reserve Now')
                        auto_drive(insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp, heatpump_out_temp, heatpump_modes, storage_temp, dhw_temp)
                        comd.var.reserve_trigger = True
                    else:
                        if comd.var.reserve_trigger:
                            print('reserve Stop')
                            comd.read_cmd.stop_mode()
                        else:
                            print('reserve Waiting...')
                else:
                    if not comd.var.reserve_trigger:
                        print('reserve Waiting...')

                    if comd.var.reserve_trigger:
                        print('reserve Stop')
                        comd.read_cmd.stop_mode()
            elif comd.var.manual_mode:
                print('manual')
            else:
                print('stop Mode')

    except Exception as ex:
        print('TEMS Control ERROR >> ', ex)

    try:
        if comd.var.bipvt_read:
            comd.control_ui.set_bipvt_data(pv_power, pv_voltage, pv_current, insolation, bipvt_inner_temp, bipvt_outer_temp,
                                       buffer_tank_temp, bipvt_fault, damper_status, fan_status, exchanger_status, buffer_status)
    except Exception as ex:
        print('set_bipvt_ui Error >> ', ex)

    try:
        if comd.var.heatpump_read:
            comd.control_ui.set_heatpump_data(heatpump_power, dhw_temp, heatpump_out_temp, storage_temp,
                                          heatpump_status, heatpump_mode, heatpump_fault, doublecoil_status,
                                          dhw_status, storage_status)
    except Exception as ex:
        print('set_heatpump_ui Error >> ', ex)

    try:
        comd.control_ui.set_control_mode()
    except Exception as ex:
        print('set_control_ui Error >> ', ex)

    try:
        comd.control_ui.set_heatpump_mode(heatpump_modes)
    except Exception as ex:
        print('set_heatpump-mode_ui Error >> ', ex)

    try:
        comd.control_ui.set_manual_mode(damper_status, fan_status, exchanger_status, buffer_status, doublecoil_status, dhw_status, storage_status, heatpump_status, heatpump_modes)
    except Exception as ex:
        print('set_manual_mode_ui Error >> ', ex)

    try:
        comd.control_ui.set_line_ui(damper_status, fan_status, exchanger_status, buffer_status, doublecoil_status, dhw_status, storage_status, heatpump_status, heatpump_modes)
    except Exception as ex:
        print('set_line_ui Error >> ', ex)

    try:
        global before_time
        if comd.var.heatpump_connect_status and comd.var.bipvt_connect_status and comd.var.bipvt_read and comd.var.heatpump_read:

            packet = [
                d_time, pv_power, pv_voltage, pv_current, insolation, bipvt_inner_temp, bipvt_outer_temp, buffer_tank_temp,
                damper_status, fan_status, exchanger_status, buffer_status, heatpump_power, dhw_temp,
                heatpump_out_temp, storage_temp, heatpump_mode, doublecoil_status,
                dhw_status, storage_status
            ]

            if packet[0] != before_time:
                db.pg_connect.data_insert(packet)
                before_time = packet[0]
            else:
                pass

    except Exception as ex:
        print('DB insert ERROR >> ', ex)


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


    # 제상모드에 안갔을경우
    if not comd.var.keep_mode:
        if float(heatpump_out_temp) <= float(comd.var.doublecoil_value) and comd.var.hot_time >= 3000:
            comd.read_cmd.doublecoil_on()
            comd.read_cmd.mode_control(3)
            comd.var.keep_mode = True
            comd.var.hot_time = 3000
    # 제상모드가 실행될경우
    else:
        # 제상모드 10분 유지
        if comd.var.hot_time >= 3600:
            comd.read_cmd.mode_control(1)
            comd.var.hot_time = 0
            comd.read_cmd.doublecoil_off()
            comd.var.keep_mode = False

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