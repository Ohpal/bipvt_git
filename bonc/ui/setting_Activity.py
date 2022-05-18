import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog
import tkinter.messagebox
from PIL import Image, ImageTk
from time import sleep
from pymodbus.client.sync import ModbusTcpClient, ModbusSerialClient
import notification.insert_keypad
import subprocess

import comd.var
import comd.read_cmd

import db.sqlite_connect


class setting_Activity(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_frame = Frame(self, bg='#111111')
        title_frame.pack(fill=X, side=TOP)

        self.logo_image = tk.PhotoImage(file="images/TEMS2.png")
        logo_label = Label(title_frame, image=self.logo_image, highlightbackground="#111111",
                           activebackground='#111111', bd=0, bg='#111111')
        logo_label.pack(side=LEFT, padx=(30, 50), ipady=20)

        self.gps_image = tk.PhotoImage(file='images/gps.png')
        gps_menu = Label(title_frame, image=self.gps_image, highlightbackground='#111111', activebackground='#111111',
                         bd=0, bg='#111111')
        gps_menu.pack(side=LEFT, padx=(0, 10), pady=(8, 0))

        weather_menu = Label(title_frame, text='날씨', highlightbackground='#111111', activebackground='#111111', bd=0,
                             bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        weather_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        weather_img = Image.open('images/weather/01d.png')
        weather_img = weather_img.resize((40, 40), Image.ANTIALIAS)
        self.weather_image = ImageTk.PhotoImage(weather_img)
        setting_Activity.weather_value = Label(title_frame, text='맑음', highlightbackground='#111111', image=self.weather_image,
                                            activebackground='#111111', bd=0, bg='#111111',
                                            font=('SCDream5', 16, 'bold'),
                                            fg='white')
        setting_Activity.weather_value.pack(side=LEFT, pady=(8, 0))

        temperature_menu = Label(title_frame, text='| 기온', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_menu.pack(side=LEFT, padx=(10, 10), pady=(8, 0))

        setting_Activity.temperature_value = Label(title_frame, text='32.5', highlightbackground='#111111',
                                                activebackground='#111111', bd=0, bg='#111111',
                                                font=('SCDream5', 16, 'bold'),
                                                fg='white')
        setting_Activity.temperature_value.pack(side=LEFT, pady=(8, 0))

        temperature_unit = Label(title_frame, text=' ℃', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_unit.pack(side=LEFT, pady=(8, 0))

        humi_menu = Label(title_frame, text='| 습도', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        setting_Activity.humi_value = Label(title_frame, text='44.3', highlightbackground='#111111',
                                         activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                         fg='white')
        setting_Activity.humi_value.pack(side=LEFT, pady=(8, 0))

        humi_unit = Label(title_frame, text='%', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_unit.pack(side=LEFT, pady=(8, 0))

        setting_Activity.time_label2 = Label(title_frame, text='-', highlightbackground='#111111',
                                          activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 18, 'bold'),
                                          fg='#96c63e')
        setting_Activity.time_label2.pack(side=RIGHT, padx=(10, 30), pady=(8, 0))

        setting_Activity.time_label1 = Label(title_frame, text='-', highlightbackground='#111111',
                                          activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 18, 'bold'),
                                          fg='white')
        setting_Activity.time_label1.pack(side=RIGHT, pady=(8, 0))

        self.date_image = tk.PhotoImage(file='images/date.png')
        date_menu = Label(title_frame, image=self.date_image, highlightbackground='#111111', activebackground='#111111',
                          bd=0, bg='#111111')
        date_menu.pack(side=RIGHT, padx=(0, 5), pady=(8, 0))

        ########################### 메뉴 버튼 ###############################
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, side=TOP, ipady=10)

        self.main_image = tk.PhotoImage(file='images/main_btn_off.png')
        self.control_image = tk.PhotoImage(file='images/control_btn_off.png')
        self.setting_image = tk.PhotoImage(file='images/setting_btn.png')
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
        setting_Activity.top_canvas = Canvas(top_frame, bg='#111111', highlightbackground='#111111', width=870, height=200)
        setting_Activity.top_canvas.pack(padx=15, fill=X, pady=(15, 0))

        above1_frame = Frame(setting_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above1_frame.pack(side=LEFT, fill=BOTH, expand=True, )

        above1_title = Label(above1_frame, text='일일 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above1_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        setting_Activity.above1_value = Label(above1_frame, text=' - ', fg='#CFDD8E', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        setting_Activity.above1_value.pack(fill=X, pady=10)

        above1_unit = Label(above1_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above1_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above2_frame = Frame(setting_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above2_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(15, 0))

        above2_title = Label(above2_frame, text='누적 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above2_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        setting_Activity.above2_value = Label(above2_frame, text=' - ', fg='#6ECEDA', bg='#2f323b',
                             font=('SCDream5', 25, 'bold'))
        setting_Activity.above2_value.pack(fill=X, pady=10)

        above2_unit = Label(above2_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above2_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above3_frame = Frame(setting_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above3_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=15)

        above3_title = Label(above3_frame, text='일일 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above3_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        setting_Activity.above3_value = Label(above3_frame, text=' - ', fg='#B97687', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        setting_Activity.above3_value.pack(fill=X, pady=10)

        above3_unit = Label(above3_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above3_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above4_frame = Frame(setting_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above4_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above4_title = Label(above4_frame, text='누적 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above4_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        setting_Activity.above4_value = Label(above4_frame, text=' - ', fg='#d18063', bg='#2f323b',
                             font=('SCDream5', 25, 'bold'))
        setting_Activity.above4_value.pack(fill=X, pady=10)

        above4_unit = Label(above4_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above4_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        # communication canvas
        communication_frame = Frame(self, bg='#111111')
        communication_frame.pack(fill=BOTH, side=TOP, expand=True)

        setting_Activity.communication_canvas = Canvas(communication_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=600)
        setting_Activity.communication_canvas.pack(fill=BOTH, padx=15, pady=15, expand=True, side=TOP)

        communication_title_frame = Frame(setting_Activity.communication_canvas, bg='#2f323b')
        communication_title_frame.pack(fill=X)

        communication_title = Label(communication_title_frame, text='통신 설정', font=('SCDream5', 20, 'bold'), fg='#96c63e', bg='#2f323b')
        communication_title.pack(pady=20)

        # BIPVT 캔버스
        bipvt_canvas = Canvas(setting_Activity.communication_canvas, bg='#2f323b', highlightbackground='#2f323b')
        bipvt_canvas.pack(fill=X, padx=30, pady=(30, 0))

        bipvt_labelframe = LabelFrame(bipvt_canvas, bg='#2f323b', text='BIPVT 통신설정', font=('SCDream5', 20, 'bold'), fg='white')
        bipvt_labelframe.pack(fill=X, padx=5, pady=5, ipady=5)

        bipvt_frame = Frame(bipvt_labelframe, bg='#2f323b')
        bipvt_frame.pack(fill=X, padx=50, pady=20)

        bipvt_label = Label(bipvt_frame, text='통신 방식', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b')
        bipvt_label.pack(side=LEFT, padx=(0, 20))

        setting_Activity.bipvt_combo = ttk.Combobox(bipvt_frame, values=['Socket 통신', 'Modbus-TCP 통신', 'Modbus-RTU 통신'], font=('SCDream5', 15, 'bold'), state='readonly', justify='center')
        self.option_add('*TCombobox*Listbox.font', ('SCDream5', 15, 'bold'))
        setting_Activity.bipvt_combo.bind('<<ComboboxSelected>>', self.bipvt_selected)
        setting_Activity.bipvt_combo.pack(side=LEFT)

        setting_Activity.bipvt_tcp_frame = Frame(bipvt_labelframe, bg='#2f323b')
        setting_Activity.bipvt_tcp_frame.pack(fill=X, padx=(50, 0), pady=10, ipadx=10, ipady=10)

        Label(setting_Activity.bipvt_tcp_frame, text='IP', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_entry1 = Entry(setting_Activity.bipvt_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_entry1.pack(side=LEFT, padx=(10, 0))
        setting_Activity.bipvt_entry1.bind('<FocusIn>', self.insert_bipvt_ip1)

        Label(setting_Activity.bipvt_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)

        setting_Activity.bipvt_entry2 = Entry(setting_Activity.bipvt_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_entry2.pack(side=LEFT)
        setting_Activity.bipvt_entry2.bind('<FocusIn>', self.insert_bipvt_ip2)

        Label(setting_Activity.bipvt_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)

        setting_Activity.bipvt_entry3 = Entry(setting_Activity.bipvt_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_entry3.pack(side=LEFT)
        setting_Activity.bipvt_entry3.bind('<FocusIn>', self.insert_bipvt_ip3)

        Label(setting_Activity.bipvt_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)

        setting_Activity.bipvt_entry4 = Entry(setting_Activity.bipvt_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_entry4.pack(side=LEFT)
        setting_Activity.bipvt_entry4.bind('<FocusIn>', self.insert_bipvt_ip4)

        Label(setting_Activity.bipvt_tcp_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold'), width=7, anchor='e').pack(side=LEFT, padx=(10,30))

        setting_Activity.bipvt_entry5 = Entry(setting_Activity.bipvt_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_entry5.pack(side=LEFT)
        setting_Activity.bipvt_entry5.bind('<FocusIn>', self.insert_bipvt_port)

        bipvt_apply = Button(setting_Activity.bipvt_tcp_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용', command=lambda: self.bipvt_apply_btn())
        bipvt_apply.pack(side=LEFT, padx=(30, 0))

        # bipvt serial frame
        setting_Activity.bipvt_serial_frame = Frame(bipvt_labelframe, bg='#2f323b')
        setting_Activity.bipvt_serial_frame.pack(fill=X, padx=(50, 0), pady=30)

        Label(setting_Activity.bipvt_serial_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry1 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry1.pack(side=LEFT, padx=(10, 20))
        setting_Activity.bipvt_serial_entry1.bind('<FocusIn>', self.insert_bipvt_serial1)

        Label(setting_Activity.bipvt_serial_frame, text='BRATE', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry2 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry2.pack(side=LEFT, padx=(10, 20))
        setting_Activity.bipvt_serial_entry2.bind('<FocusIn>', self.insert_bipvt_serial2)

        Label(setting_Activity.bipvt_serial_frame, text='PARITY', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry3 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry3.pack(side=LEFT, padx=(10, 20))
        setting_Activity.bipvt_serial_entry3.bind('<FocusIn>', self.insert_bipvt_serial3)

        Label(setting_Activity.bipvt_serial_frame, text='STOPBIT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry4 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry4.pack(side=LEFT, padx=(10, 0))
        setting_Activity.bipvt_serial_entry4.bind('<FocusIn>', self.insert_bipvt_serial4)

        bipvt_serial_apply = Button(setting_Activity.bipvt_serial_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용',
                             command=lambda: self.bipvt_serial_apply_btn())
        bipvt_serial_apply.pack(side=LEFT, padx=(30, 0))

        # 히트펌프 캔버스
        heatpump_canvas = Canvas(setting_Activity.communication_canvas, bg='#2f323b', highlightbackground='#2f323b')
        heatpump_canvas.pack(fill=X, pady=(80, 50), padx=30)
        
        heatpump_labelframe = LabelFrame(heatpump_canvas, bg='#2f323b', text='히트펌프 통신설정', font=('SCDream5', 20, 'bold'), fg='white')
        heatpump_labelframe.pack(fill=X, padx=5, pady=5, ipady=5)

        heatpump_frame = Frame(heatpump_labelframe, bg='#2f323b')
        heatpump_frame.pack(fill=X, padx=50, pady=20)

        heatpump_label = Label(heatpump_frame, text='통신 방식', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b')
        heatpump_label.pack(side=LEFT, padx=(0, 40))

        setting_Activity.heatpump_combo = ttk.Combobox(heatpump_frame, values=['Socket 통신', 'Modbus-TCP 통신', 'Modbus-RTU 통신'], font=('SCDream5', 15, 'bold'), state='readonly', justify='center')
        self.option_add('*TCombobox*Listbox.font', ('SCDream5', 15, 'bold'))
        setting_Activity.heatpump_combo.bind('<<ComboboxSelected>>', self.heatpump_selected)
        setting_Activity.heatpump_combo.pack(side=LEFT)

        setting_Activity.heatpump_tcp_frame = Frame(heatpump_labelframe, bg='#2f323b')
        setting_Activity.heatpump_tcp_frame.pack(fill=X, padx=(50, 0), pady=30)

        Label(setting_Activity.heatpump_tcp_frame, text='IP', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.heatpump_entry1 = Entry(setting_Activity.heatpump_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_entry1.pack(side=LEFT, padx=(10, 0))
        setting_Activity.heatpump_entry1.bind('<FocusIn>', self.insert_heatpump_ip1)

        Label(setting_Activity.heatpump_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)

        setting_Activity.heatpump_entry2 = Entry(setting_Activity.heatpump_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_entry2.pack(side=LEFT)
        setting_Activity.heatpump_entry2.bind('<FocusIn>', self.insert_heatpump_ip2)

        Label(setting_Activity.heatpump_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)

        setting_Activity.heatpump_entry3 = Entry(setting_Activity.heatpump_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_entry3.pack(side=LEFT)
        setting_Activity.heatpump_entry3.bind('<FocusIn>', self.insert_heatpump_ip3)

        Label(setting_Activity.heatpump_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)

        setting_Activity.heatpump_entry4 = Entry(setting_Activity.heatpump_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_entry4.pack(side=LEFT)
        setting_Activity.heatpump_entry4.bind('<FocusIn>', self.insert_heatpump_ip4)

        Label(setting_Activity.heatpump_tcp_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold'), width=7, anchor='e').pack(side=LEFT, padx=(10,30))

        setting_Activity.heatpump_entry5 = Entry(setting_Activity.heatpump_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_entry5.pack(side=LEFT)
        setting_Activity.heatpump_entry5.bind('<FocusIn>', self.insert_heatpump_port)

        heatpump_apply = Button(setting_Activity.heatpump_tcp_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용', command=lambda: self.heatpump_apply_btn())
        heatpump_apply.pack(side=LEFT, padx=(30, 0))

        # heatpump serial frame
        setting_Activity.heatpump_serial_frame = Frame(heatpump_labelframe, bg='#2f323b')
        setting_Activity.heatpump_serial_frame.pack(fill=X, padx=(50, 0), pady=30)
        # setting_Activity.heatpump_serial_frame.pack_forget()

        Label(setting_Activity.heatpump_serial_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.heatpump_serial_entry1 = Entry(setting_Activity.heatpump_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_serial_entry1.pack(side=LEFT, padx=(10, 20))
        setting_Activity.heatpump_serial_entry1.bind('<FocusIn>', self.insert_heatpump_serial1)

        Label(setting_Activity.heatpump_serial_frame, text='BRATE', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.heatpump_serial_entry2 = Entry(setting_Activity.heatpump_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_serial_entry2.pack(side=LEFT, padx=(10, 20))
        setting_Activity.heatpump_serial_entry2.bind('<FocusIn>', self.insert_heatpump_serial2)

        Label(setting_Activity.heatpump_serial_frame, text='PARITY', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.heatpump_serial_entry3 = Entry(setting_Activity.heatpump_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_serial_entry3.pack(side=LEFT, padx=(10, 20))
        setting_Activity.heatpump_serial_entry3.bind('<FocusIn>', self.insert_heatpump_serial3)

        Label(setting_Activity.heatpump_serial_frame, text='STOPBIT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.heatpump_serial_entry4 = Entry(setting_Activity.heatpump_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.heatpump_serial_entry4.pack(side=LEFT, padx=(10, 0))
        setting_Activity.heatpump_serial_entry4.bind('<FocusIn>', self.insert_heatpump_serial4)

        heatpump_serial_apply = Button(setting_Activity.heatpump_serial_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용',
                             command=lambda: self.heatpump_serial_apply_btn())
        heatpump_serial_apply.pack(side=LEFT, padx=(30, 0))

        # # FCU 통신 설정
        # fcu_canvas = Canvas(setting_Activity.communication_canvas, bg='#2f323b', highlightbackground='#2f323b')
        # fcu_canvas.pack(fill=X, padx=30, pady=(0, 40))
        #
        # fcu_labelframe = LabelFrame(fcu_canvas, bg='#2f323b', text='FCU 통신설정', font=('SCDream5', 20, 'bold'), fg='white')
        # fcu_labelframe.pack(fill=X, padx=5, pady=5, ipady=5)
        #
        # fcu_frame = Frame(fcu_labelframe, bg='#2f323b')
        # fcu_frame.pack(fill=X, padx=50, pady=20)
        #
        # fcu_label = Label(fcu_frame, text='통신 방식', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b')
        # fcu_label.pack(side=LEFT, padx=(0, 20))
        #
        # setting_Activity.fcu_combo = ttk.Combobox(fcu_frame, values=['Socket 통신', 'Modbus-TCP 통신', 'Modbus-RTU 통신'], font=('SCDream5', 15, 'bold'), state='readonly', justify='center')
        # self.option_add('*TCombobox*Listbox.font', ('SCDream5', 15, 'bold'))
        # setting_Activity.fcu_combo.bind('<<ComboboxSelected>>', self.fcu_selected)
        # setting_Activity.fcu_combo.pack(side=LEFT)
        #
        # setting_Activity.fcu_tcp_frame = Frame(fcu_labelframe, bg='#2f323b')
        # setting_Activity.fcu_tcp_frame.pack(fill=X, padx=(50, 0), pady=10)
        #
        # Label(setting_Activity.fcu_tcp_frame, text='IP', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)
        #
        # setting_Activity.fcu_entry1 = Entry(setting_Activity.fcu_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_entry1.pack(side=LEFT, padx=(10, 0))
        # setting_Activity.fcu_entry1.bind('<FocusIn>', self.insert_fcu_ip1)
        #
        # Label(setting_Activity.fcu_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)
        #
        # setting_Activity.fcu_entry2 = Entry(setting_Activity.fcu_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_entry2.pack(side=LEFT)
        # setting_Activity.fcu_entry2.bind('<FocusIn>', self.insert_fcu_ip2)
        #
        # Label(setting_Activity.fcu_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)
        #
        # setting_Activity.fcu_entry3 = Entry(setting_Activity.fcu_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_entry3.pack(side=LEFT)
        # setting_Activity.fcu_entry3.bind('<FocusIn>', self.insert_fcu_ip3)
        #
        # Label(setting_Activity.fcu_tcp_frame, text='.', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT, padx=3)
        #
        # setting_Activity.fcu_entry4 = Entry(setting_Activity.fcu_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_entry4.pack(side=LEFT)
        # setting_Activity.fcu_entry4.bind('<FocusIn>', self.insert_fcu_ip4)
        #
        # Label(setting_Activity.fcu_tcp_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold'), width=7, anchor='e').pack(side=LEFT, padx=(10,30))
        #
        # setting_Activity.fcu_entry5 = Entry(setting_Activity.fcu_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_entry5.pack(side=LEFT)
        # setting_Activity.fcu_entry5.bind('<FocusIn>', self.insert_fcu_port)
        #
        # fcu_apply = Button(setting_Activity.fcu_tcp_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용', command=lambda: self.fcu_apply_btn())
        # fcu_apply.pack(side=LEFT, padx=(30, 0))
        #
        # # fcu serial frame
        # setting_Activity.fcu_serial_frame = Frame(fcu_labelframe, bg='#2f323b')
        # setting_Activity.fcu_serial_frame.pack(fill=X, padx=(50, 0), pady=10)
        # # setting_Activity.fcu_serial_frame.pack_forget()
        #
        # Label(setting_Activity.fcu_serial_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)
        #
        # setting_Activity.fcu_serial_entry1 = Entry(setting_Activity.fcu_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_serial_entry1.pack(side=LEFT, padx=(10, 20))
        # setting_Activity.fcu_serial_entry1.bind('<FocusIn>', self.insert_fcu_serial1)
        #
        # Label(setting_Activity.fcu_serial_frame, text='BRATE', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)
        #
        # setting_Activity.fcu_serial_entry2 = Entry(setting_Activity.fcu_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_serial_entry2.pack(side=LEFT, padx=(10, 20))
        # setting_Activity.fcu_serial_entry2.bind('<FocusIn>', self.insert_fcu_serial2)
        #
        # Label(setting_Activity.fcu_serial_frame, text='PARITY', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)
        #
        # setting_Activity.fcu_serial_entry3 = Entry(setting_Activity.fcu_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_serial_entry3.pack(side=LEFT, padx=(10, 20))
        # setting_Activity.fcu_serial_entry3.bind('<FocusIn>', self.insert_fcu_serial3)
        #
        # Label(setting_Activity.fcu_serial_frame, text='STOPBIT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)
        #
        # setting_Activity.fcu_serial_entry4 = Entry(setting_Activity.fcu_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        # setting_Activity.fcu_serial_entry4.pack(side=LEFT, padx=(10, 0))
        # setting_Activity.fcu_serial_entry4.bind('<FocusIn>', self.insert_fcu_serial4)
        #
        # fcu_serial_apply = Button(setting_Activity.fcu_serial_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용',
        #                      command=lambda: self.fcu_serial_apply_btn())
        # fcu_serial_apply.pack(side=LEFT, padx=(30, 0))

        # communication canvas
        setting_frame = Frame(self, bg='#111111')
        setting_frame.pack(fill=BOTH, side=TOP, expand=True)

        setting_canvas = Canvas(setting_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=600)
        setting_canvas.pack(padx=15, fill=BOTH, expand=True, pady=15)

        setting_title_frame = Frame(setting_canvas, bg='#2f323b')
        setting_title_frame.pack(fill=X, pady=20)

        Label(setting_title_frame, text='시스템 설정', bg='#2f323b', fg='#96c63e', font=('SCDream5', 20, 'bold')).pack()

        setting_left_canvas = Canvas(setting_canvas, width=870, height=500, bg='#2f323b', highlightbackground='#2f323b')
        setting_left_canvas.pack(side=LEFT, fill=X, expand=True, ipadx=15, ipady=15)

        # setting_right_canvas = Canvas(setting_canvas, width=435, height=500, bg='#2f323b', highlightbackground='#2f323b')
        # setting_right_canvas.pack(side=RIGHT, fill=X, expand=True, ipadx=15, ipady=15)

        pvt_frame = Frame(setting_left_canvas, bg='#2f323b')
        pvt_frame.pack(fill=X, pady=(0, 20))

        pvt_title = Label(pvt_frame, text='태양광 용량(W)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=40, anchor='e')
        pvt_title.pack(side=LEFT, padx=(15, 0))

        setting_Activity.pvt_value = Entry(pvt_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        setting_Activity.pvt_value.pack(side=LEFT, padx=(20, 20))
        setting_Activity.pvt_value.bind('<FocusIn>', self.insert_pvt_value)

        pvt_btn = Button(pvt_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.pvt_value_btn())
        pvt_btn.pack(side=LEFT)

        load_frame = Frame(setting_left_canvas, bg='#2f323b')
        load_frame.pack(fill=X, pady=20)

        load_title = Label(load_frame, text='최대 부하 사용량(W)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=40, anchor='e')
        load_title.pack(side=LEFT, padx=(15, 0))

        setting_Activity.load_value = Entry(load_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        setting_Activity.load_value.pack(side=LEFT, padx=(20, 20))
        setting_Activity.load_value.bind('<FocusIn>', self.insert_load_value)

        load_btn = Button(load_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.load_value_btn())
        load_btn.pack(side=LEFT)

        insolation_frame = Frame(setting_left_canvas, bg='#2f323b')
        insolation_frame.pack(fill=X, pady=20)

        insolation_title = Label(insolation_frame, text='Fan 제어 일사량설정(W/m²)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=40, anchor='e')
        insolation_title.pack(side=LEFT, padx=(15, 0))

        setting_Activity.insolation_value = Entry(insolation_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        setting_Activity.insolation_value.pack(side=LEFT, padx=(20, 20))
        setting_Activity.insolation_value.bind('<FocusIn>', self.insert_insolation_value)

        insolation_btn = Button(insolation_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.insolation_value_btn())
        insolation_btn.pack(side=LEFT)

        damper_frame = Frame(setting_left_canvas, bg='#2f323b')
        damper_frame.pack(fill=X, pady=20)

        damper_title = Label(damper_frame, text='댐퍼 제어 온도설정(℃)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=40, anchor='e')
        damper_title.pack(side=LEFT, padx=(15, 0))

        setting_Activity.damper_value = Entry(damper_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        setting_Activity.damper_value.pack(side=LEFT, padx=(20, 20))
        setting_Activity.damper_value.bind('<FocusIn>', self.insert_damper_value)

        damper_btn = Button(damper_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.damper_value_btn())
        damper_btn.pack(side=LEFT)

        summer_heatpump_frame = Frame(setting_left_canvas, bg='#2f323b')
        summer_heatpump_frame.pack(fill=X, pady=20)

        summer_heatpump_title = Label(summer_heatpump_frame, text='하계 히트펌프 제어 온도설정(℃)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=40, anchor='e')
        summer_heatpump_title.pack(side=LEFT, padx=(15, 0))

        setting_Activity.summer_heatpump_value = Entry(summer_heatpump_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        setting_Activity.summer_heatpump_value.pack(side=LEFT, padx=(20, 20))
        setting_Activity.summer_heatpump_value.bind('<FocusIn>', self.insert_summer_heatpump_value)

        summer_heatpump_btn = Button(summer_heatpump_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.summer_heatpump_value_btn())
        summer_heatpump_btn.pack(side=LEFT)

        winter_heatpump_frame = Frame(setting_left_canvas, bg='#2f323b')
        winter_heatpump_frame.pack(fill=X, pady=20)

        winter_heatpump_title = Label(winter_heatpump_frame, text='동계 히트펌프 제어 온도설정(℃)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=40, anchor='e')
        winter_heatpump_title.pack(side=LEFT, padx=(15, 0))

        setting_Activity.winter_heatpump_value = Entry(winter_heatpump_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        setting_Activity.winter_heatpump_value.pack(side=LEFT, padx=(20, 20))
        setting_Activity.winter_heatpump_value.bind('<FocusIn>', self.insert_winter_heatpump_value)

        winter_heatpump_btn = Button(winter_heatpump_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.winter_heatpump_value_btn())
        winter_heatpump_btn.pack(side=LEFT)

        # cooling_frame = Frame(setting_right_canvas, bg='#2f323b')
        # cooling_frame.pack(fill=X, pady=20)
        #
        # cooling_title = Label(cooling_frame, text='냉방모드 온도설정(℃)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=17, anchor='e')
        # cooling_title.pack(side=LEFT, padx=(15, 0))
        #
        # setting_Activity.cooling_value = Entry(cooling_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        # setting_Activity.cooling_value.pack(side=LEFT, padx=(20, 20))
        # setting_Activity.cooling_value.bind('<FocusIn>', self.insert_cooling_value)
        #
        # cooling_btn = Button(cooling_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.cooling_value_btn())
        # cooling_btn.pack(side=LEFT)
        #
        # heating_frame = Frame(setting_right_canvas, bg='#2f323b')
        # heating_frame.pack(fill=X, pady=20)
        #
        # heating_title = Label(heating_frame, text='난방모드 온도설정(℃)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=17, anchor='e')
        # heating_title.pack(side=LEFT, padx=(15, 0))
        #
        # setting_Activity.heating_value = Entry(heating_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        # setting_Activity.heating_value.pack(side=LEFT, padx=(20, 20))
        # setting_Activity.heating_value.bind('<FocusIn>', self.insert_heating_value)
        #
        # heating_btn = Button(heating_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.heating_value_btn())
        # heating_btn.pack(side=LEFT)
        #
        # dhw_frame = Frame(setting_right_canvas, bg='#2f323b')
        # dhw_frame.pack(fill=X, pady=20)
        #
        # dhw_title = Label(dhw_frame, text='급탕모드 온도설정(℃)', font=('SCDream5', 15, 'bold'), fg='white', bg='#2f323b', width=17, anchor='e')
        # dhw_title.pack(side=LEFT, padx=(15, 0))
        #
        # setting_Activity.dhw_value = Entry(dhw_frame, font=('SCDream5', 20, 'bold',), justify='center', width=9)
        # setting_Activity.dhw_value.pack(side=LEFT, padx=(20, 20))
        # setting_Activity.dhw_value.bind('<FocusIn>', self.insert_dhw_value)
        #
        # dhw_btn = Button(dhw_frame, text='적 용', font=('SCDream5', 15, 'bold'), command=lambda :self.dhw_value_btn())
        # dhw_btn.pack(side=LEFT)
        #
        # empty_frame = Frame(setting_right_canvas, bg='#2f323b')
        # empty_frame.pack(fill=X, pady=20)
        #
        # empty_value = Label(empty_frame, text='', font=('SCDream5', 20, 'bold',), justify='center', width=9, bg='#2f323b')
        # empty_value.pack(side=LEFT, padx=(20, 20))


    # BIPVT TCP 통신 적용 버튼 클릭시
    def bipvt_apply_btn(self):
        if self.bipvt_entry1.get() == '' or self.bipvt_entry2.get() == '' or self.bipvt_entry3.get() == '' or self.bipvt_entry4.get() == '' or self.bipvt_entry5.get() == '':
            tkinter.messagebox.showwarning('설정오류', 'BIPVT 설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                set_ip = self.bipvt_entry1.get() + '.' + self.bipvt_entry2.get() + '.' + self.bipvt_entry3.get() + '.' + self.bipvt_entry4.get()
                set_data = [set_ip, self.bipvt_entry5.get()]
                db.sqlite_connect.protocol_update('bipvt', setting_Activity.bipvt_combo.get(), set_data)
                self.bipvt_client()

    # BIPVT Serial 통신 적용 버튼 클릭시
    def bipvt_serial_apply_btn(self):
        if self.bipvt_serial_entry1.get() == '' or self.bipvt_serial_entry2.get() == '' or self.bipvt_serial_entry3.get() == '' or self.bipvt_serial_entry4.get() == '':
            tkinter.messagebox.showwarning('설정오류', 'BIPVT 설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                set_port = self.bipvt_serial_entry1.get()
                set_brate = self.bipvt_serial_entry2.get()
                set_parity = self.bipvt_serial_entry3.get()
                set_stopbit = self.bipvt_serial_entry4.get()
                set_data = [set_port, set_brate, set_parity, set_stopbit]
                db.sqlite_connect.protocol_update('bipvt', setting_Activity.bipvt_combo.get(), set_data)
                self.bipvt_client()


    def heatpump_apply_btn(self):
        if self.heatpump_entry1.get() == '' or self.heatpump_entry2.get() == '' or self.heatpump_entry3.get() == '' or self.heatpump_entry4.get() == '' or self.heatpump_entry5.get() == '':
            tkinter.messagebox.showwarning('설정오류', '히트펌프 설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                set_ip = self.heatpump_entry1.get() + '.' + self.heatpump_entry2.get() + '.' + self.heatpump_entry3.get() + '.' + self.heatpump_entry4.get()
                set_data = [set_ip, self.heatpump_entry5.get()]
                db.sqlite_connect.protocol_update('heatpump', setting_Activity.heatpump_combo.get(), set_data)
                self.heatpump_client()

    def heatpump_serial_apply_btn(self):
        if self.heatpump_serial_entry1.get() == '' or self.heatpump_serial_entry2.get() == '' or self.heatpump_serial_entry3.get() == '' or self.heatpump_serial_entry4.get() == '':
            tkinter.messagebox.showwarning('설정오류', 'heatpump 설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                set_port = self.heatpump_serial_entry1.get()
                set_brate = self.heatpump_serial_entry2.get()
                set_parity = self.heatpump_serial_entry3.get()
                set_stopbit = self.heatpump_serial_entry4.get()
                set_data = [set_port, set_brate, set_parity, set_stopbit]
                db.sqlite_connect.protocol_update('heatpump', setting_Activity.heatpump_combo.get(), set_data)
                self.heatpump_client()

    def fcu_apply_btn(self):
        if self.fcu_entry1.get() == '' or self.fcu_entry2.get() == '' or self.fcu_entry3.get() == '' or self.fcu_entry4.get() == '' or self.fcu_entry5.get() == '':
            tkinter.messagebox.showwarning('설정오류', '히트펌프 설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                set_ip = self.fcu_entry1.get() + '.' + self.fcu_entry2.get() + '.' + self.fcu_entry3.get() + '.' + self.fcu_entry4.get()
                set_data = [set_ip, self.fcu_entry5.get()]
                db.sqlite_connect.protocol_update('fcu', setting_Activity.fcu_combo.get(), set_data)
                self.fcu_client()

    def fcu_serial_apply_btn(self):
        if self.fcu_serial_entry1.get() == '' or self.fcu_serial_entry2.get() == '' or self.fcu_serial_entry3.get() == '' or self.fcu_serial_entry4.get() == '':
            tkinter.messagebox.showwarning('설정오류', 'fcu 설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                set_port = self.fcu_serial_entry1.get()
                set_brate = self.fcu_serial_entry2.get()
                set_parity = self.fcu_serial_entry3.get()
                set_stopbit = self.fcu_serial_entry4.get()
                set_data = [set_port, set_brate, set_parity, set_stopbit]
                db.sqlite_connect.protocol_update('fcu', setting_Activity.fcu_combo.get(), set_data)
                self.fcu_client()

    def pvt_value_btn(self):
        if self.pvt_value.get() == '':
            tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                get_data = self.pvt_value.get()
                db.sqlite_connect.system_update('pvt', get_data)

    def insolation_value_btn(self):
        if self.insolation_value.get() == '':
            tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                get_data = self.insolation_value.get()
                db.sqlite_connect.system_update('insolation', get_data)

    def damper_value_btn(self):
        if self.damper_value.get() == '':
            tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                get_data = self.damper_value.get()
                db.sqlite_connect.system_update('damper', get_data)

    def load_value_btn(self):
        if self.load_value.get() == '':
            tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                get_data = self.load_value.get()
                db.sqlite_connect.system_update('load', get_data)

    def winter_heatpump_value_btn(self):
        if self.winter_heatpump_value.get() == '':
            tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                get_data = self.winter_heatpump_value.get()
                db.sqlite_connect.system_update('winter', get_data)

    def summer_heatpump_value_btn(self):
        if self.summer_heatpump_value.get() == '':
            tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                get_data = self.summer_heatpump_value.get()
                db.sqlite_connect.system_update('summer', get_data)

    # def cooling_value_btn(self):
    #     if self.cooling_value.get() == '':
    #         tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
    #     else:
    #         res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')
    #
    #         if res_msg:
    #             get_data = self.cooling_value.get()
    #             db.sqlite_connect.system_update('cooling', get_data)

    # def heating_value_btn(self):
    #     if self.heating_value.get() == '':
    #         tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
    #     else:
    #         res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')
    #
    #         if res_msg:
    #             get_data = self.heating_value.get()
    #             db.sqlite_connect.system_update('heating', get_data)

    # def dhw_value_btn(self):
    #     if self.dhw_value.get() == '':
    #         tkinter.messagebox.showwarning('설정오류', '설정값을 입력하세요')
    #     else:
    #         res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')
    #
    #         if res_msg:
    #             get_data = self.dhw_value.get()
    #             db.sqlite_connect.system_update('dhw', get_data)

    # 통신설정 변경시 BIPVT 클라이언트 재실행
    def bipvt_client(self):
        try:
            hosting = comd.var.bipvt_ip
            porting = int(comd.var.bipvt_port)

            comd.read_cmd.bipvt_client = ModbusTcpClient(hosting, porting)
            comd.read_cmd.bipvt_client.inter_char_timeout = 3
        except Exception as ex:
            print('bipvt_reclient() Exception -> ', ex)
            comd.var.bipvt_connect_status = False

    # 통신설정 변경시 히트펌프 클라이언트 재실행
    def heatpump_client(self):
        try:
            serial_porting = comd.var.heatpump_serial_port
            brate = comd.var.heatpump_brate
            parity = 'N'
            stopbit = comd.var.heatpump_stopbit

            comd.read_cmd.heatpump_client = ModbusSerialClient(method='rtu', port=serial_porting, baudrate=int(brate), stopbits=int(stopbit), parity=parity)
            comd.read_cmd.heatpump_client.inter_char_timeout = 3
        except Exception as ex:
            print('heatpump_reclient() Exception -> ', ex)
            comd.var.heatpump_connect_status = False

    def insert_pvt_value(self, event):
        notification.insert_keypad.put_pvt_value(self, '값 입력')
    def insert_insolation_value(self, event):
        notification.insert_keypad.put_insolation_value(self, '값 입력')
    def insert_damper_value(self, event):
        notification.insert_keypad.put_damper_value(self, '값 입력')
    def insert_load_value(self, event):
        notification.insert_keypad.put_load_value(self, '값 입력')
    def insert_cooling_value(self, event):
        notification.insert_keypad.put_cool_value(self, '값 입력')
    def insert_heating_value(self, event):
        notification.insert_keypad.put_hot_value(self, '값 입력')
    def insert_dhw_value(self, event):
        notification.insert_keypad.put_dhw_value(self, '값 입력')
    def insert_summer_heatpump_value(self, event):
        notification.insert_keypad.put_summer_heatpump_value(self, '값 입력')
    def insert_winter_heatpump_value(self, event):
        notification.insert_keypad.put_winter_heatpump_value(self, '값 입력')


    def insert_bipvt_ip1(self, event):
        notification.insert_keypad.put_bipvt_ip_value1(self, '값 입력')
    def insert_bipvt_ip2(self, event):
        notification.insert_keypad.put_bipvt_ip_value2(self, '값 입력')
    def insert_bipvt_ip3(self, event):
        notification.insert_keypad.put_bipvt_ip_value3(self, '값 입력')
    def insert_bipvt_ip4(self, event):
        notification.insert_keypad.put_bipvt_ip_value4(self, '값 입력')
    def insert_bipvt_port(self, event):
        notification.insert_keypad.put_bipvt_port_value(self, '값 입력')

    def insert_bipvt_serial1(self, event):
        notification.insert_keypad.put_bipvt_serial_value1(self, '값 입력')
    def insert_bipvt_serial2(self, event):
        notification.insert_keypad.put_bipvt_serial_value2(self, '값 입력')
    def insert_bipvt_serial3(self, event):
        notification.insert_keypad.put_bipvt_serial_value3(self, '값 입력')
    def insert_bipvt_serial4(self, event):
        notification.insert_keypad.put_bipvt_serial_value4(self, '값 입력')


    def insert_heatpump_ip1(self, event):
        notification.insert_keypad.put_heatpump_ip_value1(self, '값 입력')
    def insert_heatpump_ip2(self, event):
        notification.insert_keypad.put_heatpump_ip_value2(self, '값 입력')
    def insert_heatpump_ip3(self, event):
        notification.insert_keypad.put_heatpump_ip_value3(self, '값 입력')
    def insert_heatpump_ip4(self, event):
        notification.insert_keypad.put_heatpump_ip_value4(self, '값 입력')
    def insert_heatpump_port(self, event):
        notification.insert_keypad.put_heatpump_port_value(self, '값 입력')

    def insert_heatpump_serial1(self, event):
        notification.insert_keypad.put_heatpump_serial_value1(self, '값 입력')
    def insert_heatpump_serial2(self, event):
        notification.insert_keypad.put_heatpump_serial_value2(self, '값 입력')
    def insert_heatpump_serial3(self, event):
        notification.insert_keypad.put_heatpump_serial_value3(self, '값 입력')
    def insert_heatpump_serial4(self, event):
        notification.insert_keypad.put_heatpump_serial_value4(self, '값 입력')

    def insert_fcu_ip1(self, event):
        notification.insert_keypad.put_fcu_ip_value1(self, '값 입력')
    def insert_fcu_ip2(self, event):
        notification.insert_keypad.put_fcu_ip_value2(self, '값 입력')
    def insert_fcu_ip3(self, event):
        notification.insert_keypad.put_fcu_ip_value3(self, '값 입력')
    def insert_fcu_ip4(self, event):
        notification.insert_keypad.put_fcu_ip_value4(self, '값 입력')
    def insert_fcu_port(self, event):
        notification.insert_keypad.put_fcu_port_value(self, '값 입력')

    def insert_fcu_serial1(self, event):
        notification.insert_keypad.put_fcu_serial_value1(self, '값 입력')
    def insert_fcu_serial2(self, event):
        notification.insert_keypad.put_fcu_serial_value2(self, '값 입력')
    def insert_fcu_serial3(self, event):
        notification.insert_keypad.put_fcu_serial_value3(self, '값 입력')
    def insert_fcu_serial4(self, event):
        notification.insert_keypad.put_fcu_serial_value4(self, '값 입력')

    # BIPVT 통신 설정
    def bipvt_selected(self, event):
        if setting_Activity.bipvt_combo.get() == 'Socket 통신' or setting_Activity.bipvt_combo.get() == 'Modbus-TCP 통신':
            setting_Activity.bipvt_serial_frame.pack_forget()
            setting_Activity.bipvt_tcp_frame.pack(fill=X, padx=(50, 0), pady=10)
        else:
            setting_Activity.bipvt_tcp_frame.pack_forget()
            setting_Activity.bipvt_serial_frame.pack(fill=X, padx=(50, 0), pady=10)

    # 히트펌프 통신 설정
    def heatpump_selected(self, event):
        if setting_Activity.heatpump_combo.get() == 'Socket 통신' or setting_Activity.heatpump_combo.get() == 'Modbus-TCP 통신':
            setting_Activity.heatpump_serial_frame.pack_forget()
            setting_Activity.heatpump_tcp_frame.pack(fill=X, padx=(50, 0), pady=10)
        else:
            setting_Activity.heatpump_tcp_frame.pack_forget()
            setting_Activity.heatpump_serial_frame.pack(fill=X, padx=(50, 0), pady=10)

    # FCU 통신 설정
    def fcu_selected(self, event):
        if setting_Activity.fcu_combo.get() == 'Socket 통신' or setting_Activity.fcu_combo.get() == 'Modbus-TCP 통신':
            setting_Activity.fcu_serial_frame.pack_forget()
            setting_Activity.fcu_tcp_frame.pack(fill=X, padx=(50, 0), pady=10)
        else:
            setting_Activity.fcu_tcp_frame.pack_forget()
            setting_Activity.fcu_serial_frame.pack(fill=X, padx=(50, 0), pady=10)
