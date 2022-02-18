import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
from time import sleep
import notification.insert_keypad

import comd.var

# Graph Library
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random


class main_Activity(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 상단 메뉴바
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, ipady=20)

        self.logo_image = tk.PhotoImage(file="images/bonc.png")
        logo_label = Label(menu_frame, image=self.logo_image, highlightbackground="#111111", activebackground='#111111', bd=0, bg='#111111')
        logo_label.pack(side=LEFT, padx=20)

        # left frame
        left_frame = Frame(self, bg='#111111')
        left_frame.pack(fill=Y, side=LEFT, ipadx=15)

        self.main_image = tk.PhotoImage(file='images/main_btn.gif')
        self.control_image = tk.PhotoImage(file='images/control_btn_off.gif')
        self.setting_image = tk.PhotoImage(file='images/setting_btn_off.gif')

        main_menu = Button(left_frame, image=self.main_image, highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', command=lambda: controller.show_frame('main_Activity'))
        main_menu.pack(pady=(40, 20))

        control_menu = Button(left_frame, image=self.control_image, highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', command=lambda: controller.show_frame('control_Activity'))
        control_menu.pack(pady=20)

        detail_menu = Button(left_frame, image=self.main_image, highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', command=lambda: controller.show_frame('control_Activity'))
        detail_menu.pack(pady=20)

        setting_menu = Button(left_frame, image=self.setting_image, highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', command=lambda: controller.show_frame('setting_Activity'))
        setting_menu.pack(pady=20)

        self.gps_image = tk.PhotoImage(file='images/gps.png')
        gps_menu = Label(left_frame, image=self.gps_image, highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111')
        gps_menu.pack(pady=(950, 15))

        weather_frame = Frame(left_frame, bg='#111111')
        weather_frame.pack(pady=(0, 10))

        weather_menu = Label(weather_frame, text='날 씨', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 16, 'bold'), fg='white')
        weather_menu.pack(side=LEFT, padx=(0, 10))

        main_Activity.weather_label = Label(weather_frame, text='맑 음', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 16), fg='white')
        main_Activity.weather_label.pack(side=LEFT)

        temperature_frame = Frame(left_frame, bg='#111111')
        temperature_frame.pack()

        temperature_menu = Label(temperature_frame, text='기 온', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 16, 'bold'), fg='white')
        temperature_menu.pack(side=LEFT, padx=(0, 10))

        main_Activity.temperature_label = Label(temperature_frame, text='32', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 16), fg='white')
        main_Activity.temperature_label.pack(side=LEFT)

        temperature_unit = Label(temperature_frame, text=' ℃', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 16, 'bold'), fg='white')
        temperature_unit.pack(side=LEFT)

        main_Activity.time_label1 = Label(left_frame, text='-', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 16, 'bold'), fg='white')
        main_Activity.time_label1.pack(pady=(150, 10))

        main_Activity.time_label2 = Label(left_frame, text='-', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 16, 'bold'), fg='#96c63e')
        main_Activity.time_label2.pack()

        # center top frame
        center_frame = Frame(self, bg='#2f323b')
        center_frame.pack(fill=BOTH, side=TOP, expand=True)

        # 라인선 그리기
        main_Activity.liner = Canvas(center_frame, bg='#2f323b', highlightbackground='#2f323b', width=1280, height=670)
        main_Activity.liner.pack()

        # 설비 연결선 라벨
        main_Activity.line1 = main_Activity.liner.create_line(235, 219, 368, 138, fill='white', width=5, arrow=LAST)    # PVT-팬
        main_Activity.line2 = main_Activity.liner.create_line(393, 180, 307, 232, 392, 296, fill='white', width=5, arrow=LAST)  # 팬-열교환기
        main_Activity.line3 = main_Activity.liner.create_line(368, 398, 241, 473, fill='white', width=5, arrow=LAST)    # 열교환기-댐퍼
        main_Activity.line4 = main_Activity.liner.create_line(293, 542, 233, 500, fill='#96c63e', width=5, arrow=LAST)    # 외기-댐퍼
        main_Activity.line5 = main_Activity.liner.create_line(136, 429, 18, 348, 148, 272, fill='white', width=5, arrow=LAST)   # 댐퍼-PVT
        main_Activity.line6 = main_Activity.liner.create_line(490, 414, 615, 502, fill='white', width=5, arrow=LAST)    # 열교환기-버퍼탱크
        main_Activity.line7 = main_Activity.liner.create_line(598, 541, 457, 444, fill='white', width=5, arrow=LAST)    # 버퍼탱크-열교환기
        main_Activity.line8 = main_Activity.liner.create_line(636, 404, 636, 298, fill='white', width=5, arrow=LAST)    # 버퍼탱크-이중코일
        main_Activity.line9 = main_Activity.liner.create_line(683, 298, 683, 404, fill='white', width=5, arrow=LAST)    # 이중코일-버퍼탱크
        main_Activity.line10 = main_Activity.liner.create_line(828, 157, 710, 227,  fill='white', width=5, arrow=LAST)  # 외기-이중코일
        main_Activity.line11 = main_Activity.liner.create_line(721, 256, 837, 334, fill='white', width=5, arrow=LAST)   # 이중코일-히트펌프
        main_Activity.line12 = main_Activity.liner.create_line(852, 396, 694, 291, fill='white', width=5, arrow=LAST)   # 히트펌프-이중코일
        main_Activity.line13 = main_Activity.liner.create_line(942, 386, 1095, 293, fill='white', width=5, arrow=LAST)  # 히트펌프-저장탱크
        main_Activity.line14 = main_Activity.liner.create_line(1069, 276, 939, 355, fill='white', width=5, arrow=LAST)  # 저장탱크-히트펌프
        main_Activity.line15 = main_Activity.liner.create_line(950, 405, 1093, 498, fill='white', width=5, arrow=LAST)  # 히트펌프-온수탱크
        main_Activity.line16 = main_Activity.liner.create_line(1068, 536, 924, 442, fill='white', width=5, arrow=LAST)  # 온수탱크-히트펌프

        x = 80
        y = 50

        # 설비 이미지 라벨
        self.fan_image = tk.PhotoImage(file='images/fan.png')
        self.bipvt_image = tk.PhotoImage(file='images/bipvt.png')
        self.damper_image = tk.PhotoImage(file='images/damper.png')
        self.exchanger_image = tk.PhotoImage(file='images/exchanger.png')
        self.outair_image = tk.PhotoImage(file='images/outair.png')
        self.buffer_image = tk.PhotoImage(file='images/buffer.png')
        self.doublecoil_image = tk.PhotoImage(file='images/doublecoil.png')
        self.storage_image = tk.PhotoImage(file='images/storage.png')
        self.heatpump_image = tk.PhotoImage(file='images/heatpump.png')
        self.dhw_image = tk.PhotoImage(file='images/dhw.png')

        main_Activity.liner.create_image(350 + x, 50 + y, image=self.fan_image)
        main_Activity.liner.create_image(100 + x, 140 + y, image=self.bipvt_image)
        main_Activity.liner.create_image(100 + x, 380 + y, image=self.damper_image)
        main_Activity.liner.create_image(350 + x, 310 + y, image=self.exchanger_image)
        main_Activity.liner.create_image(250 + x, 500 + y, image=self.outair_image)
        main_Activity.liner.create_image(810 + x, 60 + y, image=self.outair_image)
        main_Activity.liner.create_image(580 + x, 430 + y, image=self.buffer_image)
        main_Activity.liner.create_image(580 + x, 160 + y, image=self.doublecoil_image)
        main_Activity.liner.create_image(1050 + x, 160 + y, image=self.storage_image)
        main_Activity.liner.create_image(810 + x, 310 + y, image=self.heatpump_image)
        main_Activity.liner.create_image(1050 + x, 430 + y, image=self.dhw_image)

        #########
        bipvt_connect_label = Label(main_Activity.liner, text='PVT통신', font=('arial', 13, 'bold'), fg='white', bg='#2f323b')
        bipvt_connect_label.place(x=20, y=13)

        main_Activity.bipvt_connect_value = Label(main_Activity.liner, text='●', font=('arial', 25, 'bold'), fg='red', bg='#2f323b')
        main_Activity.bipvt_connect_value.place(x=100, y=0)

        heatpump_connect_label = Label(main_Activity.liner, text='히트펌프통신', font=('arial', 13, 'bold'), fg='white', bg='#2f323b')
        heatpump_connect_label.place(x=140, y=13)

        main_Activity.heatpump_connect_value = Label(main_Activity.liner, text='●', font=('arial', 25, 'bold'), fg='red', bg='#2f323b')
        main_Activity.heatpump_connect_value.place(x=250, y=0)

        control_label = Label(main_Activity.liner, text='운전상태', font=('arial', 13, 'bold'), fg='white', bg='#2f323b')
        control_label.place(x=20, y=45)

        main_Activity.control_now = Label(main_Activity.liner, text=' - ', font=('arial', 13, 'bold'), fg='white', bg='#2f323b')
        main_Activity.control_now.place(x=100, y=45)

        # bipvt 조도
        bipvt_insolation_label = Label(main_Activity.liner, text='조도', fg='white', bg='#2f323b', font=('arial', 13))
        bipvt_insolation_label.place(x=25, y=110)

        main_Activity.bipvt_insolation_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.bipvt_insolation_value.place(x=70, y=110)

        bipvt_insolation_unit = Label(main_Activity.liner, text='W/m²', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        bipvt_insolation_unit.place(x=125, y=110)

        bipvt_power_label = Label(main_Activity.liner, text='전력', fg='white', bg='#2f323b', font=('arial', 13))
        bipvt_power_label.place(x=25, y=130)

        main_Activity.bipvt_power_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.bipvt_power_value.place(x=70, y=130)

        bipvt_power_unit = Label(main_Activity.liner, text='kW', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        bipvt_power_unit.place(x=125, y=130)

        bipvt_voltage_label = Label(main_Activity.liner, text='전압', fg='white', bg='#2f323b', font=('arial', 13))
        bipvt_voltage_label.place(x=25, y=150)

        main_Activity.bipvt_voltage_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.bipvt_voltage_value.place(x=70, y=150)

        bipvt_voltage_unit = Label(main_Activity.liner, text='V', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        bipvt_voltage_unit.place(x=125, y=150)

        bipvt_current_label = Label(main_Activity.liner, text='전류', fg='white', bg='#2f323b', font=('arial', 13))
        bipvt_current_label.place(x=25, y=170)

        main_Activity.bipvt_current_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.bipvt_current_value.place(x=70, y=170)

        bipvt_current_unit = Label(main_Activity.liner, text='A', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        bipvt_current_unit.place(x=125, y=170)

        bipvt_inner_temp_label = Label(main_Activity.liner, text='입구온도', fg='white', bg='#2f323b', font=('arial', 13))
        bipvt_inner_temp_label.place(x=40, y=245)

        main_Activity.bipvt_inner_temp_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.bipvt_inner_temp_value.place(x=40, y=265)

        bipvt_outer_temp_label = Label(main_Activity.liner, text='출구온도', fg='white', bg='#2f323b', font=('arial', 13))
        bipvt_outer_temp_label.place(x=245, y=245)

        main_Activity.bipvt_outer_temp_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.bipvt_outer_temp_value.place(x=245, y=265)

        fan_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        fan_status_label.place(x=495, y=130)

        main_Activity.fan_status_value = Label(main_Activity.liner, text='ON', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.fan_status_value.place(x=495, y=150)

        damper_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        damper_status_label.place(x=70, y=465)

        main_Activity.damper_status_value = Label(main_Activity.liner, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.damper_status_value.place(x=70, y=485)

        coil_out_temp_label = Label(main_Activity.liner, text='외기온도', fg='white', bg='#2f323b', font=('arial', 13))
        coil_out_temp_label.place(x=960, y=140)

        main_Activity.coil_out_temp_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.coil_out_temp_value.place(x=960, y=160)

        exchanger_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        exchanger_status_label.place(x=335, y=345)

        main_Activity.exchanger_status_value = Label(main_Activity.liner, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.exchanger_status_value.place(x=335, y=365)

        buffer_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        buffer_status_label.place(x=725, y=505)

        main_Activity.buffer_status_value = Label(main_Activity.liner, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.buffer_status_value.place(x=725, y=525)

        buffer_temp_label = Label(main_Activity.liner, text='버퍼탱크온도', fg='white', bg='#2f323b', font=('arial', 13))
        buffer_temp_label.place(x=595, y=580)

        main_Activity.buffer_temp_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.buffer_temp_value.place(x=595, y=600)

        dhw_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        dhw_status_label.place(x=1200, y=510)

        main_Activity.dhw_status_value = Label(main_Activity.liner, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.dhw_status_value.place(x=1200, y=530)

        dhw_temp_label = Label(main_Activity.liner, text='온수탱크온도', fg='white', bg='#2f323b', font=('arial', 13))
        dhw_temp_label.place(x=1065, y=580)

        main_Activity.dhw_temp_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.dhw_temp_value.place(x=1065, y=600)

        heatpump_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        heatpump_status_label.place(x=780, y=390)

        main_Activity.heatpump_status_value = Label(main_Activity.liner, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.heatpump_status_value.place(x=780, y=410)

        heatpump_activepower_label = Label(main_Activity.liner, text='전력사용량', fg='white', bg='#2f323b', font=('arial', 13))
        heatpump_activepower_label.place(x=790,y=490)

        main_Activity.heatpump_activepower_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.heatpump_activepower_value.place(x=880, y=490)

        heatpump_mode_label = Label(main_Activity.liner, text='현재모드', fg='white', bg='#2f323b', font=('arial', 13))
        heatpump_mode_label.place(x=790, y=465)

        main_Activity.heatpump_mode_value = Label(main_Activity.liner, text='급탕', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.heatpump_mode_value.place(x=880, y=465)

        storage_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        storage_status_label.place(x=1200, y=240)

        main_Activity.storage_status_value = Label(main_Activity.liner, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.storage_status_value.place(x=1200, y=260)

        storage_temp_label = Label(main_Activity.liner, text='저장탱크온도', fg='white', bg='#2f323b', font=('arial', 13))
        storage_temp_label.place(x=1065, y=315)

        main_Activity.storage_temp_value = Label(main_Activity.liner, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.storage_temp_value.place(x=1065, y=335)

        doublecoil_status_label = Label(main_Activity.liner, text='상태', fg='white', bg='#2f323b', font=('arial', 13))
        doublecoil_status_label.place(x=550, y=240)

        main_Activity.doublecoil_status_value = Label(main_Activity.liner, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 13, 'bold'))
        main_Activity.doublecoil_status_value.place(x=550, y=260)

        #########

        figure = plt.Figure(figsize=(6,5), dpi=100)
        ax = figure.add_subplot(111, xlim=(0, 24), ylim=(0, 1024))
        chart_type = FigureCanvasTkAgg(figure, self)



    def animate(self):
        y = random.randint(0, 1024)
        old_y = line.get_ydata()