import os, sys
import random
from tkinter import *
import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
from time import sleep


if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

import notification.insert_keypad
import comd.var

# Graph Library
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class main_Activity(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 상단 메뉴바
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, ipady=20)

        self.logo_image = tk.PhotoImage(file="images/bonc_white.png")
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

        main_Activity.time_label1 = Label(left_frame, text='-', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 18, 'bold'), fg='white')
        main_Activity.time_label1.pack(pady=(150, 10))

        main_Activity.time_label2 = Label(left_frame, text='-', highlightbackground='#111111', activebackground='#111111', bd=0, bg='#111111', font=('arial', 18, 'bold'), fg='#96c63e')
        main_Activity.time_label2.pack()

        # center top frame
        center_frame = Frame(self, bg='#2f323b')
        center_frame.pack(fill=BOTH, side=TOP, expand=True)

        # 라인선 그리기
        main_Activity.main_canvas = Canvas(center_frame, bg='#2f323b', highlightbackground='#2f323b', width=900, height=1800)
        main_Activity.main_canvas.pack()

        # 설비 연결선 라벨
        main_Activity.line1 = main_Activity.main_canvas.create_line(465, 190, 685, 190, fill='white', width=5, arrow=LAST)    # PVT-팬
        main_Activity.line2 = main_Activity.main_canvas.create_line(732, 242, 641, 365, fill='white', width=5, arrow=LAST)  # 팬-열교환기
        main_Activity.line3 = main_Activity.main_canvas.create_line(538, 400, 363, 400, fill='white', width=5, arrow=LAST)    # 열교환기-댐퍼
        main_Activity.line4 = main_Activity.main_canvas.create_line(186, 556, 270, 436, fill='#96c63e', width=5, arrow=LAST)    # 외기-댐퍼
        main_Activity.line5 = main_Activity.main_canvas.create_line(342, 338, 417, 235, fill='white', width=5, arrow=LAST)   # 댐퍼-PVT
        main_Activity.line6 = main_Activity.main_canvas.create_line(583, 443, 490, 570, fill='white', width=5, arrow=LAST)    # 열교환기-버퍼탱크
        main_Activity.line7 = main_Activity.main_canvas.create_line(484, 518, 552, 425, fill='white', width=5, arrow=LAST)    # 버퍼탱크-열교환기
        main_Activity.line8 = main_Activity.main_canvas.create_line(513, 590, 688, 590, fill='white', width=5, arrow=LAST)    # 버퍼탱크-이중코일
        main_Activity.line9 = main_Activity.main_canvas.create_line(692, 615, 513, 615, fill='white', width=5, arrow=LAST)    # 이중코일-버퍼탱크
        main_Activity.line11 = main_Activity.main_canvas.create_line(701, 625, 647, 697, fill='white', width=5, arrow=LAST)   # 이중코일-히트펌프
        main_Activity.line12 = main_Activity.main_canvas.create_line(654, 744, 729, 642, fill='white', width=5, arrow=LAST)   # 히트펌프-이중코일
        main_Activity.line13 = main_Activity.main_canvas.create_line(551, 825, 485, 916, fill='white', width=5, arrow=LAST)  # 히트펌프-저장탱크
        main_Activity.line14 = main_Activity.main_canvas.create_line(489, 967, 582, 843, fill='white', width=5, arrow=LAST)  # 저장탱크-히트펌프
        main_Activity.line15 = main_Activity.main_canvas.create_line(538, 788, 363, 788, fill='white', width=5, arrow=LAST)  # 히트펌프-온수탱크
        main_Activity.line16 = main_Activity.main_canvas.create_line(363, 813, 538, 813, fill='white', width=5, arrow=LAST)  # 온수탱크-히트펌프
        main_Activity.line17 = main_Activity.main_canvas.create_line(513, 987, 688, 987, fill='white', width=5, arrow=LAST)  # 저장탱크-FCU
        main_Activity.line18 = main_Activity.main_canvas.create_line(688, 1017, 513, 1017, fill='white', width=5, arrow=LAST)  # FCU-저장탱크

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

        main_Activity.main_canvas.create_image(450, 150, image=self.bipvt_image)
        main_Activity.main_canvas.create_image(750, 150, image=self.fan_image)
        main_Activity.main_canvas.create_image(300, 350, image=self.damper_image)
        main_Activity.main_canvas.create_image(600, 350, image=self.exchanger_image)
        main_Activity.main_canvas.create_image(150, 550, image=self.outair_image)
        # main_Activity.main_canvas.create_image(810, 60, image=self.outair_image)
        main_Activity.main_canvas.create_image(450, 550, image=self.buffer_image)
        main_Activity.main_canvas.create_image(750, 550, image=self.doublecoil_image)
        main_Activity.main_canvas.create_image(600, 750, image=self.heatpump_image)
        main_Activity.main_canvas.create_image(450, 950, image=self.storage_image)
        main_Activity.main_canvas.create_image(300, 750, image=self.dhw_image)
        main_Activity.main_canvas.create_image(750, 950, image=self.dhw_image)

        #########
        bipvt_connect_label = Label(main_Activity.main_canvas, text='PVT통신', font=('arial', 15, 'bold'), fg='white', bg='#2f323b')
        bipvt_connect_label.place(x=20, y=13)

        main_Activity.bipvt_connect_value = Label(main_Activity.main_canvas, text='●', font=('arial', 25, 'bold'), fg='red', bg='#2f323b')
        main_Activity.bipvt_connect_value.place(x=100, y=0)

        heatpump_connect_label = Label(main_Activity.main_canvas, text='히트펌프통신', font=('arial', 15, 'bold'), fg='white', bg='#2f323b')
        heatpump_connect_label.place(x=140, y=13)

        main_Activity.heatpump_connect_value = Label(main_Activity.main_canvas, text='●', font=('arial', 25, 'bold'), fg='red', bg='#2f323b')
        main_Activity.heatpump_connect_value.place(x=250, y=0)

        control_label = Label(main_Activity.main_canvas, text='운전상태', font=('arial', 15, 'bold'), fg='white', bg='#2f323b')
        control_label.place(x=20, y=45)

        main_Activity.control_now = Label(main_Activity.main_canvas, text=' - ', font=('arial', 15, 'bold'), fg='white', bg='#2f323b')
        main_Activity.control_now.place(x=100, y=45)

        # bipvt 내부온도
        bipvt_temp_label = Label(main_Activity.main_canvas, text='내부온도', fg='white', bg='#2f323b', font=('arial', 15))
        bipvt_temp_label.place(x=230, y=110)

        main_Activity.bipvt_temp_value = Label(main_Activity.main_canvas, text='-', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.bipvt_temp_value.place(x=320, y=110)

        bipvt_temp_unit = Label(main_Activity.main_canvas, text='℃', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        bipvt_temp_unit.place(x=360, y=110)

        bipvt_power_label = Label(main_Activity.main_canvas, text='전      력', fg='white', bg='#2f323b', font=('arial', 15))
        bipvt_power_label.place(x=230, y=140)

        main_Activity.bipvt_power_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.bipvt_power_value.place(x=320, y=140)

        bipvt_power_unit = Label(main_Activity.main_canvas, text='kW', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        bipvt_power_unit.place(x=360, y=140)

        bipvt_voltage_label = Label(main_Activity.main_canvas, text='전      압', fg='white', bg='#2f323b', font=('arial', 15))
        bipvt_voltage_label.place(x=230, y=170)

        main_Activity.bipvt_voltage_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.bipvt_voltage_value.place(x=320, y=170)

        bipvt_voltage_unit = Label(main_Activity.main_canvas, text='V', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        bipvt_voltage_unit.place(x=360, y=170)

        bipvt_current_label = Label(main_Activity.main_canvas, text='전      류', fg='white', bg='#2f323b', font=('arial', 15))
        bipvt_current_label.place(x=230, y=200)

        main_Activity.bipvt_current_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.bipvt_current_value.place(x=320, y=200)

        bipvt_current_unit = Label(main_Activity.main_canvas, text='A', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        bipvt_current_unit.place(x=360, y=200)

        # bipvt_inner_temp_label = Label(main_Activity.main_canvas, text='입구온도', fg='white', bg='#2f323b', font=('arial', 15))
        # bipvt_inner_temp_label.place(x=40, y=245)
        #
        # main_Activity.bipvt_inner_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        # main_Activity.bipvt_inner_temp_value.place(x=40, y=265)
        #
        # bipvt_outer_temp_label = Label(main_Activity.main_canvas, text='출구온도', fg='white', bg='#2f323b', font=('arial', 15))
        # bipvt_outer_temp_label.place(x=245, y=245)
        #
        # main_Activity.bipvt_outer_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        # main_Activity.bipvt_outer_temp_value.place(x=245, y=265)
        #
        fan_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        fan_status_label.place(x=775, y=240)

        main_Activity.fan_status_value = Label(main_Activity.main_canvas, text='ON', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.fan_status_value.place(x=775, y=270)

        damper_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        damper_status_label.place(x=185, y=370)

        main_Activity.damper_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.damper_status_value.place(x=185, y=400)

        out_temp_label = Label(main_Activity.main_canvas, text='외부온도', fg='white', bg='#2f323b', font=('arial', 15))
        out_temp_label.place(x=110, y=655)

        main_Activity.out_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.out_temp_value.place(x=110, y=685)

        exchanger_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        exchanger_status_label.place(x=670, y=370)

        main_Activity.exchanger_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.exchanger_status_value.place(x=670, y=400)

        buffer_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        buffer_status_label.place(x=335, y=575)

        main_Activity.buffer_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.buffer_status_value.place(x=335, y=605)

        buffer_temp_label = Label(main_Activity.main_canvas, text='버퍼탱크온도', fg='white', bg='#2f323b', font=('arial', 15))
        buffer_temp_label.place(x=390, y=655)

        main_Activity.buffer_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.buffer_temp_value.place(x=390, y=685)

        dhw_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        dhw_status_label.place(x=185, y=780)

        main_Activity.dhw_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.dhw_status_value.place(x=185, y=810)

        dhw_temp_label = Label(main_Activity.main_canvas, text='온수탱크온도', fg='white', bg='#2f323b', font=('arial', 15))
        dhw_temp_label.place(x=240, y=855)

        main_Activity.dhw_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.dhw_temp_value.place(x=240, y=885)

        heatpump_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        heatpump_status_label.place(x=600, y=850)

        main_Activity.heatpump_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.heatpump_status_value.place(x=600, y=880)

        heatpump_mode_label = Label(main_Activity.main_canvas, text='현재모드', fg='white', bg='#2f323b', font=('arial', 15))
        heatpump_mode_label.place(x=670, y=770)

        main_Activity.heatpump_mode_value = Label(main_Activity.main_canvas, text='급탕', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.heatpump_mode_value.place(x=770, y=770)

        heatpump_activepower_label = Label(main_Activity.main_canvas, text='소비전력', fg='white', bg='#2f323b', font=('arial', 15))
        heatpump_activepower_label.place(x=670, y=800)

        main_Activity.heatpump_activepower_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.heatpump_activepower_value.place(x=770, y=800)

        storage_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        storage_status_label.place(x=335, y=980)

        main_Activity.storage_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.storage_status_value.place(x=335, y=1010)

        storage_temp_label = Label(main_Activity.main_canvas, text='저장탱크온도', fg='white', bg='#2f323b', font=('arial', 15))
        storage_temp_label.place(x=390, y=1055)

        main_Activity.storage_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.storage_temp_value.place(x=390, y=1085)
        #
        doublecoil_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('arial', 15))
        doublecoil_status_label.place(x=775, y=640)

        main_Activity.doublecoil_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b', font=('arial', 15, 'bold'))
        main_Activity.doublecoil_status_value.place(x=775, y=670)

        #########

        figure = plt.Figure(figsize=(6,5), dpi=100)
        ax = figure.add_subplot(111, xlim=(0, 24), ylim=(0, 1024))
        chart_type = FigureCanvasTkAgg(figure, self)



    def animate(self):
        y = random.randint(0, 1024)
        old_y = line.get_ydata()