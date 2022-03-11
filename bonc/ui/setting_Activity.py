import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog
import tkinter.messagebox
from time import sleep
from pymodbus.client.sync import ModbusTcpClient
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

        setting_Activity.weather_value = Label(title_frame, text='맑음', highlightbackground='#111111',
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

        above1_value = Label(above1_frame, text=' 79514.3 ', fg='#CFDD8E', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        above1_value.pack(fill=X, pady=10)

        above1_unit = Label(above1_frame, text='kW', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above1_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above2_frame = Frame(setting_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above2_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(15, 0))

        above2_title = Label(above2_frame, text='누적 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above2_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        above2_value = Label(above2_frame, text=' 7979842.7 ', fg='#6ECEDA', bg='#2f323b',
                             font=('SCDream5', 25, 'bold'))
        above2_value.pack(fill=X, pady=10)

        above2_unit = Label(above2_frame, text='kW', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above2_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above3_frame = Frame(setting_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above3_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=15)

        above3_title = Label(above3_frame, text='일일 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above3_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        above3_value = Label(above3_frame, text=' 749843.4 ', fg='#B97687', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        above3_value.pack(fill=X, pady=10)

        above3_unit = Label(above3_frame, text='kW', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above3_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above4_frame = Frame(setting_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above4_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above4_title = Label(above4_frame, text='누적 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above4_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        above4_value = Label(above4_frame, text=' 498736.75 ', fg='#d18063', bg='#2f323b',
                             font=('SCDream5', 25, 'bold'))
        above4_value.pack(fill=X, pady=10)

        above4_unit = Label(above4_frame, text='kW', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above4_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        # communication canvas
        communication_frame = Frame(self, bg='#111111')
        communication_frame.pack(fill=BOTH, side=TOP, expand=True)

        setting_Activity.communication_canvas = Canvas(communication_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=500)
        setting_Activity.communication_canvas.pack(fill=X, padx=15, pady=15)

        communication_title_frame = Frame(setting_Activity.communication_canvas, bg='#2f323b')
        communication_title_frame.pack(fill=X, expand=True)

        communication_title = Label(communication_title_frame, text='통신 설정', font=('SCDream5', 20, 'bold'), fg='#23A96E', bg='#2f323b')
        communication_title.pack()

        # fake_keyboard = Button(setting_Activity.communication_canvas, bg='red', width=50, bd=0, activebackground='#2F323B', command=lambda :self.sys_keyboard())
        # fake_keyboard.place(x=950, y=0)

        bipvt_frame = Frame(setting_Activity.communication_canvas, bg='#2f323b')
        bipvt_frame.pack(fill=X, padx=50, pady=(40, 20))

        bipvt_label = Label(bipvt_frame, text='BIPVT 통신 설정', font=('SCDream5', 20, 'bold'), fg='white', bg='#2f323b')
        bipvt_label.pack(side=LEFT, padx=(0, 20))

        setting_Activity.bipvt_combo = ttk.Combobox(bipvt_frame, values=['Socket 통신', 'Modbus-TCP 통신', 'Modbus-RTU 통신'], font=('SCDream5', 20, 'bold'), state='readonly')
        self.option_add('*TCombobox*Listbox.font', ('SCDream5', 15, 'bold'))
        setting_Activity.bipvt_combo.bind('<<ComboboxSelected>>', self.bipvt_selected)
        setting_Activity.bipvt_combo.pack(side=LEFT)

        setting_Activity.bipvt_tcp_frame = Frame(setting_Activity.communication_canvas, bg='#2f323b')
        setting_Activity.bipvt_tcp_frame.pack(fill=X, padx=(50, 0), pady=10)

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

        Label(setting_Activity.bipvt_tcp_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold'), width=7, anchor='e').pack(side=LEFT, padx=(20,30))

        setting_Activity.bipvt_entry5 = Entry(setting_Activity.bipvt_tcp_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_entry5.pack(side=LEFT)
        setting_Activity.bipvt_entry5.bind('<FocusIn>', self.insert_bipvt_port)

        bipvt_apply = Button(setting_Activity.bipvt_tcp_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용', command=lambda: self.bipvt_apply_btn())
        bipvt_apply.pack(side=LEFT, padx=30)

        # bipvt serial frame
        setting_Activity.bipvt_serial_frame = Frame(setting_Activity.communication_canvas, bg='#2f323b')
        setting_Activity.bipvt_serial_frame.pack(fill=X, padx=(50, 0), pady=10)

        Label(setting_Activity.bipvt_serial_frame, text='PORT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry1 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry1.pack(side=LEFT, padx=(10, 30))
        setting_Activity.bipvt_serial_entry1.bind('<FocusIn>', self.insert_bipvt_serial1)

        Label(setting_Activity.bipvt_serial_frame, text='BRATE', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry2 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry2.pack(side=LEFT, padx=(10, 30))
        setting_Activity.bipvt_serial_entry2.bind('<FocusIn>', self.insert_bipvt_serial2)

        Label(setting_Activity.bipvt_serial_frame, text='PARITY', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry3 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry3.pack(side=LEFT, padx=(10, 30))
        setting_Activity.bipvt_serial_entry3.bind('<FocusIn>', self.insert_bipvt_serial3)

        Label(setting_Activity.bipvt_serial_frame, text='STOPBIT', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold')).pack(side=LEFT)

        setting_Activity.bipvt_serial_entry4 = Entry(setting_Activity.bipvt_serial_frame, bg='white', fg='#2E2F31', font=('SCDream5', 15, 'bold'), width=8, justify='center')
        setting_Activity.bipvt_serial_entry4.pack(side=LEFT, padx=(10, 0))
        setting_Activity.bipvt_serial_entry4.bind('<FocusIn>', self.insert_bipvt_serial4)

        bipvt_serial_apply = Button(setting_Activity.bipvt_serial_frame, font=('SCDream5', 15, 'bold'), width=6, text='적용',
                             command=lambda: self.bipvt_serial_apply_btn())
        bipvt_serial_apply.pack(side=LEFT, padx=30)

    #     # left frame
    #     center_frame = Frame(self, bg='#2f323b')
    #     center_frame.pack(fill=BOTH, side=TOP, expand=True)
    #
    #     label1 = Label(center_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     # 내부 Frame
    #     top_set_contents_frame = Frame(center_frame, bg="#2f323b")
    #     top_set_contents_frame.pack(side=TOP, ipadx=30, ipady=20, fill=BOTH, padx=10)
    #
    #     system_title_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     system_title_frame.pack(fill=X)
    #
    #     system_title_label = Label(system_title_frame, bg='#2f323b', text='시스템 설정', font=('arial', 15, 'bold'), fg='#23A96E')
    #     system_title_label.pack()
    #
    #     # system_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     # system_frame.pack(fill=X)
    #
    #     setting_apply = Button(system_title_frame, font=('arial', 13), text='적용', command=lambda: self.system_apply_btn())
    #     setting_apply.place(x=980, y=0)
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     set1_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     set1_frame.pack(pady=5)
    #
    #     insolation_text = Label(set1_frame, width=20, text='BIPVT 조도 ', font=('arial', 15), anchor='e', fg='white', bg='#2f323b')
    #     insolation_text.pack(side=LEFT)
    #
    #     setting_Activity.insolation_value = Entry(set1_frame, width=15, textvariable=str, font=('arial', 15), justify='center')
    #     setting_Activity.insolation_value.pack(side=LEFT)
    #     setting_Activity.insolation_value.bind('<FocusIn>', self.insert_insolation_value)
    #
    #     insolation_unit = Label(set1_frame, width=7, text=' W/m³ ', font=('arial', 15), bg='#2f323b', fg='white')
    #     insolation_unit.pack(side=LEFT)
    #
    #     bipvt_inner_temp_text = Label(set1_frame, width=20, text='BIPVT 입구온도 ', font=('arial', 15), anchor='e', fg='white', bg='#2f323b')
    #     bipvt_inner_temp_text.pack(side=LEFT)
    #
    #     setting_Activity.bipvt_inner_temp_value = Entry(set1_frame, width=15, textvariable=str, font=('arial', 15), justify='center')
    #     setting_Activity.bipvt_inner_temp_value.pack(side=LEFT)
    #     setting_Activity.bipvt_inner_temp_value.bind('<FocusIn>', self.insert_bipvt_inner_temp_value)
    #
    #     bipvt_inner_temp_unit = Label(set1_frame, width=7, text=' ℃ ', font=('arial', 15), bg='#2f323b', fg='white')
    #     bipvt_inner_temp_unit.pack(side=LEFT)
    #
    #     set2_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     set2_frame.pack(pady=5)
    #
    #     cool_text = Label(set2_frame, width=20, text='냉방온도 ', font=('arial', 15), anchor='e', fg='white', bg='#2f323b')
    #     cool_text.pack(side=LEFT)
    #
    #     setting_Activity.cool_value = Entry(set2_frame, width=15, textvariable=str, font=('arial', 15), justify='center')
    #     setting_Activity.cool_value.pack(side=LEFT)
    #     setting_Activity.cool_value.bind('<FocusIn>', self.insert_cool_value)
    #
    #     cool_unit = Label(set2_frame, width=7, text=' ℃ ', font=('arial', 15), bg='#2f323b', fg='white')
    #     cool_unit.pack(side=LEFT)
    #
    #     hot_text = Label(set2_frame, width=20, text='난방온도 ', font=('arial', 15), anchor='e', fg='white', bg='#2f323b')
    #     hot_text.pack(side=LEFT)
    #
    #     setting_Activity.hot_value = Entry(set2_frame, width=15, textvariable=str, font=('arial', 15), justify='center')
    #     setting_Activity.hot_value.pack(side=LEFT)
    #     setting_Activity.hot_value.bind('<FocusIn>', self.insert_hot_value)
    #
    #     hot_unit = Label(set2_frame, width=7, text=' ℃ ', font=('arial', 15), bg='#2f323b', fg='white')
    #     hot_unit.pack(side=LEFT)
    #
    #     set3_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     set3_frame.pack(pady=5)
    #
    #     dhw_text = Label(set3_frame, width=20, text='급탕온도 ', font=('arial', 15), anchor='e', fg='white', bg='#2f323b')
    #     dhw_text.pack(side=LEFT)
    #
    #     setting_Activity.dhw_value = Entry(set3_frame, width=15, textvariable=str, font=('arial', 15), justify='center')
    #     setting_Activity.dhw_value.pack(side=LEFT)
    #     setting_Activity.dhw_value.bind('<FocusIn>', self.insert_dhw_value)
    #
    #     dhw_unit = Label(set3_frame, width=7, text=' ℃ ', font=('arial', 15), bg='#2f323b', fg='white')
    #     dhw_unit.pack(side=LEFT)
    #
    #     doublecoil_text = Label(set3_frame, width=20, text='이중코일 동작온도 ', font=('arial', 15), anchor='e', fg='white', bg='#2f323b')
    #     doublecoil_text.pack(side=LEFT)
    #
    #     setting_Activity.doublecoil_value = Entry(set3_frame, width=15, textvariable=str, font=('arial', 15), justify='center')
    #     setting_Activity.doublecoil_value.pack(side=LEFT)
    #     setting_Activity.doublecoil_value.bind('<FocusIn>', self.insert_doublecoil_value)
    #
    #     doublecoil_unit = Label(set3_frame, width=7, text=' ℃ ', font=('arial', 15), bg='#2f323b', fg='white')
    #     doublecoil_unit.pack(side=LEFT)
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     title_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     title_frame.pack(fill=X)
    #
    #     title_label = Label(title_frame, bg='#2f323b', text='통신 설정', font=('arial', 15, 'bold'), fg='#23A96E')
    #     title_label.pack()
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     # BMS 통신 설정
    #     bipvt_label_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     bipvt_label_frame.pack(fill=X, padx=50)
    #
    #     bipvt_label = Label(bipvt_label_frame, bg='#2f323b', fg='white', font=('arial', 15, 'bold'),
    #                       text='BIPVT', width=15, anchor='w')
    #     bipvt_label.pack(side=LEFT)
    #
    #     Label(bipvt_label_frame, text='IP', bg='#2f323b', fg='white', font=('arial', 15, 'bold')).pack(side=LEFT)
    #
    #     setting_Activity.bipvt_entry1 = Entry(bipvt_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.bipvt_entry1.pack(side=LEFT, padx=(30, 0))
    #     setting_Activity.bipvt_entry1.bind('<FocusIn>', self.insert_bipvt_ip1)
    #
    #     Label(bipvt_label_frame, text='.', bg='#2f323b', fg='white', font=('arial', 15)).pack(side=LEFT, padx=3)
    #
    #     setting_Activity.bipvt_entry2 = Entry(bipvt_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.bipvt_entry2.pack(side=LEFT)
    #     setting_Activity.bipvt_entry2.bind('<FocusIn>', self.insert_bipvt_ip2)
    #
    #     Label(bipvt_label_frame, text='.', bg='#2f323b', fg='white', font=('arial', 15)).pack(side=LEFT, padx=3)
    #
    #     setting_Activity.bipvt_entry3 = Entry(bipvt_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.bipvt_entry3.pack(side=LEFT)
    #     setting_Activity.bipvt_entry3.bind('<FocusIn>', self.insert_bipvt_ip3)
    #
    #     Label(bipvt_label_frame, text='.', bg='#2f323b', fg='white', font=('arial', 15)).pack(side=LEFT, padx=3)
    #
    #     setting_Activity.bipvt_entry4 = Entry(bipvt_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.bipvt_entry4.pack(side=LEFT)
    #     setting_Activity.bipvt_entry4.bind('<FocusIn>', self.insert_bipvt_ip4)
    #
    #     Label(bipvt_label_frame, text='PORT', bg='#2f323b', fg='white', font=('arial', 15, 'bold'), width=7, anchor='e').pack(side=LEFT, padx=(20,30))
    #
    #     setting_Activity.bipvt_entry5 = Entry(bipvt_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.bipvt_entry5.pack(side=LEFT)
    #     setting_Activity.bipvt_entry5.bind('<FocusIn>', self.insert_bipvt_port)
    #
    #     bipvt_apply = Button(bipvt_label_frame, font=('arial', 15), text='적용', command=lambda: self.bipvt_apply_btn())
    #     bipvt_apply.pack(side=LEFT, padx=30)
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     # heatpump 통신 설정
    #     heatpump_label_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     heatpump_label_frame.pack(fill=X, padx=50)
    #
    #     heatpump_label = Label(heatpump_label_frame, bg='#2f323b', fg='white', font=('arial', 15, 'bold'),
    #                       text='HeatPump', width=15, anchor='w')
    #     heatpump_label.pack(side=LEFT)
    #
    #     Label(heatpump_label_frame, text='IP', bg='#2f323b', fg='white', font=('arial', 15, 'bold')).pack(side=LEFT)
    #
    #     setting_Activity.heatpump_entry1 = Entry(heatpump_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.heatpump_entry1.pack(side=LEFT, padx=(30, 0))
    #     setting_Activity.heatpump_entry1.bind('<FocusIn>', self.insert_heatpump_ip1)
    #
    #     Label(heatpump_label_frame, text='.', bg='#2f323b', fg='white', font=('arial', 15)).pack(side=LEFT, padx=3)
    #
    #     setting_Activity.heatpump_entry2 = Entry(heatpump_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.heatpump_entry2.pack(side=LEFT)
    #     setting_Activity.heatpump_entry2.bind('<FocusIn>', self.insert_heatpump_ip2)
    #
    #     Label(heatpump_label_frame, text='.', bg='#2f323b', fg='white', font=('arial', 15)).pack(side=LEFT, padx=3)
    #
    #     setting_Activity.heatpump_entry3 = Entry(heatpump_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.heatpump_entry3.pack(side=LEFT)
    #     setting_Activity.heatpump_entry3.bind('<FocusIn>', self.insert_heatpump_ip3)
    #
    #     Label(heatpump_label_frame, text='.', bg='#2f323b', fg='white', font=('arial', 15)).pack(side=LEFT, padx=3)
    #
    #     setting_Activity.heatpump_entry4 = Entry(heatpump_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.heatpump_entry4.pack(side=LEFT)
    #     setting_Activity.heatpump_entry4.bind('<FocusIn>', self.insert_heatpump_ip4)
    #
    #     Label(heatpump_label_frame, text='PORT', bg='#2f323b', fg='white', font=('arial', 15, 'bold'), width=7, anchor='e').pack(side=LEFT, padx=(20,30))
    #
    #     setting_Activity.heatpump_entry5 = Entry(heatpump_label_frame, bg='white', fg='#2E2F31', font=('arial', 15), width=8, justify='center')
    #     setting_Activity.heatpump_entry5.pack(side=LEFT)
    #     setting_Activity.heatpump_entry5.bind('<FocusIn>', self.insert_heatpump_port)
    #
    #     heatpump_apply = Button(heatpump_label_frame, font=('arial', 15), text='적용', command=lambda: self.heatpump_apply_btn())
    #     heatpump_apply.pack(side=LEFT, padx=30)
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     # Downloads
    #     down_title_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     down_title_frame.pack(fill=X)
    #
    #     down_title_label = Label(down_title_frame, bg='#2f323b', text='매뉴얼 다운로드', font=('arial', 15, 'bold'), fg='#23A96E')
    #     down_title_label.pack()
    #
    #     label1 = Label(top_set_contents_frame, bg='#2f323b')
    #     label1.pack()
    #
    #     down_frame = Frame(top_set_contents_frame, bg='#2f323b')
    #     down_frame.pack()
    #
    #     catalog_btn = Button(down_frame, text='카탈로그\n다운로드', width=15,  fg='white', bg='#96c63e', font=('arial', 20, 'bold'), command=lambda : self.file_downloading("스마트그리드제어시스템v1.0_카탈로그.pdf"))
    #     catalog_btn.pack(side=LEFT, padx=(0, 50))
    #
    #     manual_btn = Button(down_frame, text='사용자취급설명서\n다운로드', width=15, fg='white', bg='#007ad1', font=('arial', 20, 'bold'), command=lambda : self.file_downloading("스마트그리드제어시스템v1.0_사용자취급설명서.pdf"))
    #     manual_btn.pack(side=LEFT)
    #
    #
    # def bipvt_apply_btn(self):
    #     if self.bipvt_entry1.get() == '' or self.bipvt_entry2.get() == '' or self.bipvt_entry3.get() == '' or self.bipvt_entry4.get() == '' or self.bipvt_entry5.get() == '':
    #         tkinter.messagebox.showwarning('설정오류', 'BIPVT 설정값을 입력하세요')
    #     else:
    #         res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')
    #
    #         if res_msg:
    #             set_ip = self.bipvt_entry1.get() + '.' +self.bipvt_entry2.get() + '.' +self.bipvt_entry3.get() + '.' +self.bipvt_entry4.get()
    #             db.sqlite_connect.protocol_update('bipvt_ip', 'bipvt_port', set_ip, self.bipvt_entry5.get())
    #             self.bipvt_client()


    # def bipvt_serial_apply_btn(self):
    #     if self.bipvt_serial_entry1.get() == '' or self.bipvt_serial_entry2.get() == '' or self.bipvt_serial_entry3.get() == '' or self.bipvt_serial_entry4.get():
    #         tkinter.messagebox.showwarning('설정오류', 'BIPVT 설정값을 입력하세요')
    #     else:
    #         res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')
    #
    #         if res_msg:
    #             set_ip = self.bipvt_entry1.get() + '.' +self.bipvt_entry2.get() + '.' +self.bipvt_entry3.get() + '.' +self.bipvt_entry4.get()
    #             db.sqlite_connect.protocol_update('bipvt_ip', 'bipvt_port', set_ip, self.bipvt_entry5.get())
    #             self.bipvt_client()
    #
    #
    # def heatpump_apply_btn(self):
    #     if self.heatpump_entry1.get() == '' or self.heatpump_entry2.get() == '' or self.heatpump_entry3.get() == '' or self.heatpump_entry4.get() == '' or self.heatpump_entry5.get() == '':
    #         tkinter.messagebox.showwarning('설정오류', '히트펌프 설정값을 입력하세요')
    #     else:
    #         res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')
    #
    #         if res_msg:
    #             set_ip = self.heatpump_entry1.get() + '.' + self.heatpump_entry2.get() + '.' + self.heatpump_entry3.get() + '.' + self.heatpump_entry4.get()
    #             db.sqlite_connect.protocol_update('heatpump_ip', 'heatpump_port', set_ip, self.heatpump_entry5.get())
    #             self.heatpump_client()
    #
    #
    # def system_apply_btn(self):
    #     if self.insolation_value.get() == '' or self.bipvt_inner_temp_value.get() == '' or self.cool_value.get() == '' or self.hot_value.get() == '' or self.dhw_value.get() == '' or self.doublecoil_value.get() == '':
    #         tkinter.messagebox.showwarning('설정오류', '시스템 설정값을 입력하세요')
    #     else:
    #         res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')
    #
    #         if res_msg:
    #             db.sqlite_connect.system_update(self.insolation_value.get(), self.bipvt_inner_temp_value.get(),self.cool_value.get(), self.hot_value.get(), self.dhw_value.get(), self.doublecoil_value.get())
    #
    #
    #
    # def bipvt_client(self):
    #     try:
    #         hosting = comd.var.bipvt_ip
    #         porting = int(comd.var.bipvt_port)
    #
    #         comd.read_cmd.bipvt_client = ModbusTcpClient(hosting, porting)
    #         comd.read_cmd.bipvt_client.inter_char_timeout = 3
    #     except Exception as ex:
    #         print('bipvt_reclient() Exception -> ', ex)
    #         comd.var.bipvt_connect_status = False
    #
    #
    # def heatpump_client(self):
    #     try:
    #         hosting = comd.var.heatpump_ip
    #         porting = int(comd.var.heatpump_port)
    #
    #         comd.read_cmd.heatpump_client = ModbusTcpClient(hosting, porting)
    #         comd.read_cmd.heatpump_client.inter_char_timeout = 3
    #     except Exception as ex:
    #         print('heatpump_reclinet() Exception -> ', ex)
    #         comd.var.heatpump_connect_status = False
    #
    # def insert_insolation_value(self, event):
    #     notification.insert_keypad.put_insolation_value(self, '값 입력')
    # def insert_bipvt_inner_temp_value(self, event):
    #     notification.insert_keypad.put_bipvt_inner_temp_value(self, '값 입력')
    # def insert_cool_value(self, event):
    #     notification.insert_keypad.put_cool_value(self, '값 입력')
    # def insert_hot_value(self, event):
    #     notification.insert_keypad.put_hot_value(self, '값 입력')
    # def insert_dhw_value(self, event):
    #     notification.insert_keypad.put_dhw_value(self, '값 입력')
    # def insert_doublecoil_value(self, event):
    #     notification.insert_keypad.put_doublecoil_value(self, '값 입력')
    #
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


    # def insert_heatpump_ip1(self, event):
    #     notification.insert_keypad.put_heatpump_ip_value1(self, '값 입력')
    # def insert_heatpump_ip2(self, event):
    #     notification.insert_keypad.put_heatpump_ip_value2(self, '값 입력')
    # def insert_heatpump_ip3(self, event):
    #     notification.insert_keypad.put_heatpump_ip_value3(self, '값 입력')
    # def insert_heatpump_ip4(self, event):
    #     notification.insert_keypad.put_heatpump_ip_value4(self, '값 입력')
    # def insert_heatpump_port(self, event):
    #     notification.insert_keypad.put_heatpump_port_value(self, '값 입력')
    #
    # def file_downloading(self, menu):
    #     print(menu)
    #     try:
    #         import subprocess
    #
    #         if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    #             setDir = '/media/ubuntu'
    #             cmd = 'grep /bin/bash /etc/passwd'
    #             cmd2 = 'cut -f1 -d:'
    #
    #             userName = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    #             userName2 = subprocess.Popen(cmd2.split(), stdin=userName.stdout, stdout=subprocess.PIPE)
    #             user = userName2.stdout.read()
    #             user = user.decode('utf-8')
    #             print('userName : ', user)
    #
    #             flash = subprocess.check_output(['ls', setDir])
    #             flash = flash.decode('utf-8').replace('\n', '')
    #             print(flash)
    #
    #             # USB가 꽂혀 있을경우
    #             if not flash == '':
    #                 print('USB is Founded')
    #                 getTems = subprocess.check_output(['ls', '%s/%s/' % (setDir, flash)])
    #                 listTems = getTems.decode('utf-8').split('\n')
    #                 print(listTems)
    #
    #                 if 'TEMS' not in listTems:
    #                     os.system('sudo mkdir %s/%s/TEMS' % (setDir, flash))
    #                     print('Make Dir TEMS')
    #                 else:
    #                     print('TEMS is EXIST')
    #
    #                 os.system('sudo cp /home/ubuntu/bipvt/smart_grid_v1/%s %s/%s/tems/' % (menu, setDir, flash))
    #                 print('File Copy Finished')
    #                 tkinter.messagebox.showinfo('USB 저장완료', 'USB에 다운로드가 완료되었습니다.\nTEMS 폴더를 확인하세요.')
    #
    #             # USB is Not Found
    #             else:
    #                 print('USB is Not Founded')
    #                 tkinter.messagebox.showwarning('USB 인식오류', 'USB 연결상태를 확인하세요')
    #         else:
    #             print('Windows 미지원')
    #     except Exception as ex:
    #         print('USB Down ERROR >> ', ex)

    def bipvt_selected(self, event):
        if setting_Activity.bipvt_combo.get() == 'Socket 통신' or setting_Activity.bipvt_combo.get() == 'Modbus-TCP 통신':
            setting_Activity.bipvt_serial_frame.pack_forget()
            setting_Activity.bipvt_tcp_frame.pack(pady=10)
        else:
            setting_Activity.bipvt_tcp_frame.pack_forget()
            setting_Activity.bipvt_serial_frame.pack(pady=10)
