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


def set_bipvt_data(pv_power, pv_voltage, pv_current, insolation, bipvt_inner_temp, bipvt_outer_temp,
                   buffer_tank_temp, bipvt_fault, damper_status, fan_status, exchanger_status, buffer_status):
    ui.main_Activity.main_Activity.bipvt_insolation_value.config(text=insolation)
    ui.main_Activity.main_Activity.bipvt_temp_value.config(text=bipvt_inner_temp)
    ui.main_Activity.main_Activity.bipvt_power_value.config(text=pv_power)
    ui.main_Activity.main_Activity.bipvt_voltage_value.config(text=pv_voltage)
    ui.main_Activity.main_Activity.bipvt_current_value.config(text=pv_current)
    # ui.main_Activity.main_Activity.bipvt_inner_temp_value.config(text=bipvt_inner_temp+'℃')
    # ui.main_Activity.main_Activity.bipvt_outer_temp_value.config(text=bipvt_outer_temp+'℃')
    ui.main_Activity.main_Activity.fan_status_value.config(text=fan_status)
    ui.main_Activity.main_Activity.damper_status_value.config(text=damper_status)
    # ui.main_Activity.main_Activity.out_temp_value.config(text=bipvt_out_temp)
    ui.main_Activity.main_Activity.exchanger_status_value.config(text=exchanger_status)
    ui.main_Activity.main_Activity.buffer_status_value.config(text=buffer_status)
    ui.main_Activity.main_Activity.buffer_temp_value.config(text=buffer_tank_temp+'℃')


def set_heatpump_data(heatpump_power, dhw_temp, heatpump_out_temp, storage_temp, heatpump_status,
                heatpump_mode, heatpump_fault, doublecoil_status, dhw_status, storage_status):
    ui.main_Activity.main_Activity.dhw_status_value.config(text=dhw_status)
    ui.main_Activity.main_Activity.dhw_temp_value.config(text=dhw_temp+'℃')
    ui.main_Activity.main_Activity.heatpump_status_value.config(text=heatpump_status)
    ui.main_Activity.main_Activity.heatpump_activepower_value.config(text=heatpump_power+'kW')
    ui.main_Activity.main_Activity.heatpump_mode_value.config(text=heatpump_mode)
    ui.main_Activity.main_Activity.storage_status_value.config(text=storage_status)
    ui.main_Activity.main_Activity.storage_temp_value.config(text=storage_temp+'℃')
    ui.main_Activity.main_Activity.doublecoil_status_value.config(text=doublecoil_status)
    ui.main_Activity.main_Activity.out_temp_value.config(text=heatpump_out_temp+'℃')


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
        img = Image.open('images/weather/01d.png')
    elif '02' in weather_select[3]:
        img = Image.open('images/weather/02d.png')
    elif '03' in weather_select[3]:
        img = Image.open('images/weather/03d.png')
    elif '04' in weather_select[3]:
        img = Image.open('images/weather/04d.png')
    elif '09' in weather_select[3]:
        img = Image.open('images/weather/09d.png')
    elif '10' in weather_select[3]:
        img = Image.open('images/weather/10d.png')
    elif '11' in weather_select[3]:
        img = Image.open('images/weather/11d.png')
    elif '13' in weather_select[3]:
        img = Image.open('images/weather/13d.png')
    elif '50' in weather_select[3]:
        img = Image.open('images/weather/50d.png')
    else:
        img = Image.open('images/weather/01d.png')

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
