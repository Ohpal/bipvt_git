import os, sys
import tkinter as tk

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

import ui.main_Activity
import ui.control_Activity
import ui.detail_Activity
import ui.setting_Activity

import comd.var
import datetime

from PIL import Image, ImageTk

img = ''

def now_time():
    now = datetime.datetime.now()
    getDay = now.today().weekday()
    now = now.now()
    return now, getDay


def main_timer():
    timer, getDay = now_time()
    ampm = timer.strftime('%p').upper()
    ampm = '오전' if ampm == 'AM' else '오후'
    timer = timer.strftime("%Y-%m-%d %I:%M:%S")

    weekDay = '-'
    if getDay == 0:
        weekDay = '월'
    elif getDay == 1:
        weekDay = '화'
    elif getDay == 2:
        weekDay = '수'
    elif getDay == 3:
        weekDay = '목'
    elif getDay == 4:
        weekDay = '금'
    elif getDay == 5:
        weekDay = '토'
    elif getDay == 6:
        weekDay = '일'

    timer = timer.split(' ')

    ui.main_Activity.main_Activity.time_label1.config(text='{} [{}]'.format(timer[0], weekDay))
    ui.main_Activity.main_Activity.time_label2.config(text='{} {}'.format(ampm, timer[1]))
    ui.detail_Activity.detail_Activity.time_label1.config(text='{} [{}]'.format(timer[0], weekDay))
    ui.detail_Activity.detail_Activity.time_label2.config(text='{} {}'.format(ampm, timer[1]))
    ui.setting_Activity.setting_Activity.time_label1.config(text='{} [{}]'.format(timer[0], weekDay))
    ui.setting_Activity.setting_Activity.time_label2.config(text='{} {}'.format(ampm, timer[1]))
    ui.control_Activity.control_Activity.time_label1.config(text='{} [{}]'.format(timer[0], weekDay))
    ui.control_Activity.control_Activity.time_label2.config(text='{} {}'.format(ampm, timer[1]))


def set_header_data(pv_power, pv_power_total, load_power, load_power_total):
    ui.main_Activity.main_Activity.above1_value.config(text='{:,}'.format(pv_power))
    ui.main_Activity.main_Activity.above2_value.config(text='{:,}'.format(pv_power_total))
    ui.main_Activity.main_Activity.above3_value.config(text='{:,}'.format(load_power))
    ui.main_Activity.main_Activity.above4_value.config(text='{:,}'.format(load_power_total))

    ui.control_Activity.control_Activity.above1_value.config(text='{:,}'.format(pv_power))
    ui.control_Activity.control_Activity.above2_value.config(text='{:,}'.format(pv_power_total))
    ui.control_Activity.control_Activity.above3_value.config(text='{:,}'.format(load_power))
    ui.control_Activity.control_Activity.above4_value.config(text='{:,}'.format(load_power_total))

    ui.detail_Activity.detail_Activity.above1_value.config(text='{:,}'.format(pv_power))
    ui.detail_Activity.detail_Activity.above2_value.config(text='{:,}'.format(pv_power_total))
    ui.detail_Activity.detail_Activity.above3_value.config(text='{:,}'.format(load_power))
    ui.detail_Activity.detail_Activity.above4_value.config(text='{:,}'.format(load_power_total))

    ui.setting_Activity.setting_Activity.above1_value.config(text='{:,}'.format(pv_power))
    ui.setting_Activity.setting_Activity.above2_value.config(text='{:,}'.format(pv_power_total))
    ui.setting_Activity.setting_Activity.above3_value.config(text='{:,}'.format(load_power))
    ui.setting_Activity.setting_Activity.above4_value.config(text='{:,}'.format(load_power_total))


def set_bipvt_data(insolation, bipvt_inner_temp, bipvt_outer_temp, outer_temp, outer_humi, wind_speed, bipvt_inside_temp1, bipvt_inside_temp2, bipvt_inside_temp3,  inside_temp, inside_humi,
                                       damper_status, fan_status, exchanger_status, pv_power, storage_power, buffer_power, heatpump_power, dhw_power):
    ui.main_Activity.main_Activity.bipvt_insolation_value.config(text=insolation)
    ui.main_Activity.main_Activity.bipvt_inside_temp_value.config(text=str(round(float(bipvt_inside_temp1+bipvt_inside_temp2+bipvt_inside_temp3)/3, 1)))
    # ui.main_Activity.main_Activity.bipvt_inside_temp_value2.config(text=str(bipvt_inside_temp2) + ' | \n')
    # ui.main_Activity.main_Activity.bipvt_inside_temp_value3.config(text=bipvt_inside_temp3)
    # ui.main_Activity.main_Activity.bipvt_inner_temp_value.config(text=bipvt_inner_temp+'℃')
    # ui.main_Activity.main_Activity.bipvt_outer_temp_value.config(text=bipvt_outer_temp+'℃')
    ui.main_Activity.main_Activity.fcu_temp_value.config(text=str(inside_temp) + ' ℃')
    ui.main_Activity.main_Activity.fcu_humi_value.config(text=str(inside_humi) + ' %')
    ui.main_Activity.main_Activity.fan_status_value.config(text=fan_status)
    ui.main_Activity.main_Activity.damper_status_value.config(text=damper_status)
    ui.main_Activity.main_Activity.exchanger_status_value.config(text=exchanger_status)
    # ui.main_Activity.main_Activity.buffer_status_value.config(text=buffer_status)
    ui.main_Activity.main_Activity.out_temp_value.config(text=str(outer_temp) + ' ℃')
    ui.main_Activity.main_Activity.out_humi_value.config(text=str(outer_humi) + ' %')
    ui.main_Activity.main_Activity.wind_speed_value.config(text=str(wind_speed) + 'm/s')
    ui.main_Activity.main_Activity.bipvt_power_value.config(text='{:,}'.format(pv_power))
    ui.main_Activity.main_Activity.storage_power_value.config(text=str(storage_power) + ' W')
    ui.main_Activity.main_Activity.heatpump_activepower_value.config(text=str(heatpump_power) + ' W')
    ui.main_Activity.main_Activity.buffer_power_value.config(text=str(buffer_power) + ' W')
    ui.main_Activity.main_Activity.dhw_power_value.config(text=str(dhw_power) + ' W')


def set_heatpump_data(storage_inner_temp, storage_outer_temp, dhw_inner_temp, dhw_outer_temp, dhw_tank_temp, buffer_inner_temp, buffer_tank_temp, heatpump_mode, heatpump_status, heatpump_fault_status, heatpump_control):
    ui.main_Activity.main_Activity.buffer_temp_value.config(text=str(round(buffer_tank_temp, 1))+' ℃')
    ui.main_Activity.main_Activity.buffer_inner_temp_value.config(text=str(round(buffer_inner_temp, 1))+' ℃')
    ui.main_Activity.main_Activity.dhw_temp_value.config(text=str(round(dhw_tank_temp, 1))+' ℃')
    ui.main_Activity.main_Activity.dhw_inner_temp_value.config(text=str(round(dhw_inner_temp, 1))+' ℃')
    ui.main_Activity.main_Activity.dhw_outer_temp_value.config(text=str(round(dhw_outer_temp, 1))+' ℃')
    ui.main_Activity.main_Activity.storage_temp_value.config(text=str(round(storage_inner_temp, 1))+' ℃')
    ui.main_Activity.main_Activity.storage_outer_temp_value.config(text=str(round(storage_outer_temp, 1))+' ℃')

    ui.main_Activity.main_Activity.heatpump_mode_value.config(text=heatpump_mode)
    ui.main_Activity.main_Activity.heatpump_status_value.config(text=heatpump_status)

    if heatpump_status == '운전중' or heatpump_status == '제상운전' or heatpump_status == '급탕운전':
        ui.main_Activity.main_Activity.doublecoil_status_value.config(text='ON')
    else:
        ui.main_Activity.main_Activity.doublecoil_status_value.config(text='OFF')
    # ui.main_Activity.main_Activity.dhw_status_value.config(text=dhw_status)
    # ui.main_Activity.main_Activity.dhw_temp_value.config(text=dhw_temp+'℃')
    # ui.main_Activity.main_Activity.heatpump_activepower_value.config(text=heatpump_power+'kW')
    # ui.main_Activity.main_Activity.storage_status_value.config(text=storage_status)
    # ui.main_Activity.main_Activity.storage_temp_value.config(text=storage_temp+'℃')
    # ui.main_Activity.main_Activity.out_temp_value.config(text=heatpump_out_temp+'℃')


def set_control_mode():
    if comd.var.auto_mode:
        ui.control_Activity.control_Activity.auto_mode_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.reserve_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.manual_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.stop_mode_btn.config(bg='lightgray', activebackground='lightgray')
    elif comd.var.reserve_mode:
        ui.control_Activity.control_Activity.auto_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.reserve_mode_btn.config(bg='orange', activebackground='orange')
        ui.control_Activity.control_Activity.manual_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.stop_mode_btn.config(bg='lightgray', activebackground='lightgray')
    elif comd.var.manual_mode:
        ui.control_Activity.control_Activity.auto_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.reserve_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.manual_mode_btn.config(bg='#007ad1', activebackground='#007ad1')
        ui.control_Activity.control_Activity.stop_mode_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.auto_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.reserve_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.manual_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.stop_mode_btn.config(bg='red', activebackground='red')


def set_heatpump_mode(val):
    if val == 0:
        ui.control_Activity.control_Activity.cool_mode_btn.config(bg='#007ad1', activebackground='#007ad1')
        ui.control_Activity.control_Activity.heat_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.boil_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.keep_mode_btn.config(bg='lightgray', activebackground='lightgray')
    elif val == 1:
        ui.control_Activity.control_Activity.cool_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.heat_mode_btn.config(bg='red', activebackground='red')
        ui.control_Activity.control_Activity.boil_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.keep_mode_btn.config(bg='lightgray', activebackground='lightgray')
    elif val == 2:
        ui.control_Activity.control_Activity.cool_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.heat_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.boil_mode_btn.config(bg='orange', activebackground='orange')
        ui.control_Activity.control_Activity.keep_mode_btn.config(bg='lightgray', activebackground='lightgray')
    elif val == 3:
        ui.control_Activity.control_Activity.cool_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.heat_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.boil_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.keep_mode_btn.config(bg='#96c63e', activebackground='#96c63e')
    else:
        ui.control_Activity.control_Activity.cool_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.heat_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.boil_mode_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.keep_mode_btn.config(bg='lightgray', activebackground='lightgray')


def set_manual_mode(damper_status, fan_status, exchanger_status, buffer_status, doublecoil_status, dhw_status, storage_status, heatpump_status, mode):
    if damper_status == 'ON':
        ui.control_Activity.control_Activity.damper_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.damper_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.damper_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.damper_off_btn.config(bg='red', activebackground='red')

    if fan_status == 'ON':
        ui.control_Activity.control_Activity.fan_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.fan_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.fan_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.fan_off_btn.config(bg='red', activebackground='red')

    if exchanger_status == 'ON':
        ui.control_Activity.control_Activity.exchanger_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.exchanger_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.exchanger_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.exchanger_off_btn.config(bg='red', activebackground='red')

    if buffer_status == 'ON':
        ui.control_Activity.control_Activity.buffer_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.buffer_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.buffer_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.buffer_off_btn.config(bg='red', activebackground='red')

    if doublecoil_status == 'ON':
        ui.control_Activity.control_Activity.doublecoil_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.doublecoil_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.doublecoil_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.doublecoil_off_btn.config(bg='red', activebackground='red')

    # if heatpump_outair_status == 'ON':
    #     ui.control_Activity.control_Activity.heatpump_outair_on_btn.config(bg='#96c63e', activebackground='#96c63e')
    #     ui.control_Activity.control_Activity.heatpump_outair_off_btn.config(bg='lightgray', activebackground='lightgray')
    # else:
    #     ui.control_Activity.control_Activity.heatpump_outair_on_btn.config(bg='lightgray', activebackground='lightgray')
    #     ui.control_Activity.control_Activity.heatpump_outair_off_btn.config(bg='red', activebackground='red')

    if dhw_status == 'ON':
        ui.control_Activity.control_Activity.dhw_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.dhw_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.dhw_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.dhw_off_btn.config(bg='red', activebackground='red')

    if storage_status == 'ON':
        ui.control_Activity.control_Activity.storage_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.storage_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.storage_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.storage_off_btn.config(bg='red', activebackground='red')

    if heatpump_status == 'ON':
        ui.control_Activity.control_Activity.heatpump_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.heatpump_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.heatpump_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.heatpump_off_btn.config(bg='red', activebackground='red')


def set_connect_ui():
    if comd.var.bipvt_connect_status:
        ui.main_Activity.main_Activity.bipvt_connect_value.config(fg='#96c63e')
    else:
        ui.main_Activity.main_Activity.bipvt_connect_value.config(fg='red')

    if comd.var.heatpump_connect_status:
        ui.main_Activity.main_Activity.heatpump_connect_value.config(fg='#96c63e')
    else:
        ui.main_Activity.main_Activity.heatpump_connect_value.config(fg='red')

    if comd.var.auto_mode:
        ui.main_Activity.main_Activity.control_now.config(text='자동운전', fg='#96c63e')
    elif comd.var.reserve_mode:
        ui.main_Activity.main_Activity.control_now.config(text='예약운전', fg='orange')
    elif comd.var.manual_mode:
        ui.main_Activity.main_Activity.control_now.config(text='수동운전', fg='#007ad1')
    else:
        ui.main_Activity.main_Activity.control_now.config(text='정  지', fg='red')

# ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line13, fill='white')
# ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line14, fill='white')

def set_line_ui(damper_status, fan_status, exchanger_status, buffer_status, doublecoil_status, dhw_status, storage_status, heatpump_status, mode):
    if damper_status == 'ON':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line4, fill='#96c63e')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line5, fill='#96c63e')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line4, fill='white')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line5, fill='white')

    if fan_status == 'ON':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line1, fill='#96c63e')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line1, fill='white')

    if fan_status == 'ON' and exchanger_status == 'ON':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line2, fill='red')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line2, fill='white')

    if exchanger_status == 'ON' and damper_status == 'ON':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line3, fill='#96c63e')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line3, fill='white')

    # if exchanger_status == 'ON' and buffer_status == 'ON':
    #     ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line6, fill='red')
    # else:
    #     ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line6, fill='white')

    # if exchanger_status == 'OFF' and buffer_status == 'ON':
    #     ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line7, fill='#007ad1')
    # else:
    #     ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line7, fill='white')

    # if doublecoil_status == 'ON':
    #     ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line10, fill='#96c63e')
    # else:
    #     ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line10, fill='white')

    if buffer_status == 'ON':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line6, fill='red')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line7, fill='white')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line8, fill='red')
        # ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line9, fill='white')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line6, fill='white')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line7, fill='#007ad1')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line8, fill='white')
        # ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line9, fill='#007ad1')

    if dhw_status == 'ON':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line15, fill='red')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line16, fill='white')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line15, fill='white')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line16, fill='#96c63e')

    if storage_status == 'ON':
        if mode == 0:
            ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line13, fill='#007ad1')
            ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line14, fill='red')
        elif mode == 1:
            ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line13, fill='red')
            ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line14, fill='#007ad1')
        else:
            ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line13, fill='white')
            ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line14, fill='white')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line13, fill='white')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line14, fill='white')

    if heatpump_status == 'OFF':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line12, fill='#96c63e')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line11, fill='white')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line11, fill='#96c63e')
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line12, fill='white')

    if heatpump_status == 'OFF' and buffer_status == 'OFF':
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line9, fill='#96c63e')
    else:
        ui.main_Activity.main_Activity.main_canvas.itemconfig(ui.main_Activity.main_Activity.line9, fill='white')


def set_weather_ui(weather_select):
    global img

    if '01' in weather_select[3]:
        img = Image.open('images/weather/sunny.png')
    elif '02' in weather_select[3]:
        img = Image.open('images/weather/cloudy.png')
    elif '03' in weather_select[3]:
        img = Image.open('images/weather/cloudy.png')
    elif '04' in weather_select[3]:
        img = Image.open('images/weather/cloudy.png')
    elif '09' in weather_select[3]:
        img = Image.open('images/weather/downpour.png')
    elif '10' in weather_select[3]:
        img = Image.open('images/weather/downpour.png')
    elif '11' in weather_select[3]:
        img = Image.open('images/weather/thunder.png')
    elif '13' in weather_select[3]:
        img = Image.open('images/weather/snow.png')
    elif '50' in weather_select[3]:
        img = Image.open('images/weather/foggy.png')
    else:
        img = Image.open('images/weather/sunny.png')

    img = img.resize((40, 40), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    ui.main_Activity.main_Activity.weather_value.config(image=img)
    ui.detail_Activity.detail_Activity.weather_value.config(image=img)
    ui.setting_Activity.setting_Activity.weather_value.config(image=img)
    ui.control_Activity.control_Activity.weather_value.config(image=img)

    ui.main_Activity.main_Activity.temperature_value.config(text=round(weather_select[1], 1))
    ui.detail_Activity.detail_Activity.temperature_value.config(text=round(weather_select[1], 1))
    ui.setting_Activity.setting_Activity.temperature_value.config(text=round(weather_select[1], 1))
    ui.control_Activity.control_Activity.temperature_value.config(text=round(weather_select[1], 1))

    ui.main_Activity.main_Activity.humi_value.config(text=int(weather_select[2]))
    ui.detail_Activity.detail_Activity.humi_value.config(text=int(weather_select[2]))
    ui.setting_Activity.setting_Activity.humi_value.config(text=int(weather_select[2]))
    ui.control_Activity.control_Activity.humi_value.config(text=int(weather_select[2]))


def set_schedule_checking():
    on_img = Image.open('images/on-button.png')
    off_img = Image.open('images/off-button.png')
    on_img = on_img.resize((60, 60), Image.ANTIALIAS)
    off_img = off_img.resize((60, 60), Image.ANTIALIAS)
    on_image = ImageTk.PhotoImage(on_img)
    off_image = ImageTk.PhotoImage(off_img)

    if comd.var.schedule_checking[0]:
        ui.control_Activity.control_Activity.check_btn_1.config(image=on_image)
    else:
        ui.control_Activity.control_Activity.check_btn_1.config(image=off_image)
    if comd.var.schedule_checking[1]:
        ui.control_Activity.control_Activity.check_btn_2.config(image=on_image)
    else:
        ui.control_Activity.control_Activity.check_btn_2.config(image=off_image)
    if comd.var.schedule_checking[2]:
        ui.control_Activity.control_Activity.check_btn_3.config(image=on_image)
    else:
        ui.control_Activity.control_Activity.check_btn_3.config(image=off_image)
    if comd.var.schedule_checking[3]:
        ui.control_Activity.control_Activity.check_btn_4.config(image=on_image)
    else:
        ui.control_Activity.control_Activity.check_btn_4.config(image=off_image)
    if comd.var.schedule_checking[4]:
        ui.control_Activity.control_Activity.check_btn_5.config(image=on_image)
    else:
        ui.control_Activity.control_Activity.check_btn_5.config(image=off_image)
    if comd.var.schedule_checking[5]:
        ui.control_Activity.control_Activity.check_btn_6.config(image=on_image)
    else:
        ui.control_Activity.control_Activity.check_btn_6.config(image=off_image)
    if comd.var.schedule_checking[6]:
        ui.control_Activity.control_Activity.check_btn_7.config(image=on_image)
    else:
        ui.control_Activity.control_Activity.check_btn_7.config(image=off_image)


def control_activity_data(inside_temp):
    ui.control_Activity.control_Activity.fcu_nowTemp.config(text=round(inside_temp, 1))

def setheatpump_control(heatpump_control):
    if heatpump_control == 'ON':
        ui.control_Activity.control_Activity.heatpump_on_btn.config(bg='#96c63e', activebackground='#96c63e')
        ui.control_Activity.control_Activity.heatpump_off_btn.config(bg='lightgray', activebackground='lightgray')
    else:
        ui.control_Activity.control_Activity.heatpump_on_btn.config(bg='lightgray', activebackground='lightgray')
        ui.control_Activity.control_Activity.heatpump_off_btn.config(bg='red', activebackground='red')
