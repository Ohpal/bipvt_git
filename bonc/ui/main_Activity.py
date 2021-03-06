import os, sys
import random
from tkinter import *
import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
from PIL import ImageTk, Image
from time import sleep
from datetime import datetime, timedelta

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

import notification.insert_keypad
import comd.var
import db.pg_connect

# Graph Library
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import font_manager, rc
import matplotlib.dates as mdates
from matplotlib import style
import mplcursors


style.use("seaborn-darkgrid")
nb_points = 300


class main_Activity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_frame = Frame(self, bg='#111111')
        title_frame.pack(fill=X, side=TOP)

        self.logo_image = PhotoImage(file="images/TEMS2.png")
        logo_label = Label(title_frame, image=self.logo_image, highlightbackground="#111111",
                           activebackground='#111111', bd=0, bg='#111111')
        logo_label.pack(side=LEFT, padx=(30, 50), ipady=20)

        self.gps_image = tk.PhotoImage(file='images/gps.png')
        main_Activity.gps_menu = Label(title_frame, image=self.gps_image, highlightbackground='#111111', activebackground='#111111',
                         bd=0, bg='#111111')
        main_Activity.gps_menu.pack(side=LEFT, padx=(0, 10), pady=(8, 0))

        weather_menu = Label(title_frame, text='날씨', highlightbackground='#111111', activebackground='#111111', bd=0,
                             bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        weather_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        weather_img = Image.open('images/weather/01d.png')
        weather_img = weather_img.resize((40, 40), Image.ANTIALIAS)
        self.weather_image = ImageTk.PhotoImage(weather_img)
        main_Activity.weather_value = Label(title_frame, highlightbackground='#111111', image=self.weather_image,
                                            activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                            fg='white')
        main_Activity.weather_value.pack(side=LEFT, pady=(8, 0))

        temperature_menu = Label(title_frame, text='| 기온', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        temperature_menu.pack(side=LEFT, padx=(10, 10), pady=(8, 0))

        main_Activity.temperature_value = Label(title_frame, text='32.5', highlightbackground='#111111',
                                                activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                                fg='white')
        main_Activity.temperature_value.pack(side=LEFT, pady=(8, 0))

        temperature_unit = Label(title_frame, text=' ℃', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        temperature_unit.pack(side=LEFT, pady=(8, 0))

        humi_menu = Label(title_frame, text='| 습도', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        main_Activity.humi_value = Label(title_frame, text='44.3', highlightbackground='#111111',
                                         activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        main_Activity.humi_value.pack(side=LEFT, pady=(8, 0))

        humi_unit = Label(title_frame, text='%', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_unit.pack(side=LEFT, pady=(8, 0))

        main_Activity.time_label2 = Label(title_frame, text='-', highlightbackground='#111111',
                                          activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 18, 'bold'),
                                          fg='#96c63e')
        main_Activity.time_label2.pack(side=RIGHT, padx=(10, 30), pady=(8, 0))

        main_Activity.time_label1 = Label(title_frame, text='-', highlightbackground='#111111',
                                          activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 18, 'bold'),
                                          fg='white')
        main_Activity.time_label1.pack(side=RIGHT, pady=(8, 0))

        self.date_image = tk.PhotoImage(file='images/date.png')
        date_menu = Label(title_frame, image=self.date_image, highlightbackground='#111111', activebackground='#111111',
                          bd=0, bg='#111111')
        date_menu.pack(side=RIGHT, padx=(0, 5), pady=(8, 0))

        ########################### 메뉴 버튼 ###############################
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, side=TOP, ipady=10)

        self.main_image = tk.PhotoImage(file='images/main_btn.png')
        self.control_image = tk.PhotoImage(file='images/control_btn_off.png')
        self.setting_image = tk.PhotoImage(file='images/setting_btn_off.png')
        self.detail_image = tk.PhotoImage(file='images/detail_btn_off.png')

        main_menu = Button(menu_frame, image=self.main_image, highlightbackground='#111111', activebackground='#111111',
                           bd=0, bg='#111111', command=lambda: controller.show_frame('main_Activity'))
        main_menu.pack(side=LEFT, anchor=CENTER, expand=True)

        control_menu = Button(menu_frame, image=self.control_image, highlightbackground='#111111',
                              activebackground='#111111', bd=0, bg='#111111',
                              command=lambda: controller.show_frame('control_Activity'))
        control_menu.pack(side=LEFT, anchor=CENTER, expand=True)

        detail_menu = Button(menu_frame, image=self.detail_image, highlightbackground='#111111',
                             activebackground='#111111', bd=0, bg='#111111',
                             command=lambda: controller.show_frame('detail_Activity'))
        detail_menu.pack(side=LEFT, anchor=CENTER, expand=True)

        setting_menu = Button(menu_frame, image=self.setting_image, highlightbackground='#111111',
                              activebackground='#111111', bd=0, bg='#111111',
                              command=lambda: controller.show_frame('setting_Activity'))
        setting_menu.pack(side=LEFT, anchor=CENTER, expand=True)

        ###################
        # 상단 데이터 프레임
        top_frame = Frame(self, bg='#111111')
        top_frame.pack(fill=BOTH, side=TOP, expand=True)

        # 데이터 캔버스 그리기
        main_Activity.top_canvas = Canvas(top_frame, bg='#111111', highlightbackground='#111111', width=870, height=200)
        main_Activity.top_canvas.pack(padx=15, fill=X, pady=(15, 0))

        above1_frame = Frame(main_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above1_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above1_title = Label(above1_frame, text='일일 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above1_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        main_Activity.above1_value = Label(above1_frame, text=' - ', fg='#CFDD8E', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        main_Activity.above1_value.pack(fill=X, pady=10)

        above1_unit = Label(above1_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), anchor='e')
        above1_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above2_frame = Frame(main_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above2_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(15, 0))

        above2_title = Label(above2_frame, text='누적 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above2_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        main_Activity.above2_value = Label(above2_frame, text=' - ', fg='#6ECEDA', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        main_Activity.above2_value.pack(fill=X, pady=10)

        above2_unit = Label(above2_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), anchor='e')
        above2_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above3_frame = Frame(main_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above3_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=15)

        above3_title = Label(above3_frame, text='일일 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above3_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        main_Activity.above3_value = Label(above3_frame, text=' - ', fg='#B97687', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        main_Activity.above3_value.pack(fill=X, pady=10)

        above3_unit = Label(above3_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), anchor='e')
        above3_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above4_frame = Frame(main_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above4_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above4_title = Label(above4_frame, text='누적 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above4_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        main_Activity.above4_value = Label(above4_frame, text=' - ', fg='#d18063', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        main_Activity.above4_value.pack(fill=X, pady=10)

        above4_unit = Label(above4_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), anchor='e')
        above4_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        # center top frame
        center_frame = Frame(self, bg='#111111')
        center_frame.pack(fill=BOTH, side=TOP, expand=True)

        # 계통도 캔버스 설정
        main_Activity.main_canvas = Canvas(center_frame, bg='#2f323b', highlightbackground='#2f323b', width=870,
                                           height=1150)
        main_Activity.main_canvas.pack(padx=15, fill=X, pady=15)

        x = -40
        y = 50

        # 설비 연결선 라벨
        main_Activity.line1 = main_Activity.main_canvas.create_line(465 - x, 190, 685 - x, 190, fill='white', width=5,
                                                                    arrow=LAST)  # PVT-팬
        main_Activity.line2 = main_Activity.main_canvas.create_line(732 - x, 242, 641 - x, 365, fill='white', width=5,
                                                                    arrow=LAST)  # 팬-열교환기
        main_Activity.line3 = main_Activity.main_canvas.create_line(538 - x, 400, 363 - x, 400, fill='white', width=5,
                                                                    arrow=LAST)  # 열교환기-댐퍼
        main_Activity.line4 = main_Activity.main_canvas.create_line(186 - x, 556, 270 - x, 436, fill='#96c63e', width=5,
                                                                    arrow=LAST)  # 외기-댐퍼
        main_Activity.line5 = main_Activity.main_canvas.create_line(342 - x, 338, 417 - x, 235, fill='white', width=5,
                                                                    arrow=LAST)  # 댐퍼-PVT
        main_Activity.line6 = main_Activity.main_canvas.create_line(583 - x, 443, 490 - x, 570, fill='white', width=5,
                                                                    arrow=LAST)  # 열교환기-버퍼탱크
        main_Activity.line7 = main_Activity.main_canvas.create_line(484 - x, 518, 552 - x, 425, fill='white', width=5,
                                                                    arrow=LAST)  # 버퍼탱크-열교환기
        main_Activity.line8 = main_Activity.main_canvas.create_line(513 - x, 590, 688 - x, 590, fill='white', width=5,
                                                                    arrow=LAST)  # 버퍼탱크-이중코일
        main_Activity.line9 = main_Activity.main_canvas.create_line(692 - x, 615, 513 - x, 615, fill='white', width=5,
                                                                    arrow=LAST)  # 이중코일-버퍼탱크
        main_Activity.line11 = main_Activity.main_canvas.create_line(701 - x, 625, 647 - x, 697, fill='white', width=5,
                                                                     arrow=LAST)  # 이중코일-히트펌프
        main_Activity.line12 = main_Activity.main_canvas.create_line(654 - x, 744, 729 - x, 642, fill='white', width=5,
                                                                     arrow=LAST)  # 히트펌프-이중코일
        main_Activity.line13 = main_Activity.main_canvas.create_line(551 - x, 825, 485 - x, 916, fill='white', width=5,
                                                                     arrow=LAST)  # 히트펌프-저장탱크
        main_Activity.line14 = main_Activity.main_canvas.create_line(489 - x, 967, 582 - x, 843, fill='white', width=5,
                                                                     arrow=LAST)  # 저장탱크-히트펌프
        main_Activity.line15 = main_Activity.main_canvas.create_line(538 - x, 788, 363 - x, 788, fill='white', width=5,
                                                                     arrow=LAST)  # 히트펌프-온수탱크
        main_Activity.line16 = main_Activity.main_canvas.create_line(363 - x, 813, 538 - x, 813, fill='white', width=5,
                                                                     arrow=LAST)  # 온수탱크-히트펌프
        main_Activity.line17 = main_Activity.main_canvas.create_line(513 - x, 987, 688 - x, 987, fill='white', width=5,
                                                                     arrow=LAST)  # 저장탱크-FCU
        main_Activity.line18 = main_Activity.main_canvas.create_line(688 - x, 1017, 513 - x, 1017, fill='white',
                                                                     width=5, arrow=LAST)  # FCU-저장탱크

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
        self.fcu_image = tk.PhotoImage(file='images/fcu.png')

        main_Activity.main_canvas.create_image(450 - x, 150, image=self.bipvt_image)
        main_Activity.main_canvas.create_image(750 - x, 150, image=self.fan_image)
        main_Activity.main_canvas.create_image(300 - x, 350, image=self.damper_image)
        main_Activity.main_canvas.create_image(600 - x, 350, image=self.exchanger_image)
        main_Activity.main_canvas.create_image(150 - x, 550, image=self.outair_image)
        main_Activity.main_canvas.create_image(450 - x, 550, image=self.buffer_image)
        main_Activity.main_canvas.create_image(750 - x, 550, image=self.doublecoil_image)
        main_Activity.main_canvas.create_image(600 - x, 750, image=self.heatpump_image)
        main_Activity.main_canvas.create_image(450 - x, 950, image=self.storage_image)
        main_Activity.main_canvas.create_image(300 - x, 750, image=self.dhw_image)
        main_Activity.main_canvas.create_image(750 - x, 960, image=self.fcu_image)

        #########
        connect_frame = Frame(main_Activity.main_canvas, bg='#2f323b')
        connect_frame.place(x=20, y=9)

        bipvt_connect_label = Label(connect_frame, text='PVT통신', font=('SCDream5', 15, 'bold'), fg='white',
                                    bg='#2f323b')
        bipvt_connect_label.pack(side=LEFT)

        main_Activity.bipvt_connect_value = Label(connect_frame, text='●', font=('SCDream5', 30, 'bold'),
                                                  fg='red', bg='#2f323b')
        main_Activity.bipvt_connect_value.pack(side=LEFT, padx=(5, 10))

        heatpump_connect_label = Label(connect_frame, text='히트펌프통신', font=('SCDream5', 15, 'bold'), fg='white',
                                       bg='#2f323b')
        heatpump_connect_label.pack(side=LEFT)

        main_Activity.heatpump_connect_value = Label(connect_frame, text='●', font=('SCDream5', 30, 'bold'),
                                                     fg='red', bg='#2f323b')
        main_Activity.heatpump_connect_value.pack(side=LEFT, padx=(5,10))

        # fcu_connect_label = Label(connect_frame, text='FCU통신', font=('SCDream5', 15, 'bold'), fg='white',
        #                           bg='#2f323b')
        # fcu_connect_label.pack(side=LEFT)

        # main_Activity.fcu_connect_value = Label(connect_frame, text='●', font=('SCDream5', 30, 'bold'),
        #                                         fg='red', bg='#2f323b')
        # main_Activity.fcu_connect_value.pack(side=LEFT, padx=(5,10))

        control_label = Label(main_Activity.main_canvas, text='운전상태', font=('SCDream5', 15, 'bold'), fg='white',
                              bg='#2f323b')
        control_label.place(x=20, y=50)

        main_Activity.control_now = Label(main_Activity.main_canvas, text=' - ', font=('SCDream5', 15, 'bold'), fg='white',
                                          bg='#2f323b')
        main_Activity.control_now.place(x=110, y=50)

        system_exit_btn = Button(main_Activity.main_canvas, text='', highlightbackground='#2F323B',
                                 activebackground='#2F323B', bd=0, width=50, height=2,
                                 bg='#2F323B', command=lambda: self.sys_exit())
        system_exit_btn.place(x=950, y=0)

        # bipvt 일사량
        bipvt_insolation_frame = Frame(main_Activity.main_canvas, bg='#2f323b')
        bipvt_insolation_frame.place(x=230 -x -20, y=100)

        bipvt_insolation_label = Label(bipvt_insolation_frame, text='일  사 량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        bipvt_insolation_label.pack(side=LEFT)

        main_Activity.bipvt_insolation_value = Label(bipvt_insolation_frame, text='-', fg='#96c63e', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        main_Activity.bipvt_insolation_value.pack(side=LEFT, padx=(10, 3))

        bipvt_insolation_unit = Label(bipvt_insolation_frame, text='W/m²', fg='#96c63e', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        bipvt_insolation_unit.pack(side=LEFT)

        # bipvt 전력
        bipvt_power_frame = Frame(main_Activity.main_canvas, bg='#2f323b')
        bipvt_power_frame.place(x=230-x-20, y=130)

        bipvt_power_label = Label(bipvt_power_frame, text='발전전력', fg='white', bg='#2f323b',
                                  font=('SCDream5', 15, 'bold'))
        bipvt_power_label.pack(side=LEFT)

        main_Activity.bipvt_power_value = Label(bipvt_power_frame, text=' - ', fg='#96c63e', bg='#2f323b',
                                                font=('SCDream5', 15, 'bold'))
        main_Activity.bipvt_power_value.pack(side=LEFT, padx=(10, 3))

        bipvt_power_unit = Label(bipvt_power_frame, text='W', fg='#96c63e', bg='#2f323b',
                                 font=('SCDream5', 15, 'bold'))
        bipvt_power_unit.pack(side=LEFT)

        # bipvt 내부온도
        bipvt_temp_frame = Frame(main_Activity.main_canvas, bg='#2f323b')
        bipvt_temp_frame.place(x=230 -x -20, y=160)

        bipvt_temp_label = Label(bipvt_temp_frame, text='내부온도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        bipvt_temp_label.pack(side=LEFT)

        main_Activity.bipvt_inside_temp_value = Label(bipvt_temp_frame, text='-', fg='#96c63e', bg='#2f323b',
                                               font=('SCDream5', 15, 'bold'))
        main_Activity.bipvt_inside_temp_value.pack(side=LEFT, padx=(10, 0))

        # main_Activity.bipvt_inside_temp_value2 = Label(bipvt_temp_frame, text='-', fg='#96c63e', bg='#2f323b',
        #                                                font=('SCDream5', 15, 'bold'))
        # main_Activity.bipvt_inside_temp_value2.pack(side=LEFT)
        #
        # main_Activity.bipvt_inside_temp_value3 = Label(bipvt_temp_frame, text='-', fg='#96c63e', bg='#2f323b',
        #                                                font=('SCDream5', 15, 'bold'))
        # main_Activity.bipvt_inside_temp_value3.pack(side=LEFT, padx=(0, 3))

        bipvt_temp_unit = Label(bipvt_temp_frame, text='℃', fg='#96c63e', bg='#2f323b',
                                font=('SCDream5', 15, 'bold'))
        bipvt_temp_unit.pack(side=LEFT)

        fan_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        fan_status_label.place(x=820 - x, y=170)

        main_Activity.fan_status_value = Label(main_Activity.main_canvas, text='ON', fg='#96c63e', bg='#2f323b',
                                               font=('SCDream5', 15, 'bold'))
        main_Activity.fan_status_value.place(x=820 - x, y=200)

        damper_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        damper_status_label.place(x=185 - x, y=370)

        main_Activity.damper_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
                                                  font=('SCDream5', 15, 'bold'))
        main_Activity.damper_status_value.place(x=185 - x, y=400)

        out_temp_label = Label(main_Activity.main_canvas, text='외부온도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        out_temp_label.place(x=80 - x, y=655)

        main_Activity.out_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.out_temp_value.place(x=170 - x, y=655)

        out_humi_label = Label(main_Activity.main_canvas, text='외부습도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        out_humi_label.place(x=80 - x, y=685)

        main_Activity.out_humi_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.out_humi_value.place(x=170 - x, y=685)

        out_humi_label = Label(main_Activity.main_canvas, text='풍      속', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        out_humi_label.place(x=80 - x, y=715)

        main_Activity.wind_speed_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.wind_speed_value.place(x=170 - x, y=715)

        exchanger_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b',
                                       font=('SCDream5', 15, 'bold'))
        exchanger_status_label.place(x=670 - x, y=370)

        main_Activity.exchanger_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
                                                     font=('SCDream5', 15, 'bold'))
        main_Activity.exchanger_status_value.place(x=670 - x, y=400)

        # buffer_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        # buffer_status_label.place(x=335 - x, y=575)
        #
        # main_Activity.buffer_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
        #                                           font=('SCDream5', 15, 'bold'))
        # main_Activity.buffer_status_value.place(x=335 - x, y=605)

        buffer_power_label = Label(main_Activity.main_canvas, text='소비전력', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        buffer_power_label.place(x=300 - x, y=575)

        main_Activity.buffer_power_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b', font=('SCDream5', 15, 'bold',))
        main_Activity.buffer_power_value.place(x=300 - x, y=605)

        buffer_temp_label = Label(main_Activity.main_canvas, text='버퍼탱크온도', fg='white', bg='#2f323b',
                                  font=('SCDream5', 15, 'bold'))
        buffer_temp_label.place(x=350 - x, y=655)

        main_Activity.buffer_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                                font=('SCDream5', 15, 'bold'))
        main_Activity.buffer_temp_value.place(x=480 - x, y=655)

        # buffer_temp_label = Label(main_Activity.main_canvas, text='버퍼입구온도', fg='white', bg='#2f323b',
        #                           font=('SCDream5', 15, 'bold'))
        # buffer_temp_label.place(x=350 - x, y=685)
        #
        # main_Activity.buffer_inner_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
        #                                         font=('SCDream5', 15, 'bold'))
        # main_Activity.buffer_inner_temp_value.place(x=480 - x, y=685)

        # dhw_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        # dhw_status_label.place(x=185 - x, y=780)

        # main_Activity.dhw_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
        #                                        font=('SCDream5', 15, 'bold'))
        # main_Activity.dhw_status_value.place(x=185 - x, y=810)

        dhw_power_label = Label(main_Activity.main_canvas, text='소비전력', fg='white', bg='#2f323b',
                                font=('SCDream5', 15, 'bold'))
        dhw_power_label.place(x=145 - x, y=780)

        main_Activity.dhw_power_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                              font=('SCDream5', 15, 'bold',))
        main_Activity.dhw_power_value.place(x=145 - x, y=810)

        dhw_temp_label = Label(main_Activity.main_canvas, text='급탕탱크온도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        dhw_temp_label.place(x=210 - x, y=855)

        main_Activity.dhw_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.dhw_temp_value.place(x=340 - x, y=855)

        dhw_inner_temp_label = Label(main_Activity.main_canvas, text='급탕입구온도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        dhw_inner_temp_label.place(x=210 - x, y=885)

        main_Activity.dhw_inner_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.dhw_inner_temp_value.place(x=340 - x, y=885)

        dhw_outer_temp_label = Label(main_Activity.main_canvas, text='급탕출구온도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        dhw_outer_temp_label.place(x=210 - x, y=915)

        main_Activity.dhw_outer_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.dhw_outer_temp_value.place(x=340 - x, y=915)

        heatpump_status_label = Label(main_Activity.main_canvas, text='상      태', fg='white', bg='#2f323b',
                                      font=('SCDream5', 15, 'bold'))
        heatpump_status_label.place(x=670 - x, y=760)

        main_Activity.heatpump_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
                                                    font=('SCDream5', 15, 'bold'))
        main_Activity.heatpump_status_value.place(x=760 - x, y=760)

        heatpump_mode_label = Label(main_Activity.main_canvas, text='현재모드', fg='white', bg='#2f323b',
                                    font=('SCDream5', 15, 'bold'))
        heatpump_mode_label.place(x=670 - x, y=790)

        main_Activity.heatpump_mode_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                                  font=('SCDream5', 15, 'bold'))
        main_Activity.heatpump_mode_value.place(x=760 - x, y=790)

        heatpump_activepower_label = Label(main_Activity.main_canvas, text='소비전력', fg='white', bg='#2f323b',
                                           font=('SCDream5', 15, 'bold'))
        heatpump_activepower_label.place(x=670 - x, y=820)

        main_Activity.heatpump_activepower_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e',
                                                         bg='#2f323b', font=('SCDream5', 15, 'bold'))
        main_Activity.heatpump_activepower_value.place(x=760 - x, y=820)

        # storage_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        # storage_status_label.place(x=335 - x, y=980)
        #
        # main_Activity.storage_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
        #                                            font=('SCDream5', 15, 'bold'))
        # main_Activity.storage_status_value.place(x=335 - x, y=1010)

        storage_power_label = Label(main_Activity.main_canvas, text='소비전력', fg='white', bg='#2f323b',
                                    font=('SCDream5', 15, 'bold'))
        storage_power_label.place(x=290 - x, y=980)

        main_Activity.storage_power_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                                  font=('SCDream5', 15, 'bold',))
        main_Activity.storage_power_value.place(x=290 - x, y=1010)

        storage_temp_label = Label(main_Activity.main_canvas, text='저장탱크출구온도', fg='white', bg='#2f323b',
                                   font=('SCDream5', 15, 'bold'))
        storage_temp_label.place(x=330 - x, y=1085)

        main_Activity.storage_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                                 font=('SCDream5', 15, 'bold'))
        main_Activity.storage_temp_value.place(x=490 - x, y=1085)

        storage_outer_temp_label = Label(main_Activity.main_canvas, text='저장탱크입구온도', fg='white', bg='#2f323b',
                                   font=('SCDream5', 15, 'bold'))
        storage_outer_temp_label.place(x=330 - x, y=1055)

        main_Activity.storage_outer_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                                 font=('SCDream5', 15, 'bold'))
        main_Activity.storage_outer_temp_value.place(x=490 - x, y=1055)

        doublecoil_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b',
                                        font=('SCDream5', 15, 'bold'))
        doublecoil_status_label.place(x=820 - x, y=570)

        main_Activity.doublecoil_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
                                                      font=('SCDream5', 15, 'bold'))
        main_Activity.doublecoil_status_value.place(x=820 - x, y=600)

        # fcu_status_label = Label(main_Activity.main_canvas, text='상태', fg='white', bg='#2f323b',
        #                          font=('SCDream5', 15, 'bold'))
        # fcu_status_label.place(x=820 - x, y=970)
        #
        # main_Activity.fcu_status_value = Label(main_Activity.main_canvas, text='OFF', fg='#96c63e', bg='#2f323b',
        #                                        font=('SCDream5', 15, 'bold'))
        # main_Activity.fcu_status_value.place(x=820 - x, y=1000)

        fcu_temp_label = Label(main_Activity.main_canvas, text='실내온도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        fcu_temp_label.place(x=680 - x, y=1055)

        main_Activity.fcu_temp_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.fcu_temp_value.place(x=775 - x, y=1055)

        fcu_humi_label = Label(main_Activity.main_canvas, text='실내습도', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'))
        fcu_humi_label.place(x=680 - x, y=1085)

        main_Activity.fcu_humi_value = Label(main_Activity.main_canvas, text=' - ', fg='#96c63e', bg='#2f323b',
                                             font=('SCDream5', 15, 'bold'))
        main_Activity.fcu_humi_value.place(x=775 - x, y=1085)

        #########
        # 하단 그래프 프레임
        bottom_frame = Frame(self, bg='#111111')
        bottom_frame.pack(fill=BOTH, side=TOP, expand=True)

        # 그래프 캔버스 그리기
        main_Activity.bottom_canvas = Canvas(bottom_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=400)
        main_Activity.bottom_canvas.pack(padx=15, fill=X)

        self.fig = plt.figure()
        self.fig.patch.set_facecolor('#2f323b')

        font_path = 'images/SCDream5.otf'
        font = font_manager.FontProperties(fname=font_path).get_name()
        plt.rc('font', family=font)

        self.ax = self.fig.add_subplot(111)
        self.ax.tick_params(axis='x', colors='white', labelsize=13)
        self.ax.tick_params(axis='y', colors='white', labelsize=13)
        self.ax.set_title('태양광 발전량 현황/예측', color='white', fontsize=15)
        self.ax.set_ylabel('태양광 발전량', color='white', fontsize=13)


        # format the x-axis to show the time
        myFmt = mdates.DateFormatter("%H:%M")
        self.ax.xaxis.set_major_formatter(myFmt)
        # initial x and y data
        dateTimeObj = datetime.now() + timedelta(minutes=-nb_points) + timedelta(minutes=30)
        self.x_pre_data = [dateTimeObj + timedelta(minutes=i) for i in range(int(nb_points))]
        self.y_pre_data = [0 for i in range(int(nb_points))]
        # self.x_pre_data = db.pg_connect.pre_data_select()
        # self.x_pre_data =
        # print('Y_pre', self.y_pre_data)
        # print('X_pre', self.x_pre_data)

        self.x_data = [dateTimeObj + timedelta(minutes=i) for i in range(int(nb_points) - 30)]
        self.y_data = [0 for i in range(int(nb_points) - 30)]
        # print('LEN', len(self.y_data))

        # create the plot(c:line color, markerfacecolor:marker color
        self.pre_plot = self.ax.plot(self.x_pre_data, self.y_pre_data, c='red', markerfacecolor='red', markersize=8, marker='o', linewidth=2, label='예측 발전량')[0]
        self.plot = self.ax.plot(self.x_data, self.y_data, c='#2f323b', markerfacecolor='#2f323b', markersize=8, marker='o', linewidth=2, label='실시간 발전량')[0]
        plt.legend(loc='upper left')

        self.ax.set_ylim(0, 3800)
        self.ax.set_xlim(self.x_pre_data[0], self.x_pre_data[-1])

        self.graph_canvas = FigureCanvasTkAgg(self.fig, master=main_Activity.bottom_canvas)
        self.graph_canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        self.animate()
        # x, y cursors and show data
        self.crs = mplcursors.cursor(self.ax, hover=True)
        self.crs.connect('add', lambda sel: self.cursor_annotation(sel))

    def cursor_annotation(self, sel):
        time_data = sel.annotation._text.split('=')[1].replace('\ny', '')
        sel.annotation.set_text('시간 >> {1}\n발전량 >> {0} W'.format(round(sel.target[1], 2), time_data))
        sel.annotation.get_bbox_patch().set(fc='lightsalmon', alpha=0.5)

    def animate(self):
        # append new data point to the x and y data
        try:
            try:
                pv_power = comd.var.bipvt_temp_data[46]+comd.var.bipvt_temp_data[48]
            except:
                pv_power = 0

            try:
                pv_pre_power = 0 if pv_power == 0 else db.pg_connect.pre_data_select()
            except:
                pv_pre_power = 0

            self.x_pre_data.append(datetime.now() + timedelta(minutes=30))
            self.y_pre_data.append(pv_pre_power)
            # self.y_pre_data.append(random.randint(0, 3000))

            self.x_data.append(datetime.now())
            self.y_data.append(pv_power)

            print('Graph : ', self.y_pre_data, self.y_data)
            # self.y_data.append(random.randint(0, 3000))

            # remove oldest data point
            self.x_pre_data = self.x_pre_data[1:]
            self.y_pre_data = self.y_pre_data[1:]

            self.x_data = self.x_data[1:]
            self.y_data = self.y_data[1:]

            #  update plot data
            self.pre_plot.set_xdata(self.x_pre_data)
            self.pre_plot.set_ydata(self.y_pre_data)

            self.plot.set_xdata(self.x_data)
            self.plot.set_ydata(self.y_data)

            # set text x,y / y data
            # self.ax.text(self.x_data[-1], self.y_data[-1], '{}'.format(self.y_data[-1]), fontdict={'size': 8}, rotation=60)
            # range x data
            self.ax.set_xlim(self.x_pre_data[0], self.x_pre_data[-1])
            # self.ax.text(self.x_data,self.y_data, '%s'.format(self.y_data))
            # print(self.x_data[-1], self.y_data[-1])
            self.graph_canvas.draw_idle()  # redraw plot
            self.after(1000*60*10, self.animate)  # repeat after 1s

            # 1 : 60 / 1000*60
        except Exception as ex:
            print('animate() Exception >> ', ex)

    def sys_exit(self):
        res_msg = tkinter.messagebox.askyesno('프로그램 종료', '프로그램을 종료하시겠습니까?', icon='warning')

        if res_msg:
            sys.exit(0)

    def now_time(self):
        now = datetime.datetime.now()
        now = now.strftime("%H:%M:%S")
        return now

    def time_converse(self, data):
        return datetime.fromtimestamp(data).strftime("%H:%M")
