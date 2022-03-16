import os, sys
import datetime

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter as tk
from tkinter.tix import *
import tkinter.simpledialog
import tkinter.messagebox
from PIL import ImageTk, Image

import notification.insert_keypad
import db.sqlite_connect
import ui.run_Activity
import ui.error_Activity

import comd.var


def now_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now


def run_len():
    cnt = db.sqlite_connect.run_count()
    return cnt


class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text, set_x):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + set_x
        y = y + cy + self.widget.winfo_rooty() + 33
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "13", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text, set_x):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text, set_x)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class control_Activity(tk.Frame):
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
        control_Activity.gps_menu = Label(title_frame, image=self.gps_image, highlightbackground='#111111',
                                       activebackground='#111111', bd=0, bg='#111111')
        control_Activity.gps_menu.pack(side=LEFT, padx=(0, 10), pady=(8, 0))

        weather_menu = Label(title_frame, text='날씨', highlightbackground='#111111', activebackground='#111111', bd=0,
                             bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        weather_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        weather_img = Image.open('images/weather/01d.png')
        weather_img = weather_img.resize((40, 40), Image.ANTIALIAS)
        self.weather_image = ImageTk.PhotoImage(weather_img)
        control_Activity.weather_value = Label(title_frame, highlightbackground='#111111', image=self.weather_image,
                                            activebackground='#111111', bd=0, bg='#111111',
                                            font=('SCDream5', 16, 'bold'),
                                            fg='white')
        control_Activity.weather_value.pack(side=LEFT, pady=(8, 0))

        temperature_menu = Label(title_frame, text='| 기온', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_menu.pack(side=LEFT, padx=(10, 10), pady=(8, 0))

        control_Activity.temperature_value = Label(title_frame, text='32.5', highlightbackground='#111111',
                                                activebackground='#111111', bd=0, bg='#111111',
                                                font=('SCDream5', 16, 'bold'),
                                                fg='white')
        control_Activity.temperature_value.pack(side=LEFT, pady=(8, 0))

        temperature_unit = Label(title_frame, text=' ℃', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_unit.pack(side=LEFT, pady=(8, 0))

        humi_menu = Label(title_frame, text='| 습도', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        control_Activity.humi_value = Label(title_frame, text='44.3', highlightbackground='#111111',
                                         activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                         fg='white')
        control_Activity.humi_value.pack(side=LEFT, pady=(8, 0))

        humi_unit = Label(title_frame, text='%', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_unit.pack(side=LEFT, pady=(8, 0))

        control_Activity.time_label2 = Label(title_frame, text='-', highlightbackground='#111111',
                                          activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 18, 'bold'),
                                          fg='#96c63e')
        control_Activity.time_label2.pack(side=RIGHT, padx=(10, 30), pady=(8, 0))

        control_Activity.time_label1 = Label(title_frame, text='-', highlightbackground='#111111',
                                          activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 18, 'bold'),
                                          fg='white')
        control_Activity.time_label1.pack(side=RIGHT, pady=(8, 0))

        self.date_image = tk.PhotoImage(file='images/date.png')
        date_menu = Label(title_frame, image=self.date_image, highlightbackground='#111111', activebackground='#111111',
                          bd=0, bg='#111111')
        date_menu.pack(side=RIGHT, padx=(0, 5), pady=(8, 0))

        ########################### 메뉴 버튼 ###############################
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, side=TOP, ipady=10)

        self.main_image = tk.PhotoImage(file='images/main_btn_off.png')
        self.control_image = tk.PhotoImage(file='images/control_btn.png')
        self.setting_image = tk.PhotoImage(file='images/setting_btn_off.png')
        self.detail_image = tk.PhotoImage(file='images/detail_btn_off.png')

        main_menu = Button(menu_frame, image=self.main_image, highlightbackground='#111111', activebackground='#111111',
                           bd=0, bg='#111111', command=lambda: controller.show_frame('main_Activity'))
        main_menu.pack(side=LEFT, anchor=CENTER, expand=True)

        control_menu = Button(menu_frame, image=self.control_image, highlightbackground='#111111',
                              activebackground='#111111', bd=0, bg='#111111',
                              command=lambda: controller.show_frame('control_Activity_sub'))
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
        control_Activity.top_canvas = Canvas(top_frame, bg='#111111', highlightbackground='#111111', width=870, height=200)
        control_Activity.top_canvas.pack(padx=15, fill=X, pady=(15, 0))

        above1_frame = Frame(control_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above1_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above1_title = Label(above1_frame, text='일일 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above1_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        above1_value = Label(above1_frame, text=' 79514.3 ', fg='#CFDD8E', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        above1_value.pack(fill=X, pady=10)

        above1_unit = Label(above1_frame, text='kW', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above1_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above2_frame = Frame(control_Activity.top_canvas, bg='#2f323b', height=180, width=250)
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

        above3_frame = Frame(control_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above3_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=15)

        above3_title = Label(above3_frame, text='일일 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above3_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        above3_value = Label(above3_frame, text=' 749843.4 ', fg='#B97687', bg='#2f323b', font=('SCDream5', 25, 'bold'))
        above3_value.pack(fill=X, pady=10)

        above3_unit = Label(above3_frame, text='kW', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above3_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above4_frame = Frame(control_Activity.top_canvas, bg='#2f323b', height=180, width=250)
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

        control_frame = Frame(self, bg='#111111')
        control_frame.pack(fill=BOTH, side=TOP, expand=True)

        control_canvas = Canvas(control_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=800)
        control_canvas.pack(fill=X, padx=15, pady=15)

        auto_mode_label = Label(control_canvas, text='운전모드 제어', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'))
        auto_mode_label.place(x=30, y=20)

        auto_mode_frame = Frame(control_canvas, bg='#2f323b')
        auto_mode_frame.place(x=30, y=70)

        control_Activity.auto_mode_btn = Button(auto_mode_frame, text='자동운전', fg='white', bg='#96c63e', width=7,
                                                font=('SCDream5', 18, 'bold'), command=lambda: self.auto_control())
        control_Activity.auto_mode_btn.pack(side=LEFT)

        control_Activity.reserve_mode_btn = Button(auto_mode_frame, text='예약운전', fg='white', bg='#96c63e', width=7,
                                                   font=('SCDream5', 18, 'bold'), command=lambda: self.reserve_control())
        control_Activity.reserve_mode_btn.pack(side=LEFT, padx=(10, 0))

        control_Activity.manual_mode_btn = Button(auto_mode_frame, text='수동운전', fg='white', bg='#007ad1', width=7,
                                                  font=('SCDream5', 18, 'bold'), command=lambda: self.manual_control())
        control_Activity.manual_mode_btn.pack(side=LEFT, padx=10)

        control_Activity.stop_mode_btn = Button(auto_mode_frame, text='정    지', fg='white', bg='red', width=7,
                                                font=('SCDream5', 18, 'bold'), command=lambda: self.stop_control())
        control_Activity.stop_mode_btn.pack(side=LEFT)

        heatpump_mode_label = Label(control_canvas, text='히트펌프 제어', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'))
        heatpump_mode_label.place(x=30, y=150)

        fcu_mode_label = Label(control_canvas, text='에어컨(FCU) 제어', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'))
        fcu_mode_label.place(x=580, y=20)

        fcu_frame = Frame(control_canvas, bg='#2f323b')
        fcu_frame.place(x=580, y=70)

        # 에어컨 전원 프레임
        fcu_power_frame = Frame(fcu_frame, bg='#2f323b')
        fcu_power_frame.pack(fill=X)

        Label(fcu_power_frame, text='전  원', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)
        control_Activity.fcu_power_on_btn = Button(fcu_power_frame, text='운  전', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_power_on_btn.pack(side=LEFT, padx=10)

        control_Activity.fcu_power_off_btn = Button(fcu_power_frame, text='정  지', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_power_off_btn.pack(side=LEFT)

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 10)).pack()

        # 에어컨 모드 프레임
        fcu_mode_frame = Frame(fcu_frame, bg='#2f323b')
        fcu_mode_frame.pack(fill=X)

        Label(fcu_mode_frame, text='모  드', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)
        control_Activity.fcu_cool_btn = Button(fcu_mode_frame, text='냉  방', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_cool_btn.pack(side=LEFT, padx=10)

        control_Activity.fcu_heat_btn = Button(fcu_mode_frame, text='난  방', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_heat_btn.pack(side=LEFT, padx=(0, 10))

        control_Activity.fcu_wind_btn = Button(fcu_mode_frame, text='송  풍', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_wind_btn.pack(side=LEFT)

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 10)).pack()

        # 에어컨 풍속 프레임
        fcu_speed_frame = Frame(fcu_frame, bg='#2f323b')
        fcu_speed_frame.pack(fill=X)

        Label(fcu_speed_frame, text='풍  속', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)
        control_Activity.fcu_low_btn = Button(fcu_speed_frame, text='약', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_low_btn.pack(side=LEFT, padx=10)

        control_Activity.fcu_mid_btn = Button(fcu_speed_frame, text='중', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_mid_btn.pack(side=LEFT, padx=(0, 10))

        control_Activity.fcu_high_btn = Button(fcu_speed_frame, text='강', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_high_btn.pack(side=LEFT, padx=(0, 10))

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 2)).pack()

        fcu_speed_frame2 = Frame(fcu_frame, bg='#2f323b')
        fcu_speed_frame2.pack(fill=X)

        Label(fcu_speed_frame2, text='      ', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)

        control_Activity.fcu_auto_btn = Button(fcu_speed_frame2, text='자 동', fg='white', bg='lightgray',
                                               font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_auto_btn.pack(side=LEFT, padx=10)

        control_Activity.fcu_stop_btn = Button(fcu_speed_frame2, text='정 지', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_stop_btn.pack(side=LEFT)

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 10)).pack()

        # 에어컨 풍향 프레임
        fcu_wind_frame = Frame(fcu_frame, bg='#2f323b')
        fcu_wind_frame.pack(fill=X)

        Label(fcu_wind_frame, text='풍  속', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)
        control_Activity.fcu_wind_on_btn = Button(fcu_wind_frame, text='스  윙', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_wind_on_btn.pack(side=LEFT, padx=10)

        control_Activity.fcu_wind_off_btn = Button(fcu_wind_frame, text='정  지', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_wind_off_btn.pack(side=LEFT, padx=(0, 10))

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 10)).pack()

        # 에어컨 터보모드 프레임
        fcu_turbo_frame = Frame(fcu_frame, bg='#2f323b')
        fcu_turbo_frame.pack(fill=X)

        Label(fcu_turbo_frame, text='터  보', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)
        control_Activity.fcu_turbo_on_btn = Button(fcu_turbo_frame, text='터  보', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_turbo_on_btn.pack(side=LEFT, padx=10)

        control_Activity.fcu_turbo_off_btn = Button(fcu_turbo_frame, text='정  지', fg='white', bg='lightgray', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_turbo_off_btn.pack(side=LEFT, padx=(0, 10))

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 10)).pack()

        # 에어컨 설정온도 프레임
        fcu_setTemp_frame = Frame(fcu_frame, bg='#2f323b')
        fcu_setTemp_frame.pack(fill=X)

        Label(fcu_setTemp_frame, text='온도설정', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)
        control_Activity.fcu_temp_minus_btn = Button(fcu_setTemp_frame, text='▼', fg='white', bg='red', font=('SCDream5', 18, 'bold'), width=3)
        control_Activity.fcu_temp_minus_btn.pack(side=LEFT, padx=10)

        control_Activity.fcu_temp_entry = Entry(fcu_setTemp_frame, font=('SCDream5', 20, 'bold'), width=8, justify='center', state='readonly')
        control_Activity.fcu_temp_entry.pack(side=LEFT, padx=10, ipady=5)

        control_Activity.fcu_temp_plus_btn = Button(fcu_setTemp_frame, text='▲', fg='white', bg='#96c63e', font=('SCDream5', 18, 'bold'), width=3)
        control_Activity.fcu_temp_plus_btn.pack(side=LEFT, padx=10)

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 10)).pack()

        # 에어컨 실내온도 프레임
        fcu_nowTemp_frame = Frame(fcu_frame, bg='#2f323b')
        fcu_nowTemp_frame.pack(fill=X)

        Label(fcu_nowTemp_frame, text='실내온도', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=6, anchor='w').pack(side=LEFT)

        control_Activity.fcu_nowTemp = Label(fcu_nowTemp_frame, text=' - ', fg='#96c63e', bg='#2f323b', font=('SCDream5', 20, 'bold'), width=5)
        control_Activity.fcu_nowTemp.pack(side=LEFT, padx=(10, 3))

        Label(fcu_nowTemp_frame, text='℃', fg='#96c63e', bg='#2f323b', font=('SCDream5', 20, 'bold')).pack(side=LEFT)

        Label(fcu_frame, bg='#2f323b', font=('SCDream5', 10)).pack()


        # 시스템 설정 프레임
        setting_frame = Frame(self, bg='#111111')
        setting_frame.pack(fill=BOTH, side=BOTTOM, expand=True)

        setting_canvas = Canvas(setting_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=400)
        setting_canvas.pack(fill=X, padx=15, pady=15)

        setting_title_frame = Frame(setting_canvas, bg='#2f323b')
        setting_title_frame.pack(fill=X, pady=20)

        Label(setting_title_frame, text='제어수치 설정', bg='#2f323b', fg='#96c63e', font=('SCDream5', 20, 'bold')).pack()

        setting_left_frame = Frame(setting_canvas, bg='#2f323b')
        setting_left_frame.pack(fill=BOTH, side=LEFT, expand=True)


        insolation_frame = Frame(setting_left_frame, bg='#2f323b')
        insolation_frame.pack(fill=X, pady=10)

        insolation_label = Label(insolation_frame, text='팬 제어를 위한 일사량 설정', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold'), width=22, anchor='w')
        insolation_label.pack(side=LEFT, padx=(20, 0))

        control_Activity.insolation_value = Entry(insolation_frame, width=8, font=('SCDream5', 20, 'bold'))
        control_Activity.insolation_value.pack(side=LEFT, padx=10)

        insolation_btn = Button(insolation_frame, text='적  용', font=('SCDream5', 15, 'bold'))
        insolation_btn.pack(side=LEFT)

        damper_temp_frame = Frame(setting_left_frame, bg='#2f323b')
        damper_temp_frame.pack(fill=X, pady=10)

        damper_temp_label = Label(damper_temp_frame, text='댐퍼 제어를 위한 온도 설정', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold'), width=22, anchor='w')
        damper_temp_label.pack(side=LEFT, padx=(20, 0))

        control_Activity.damper_temp_value = Entry(damper_temp_frame, width=8, font=('SCDream5', 20, 'bold'))
        control_Activity.damper_temp_value.pack(side=LEFT, padx=10)

        damper_temp_btn = Button(damper_temp_frame, text='적  용', font=('SCDream5', 15, 'bold'))
        damper_temp_btn.pack(side=LEFT)

        setting_right_frame = Frame(setting_canvas, bg='#2f323b')
        setting_right_frame.pack(fill=BOTH, side=RIGHT, expand=True)

        bipvt_power_frame = Frame(setting_right_frame, bg='#2f323b')
        bipvt_power_frame.pack(fill=X, pady=10)

        bipvt_power_label = Label(bipvt_power_frame, text='태양광 발전 용량', bg='#2f323b', fg='white', font=('SCDream5', 15, 'bold'), width=22, anchor='w')
        bipvt_power_label.pack(side=LEFT, padx=(20, 0))

        control_Activity.bipvt_power_value = Entry(bipvt_power_frame, width=8, font=('SCDream5', 20, 'bold'))
        control_Activity.bipvt_power_value.pack(side=LEFT, padx=10)

        bipvt_power_btn = Button(bipvt_power_frame, text='적  용', font=('SCDream5', 15, 'bold'))
        bipvt_power_btn.pack(side=LEFT)




    def auto_contrl(self):
        if comd.var.bipvt_connect_status and comd.var.heatpump_connect_status:
            comd.read_cmd.auto_mode()
            db.sqlite_connect.automode_update('auto')
            db.sqlite_connect.run_insert('자동운전모드', '자동운전', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), '자동운전모드', '자동운전'))
        else:
            tk.messagebox.showwarning('자동운전모드 제어 에러', 'PVT, 히트펌프 연결 상태를 확인하세요')

    def reserve_control(self):
        if comd.var.bipvt_connect_status and comd.var.heatpump_connect_status:
            comd.read_cmd.reserve_mode()
            comd.var.reserve_trigger = False
            db.sqlite_connect.automode_update('reserve')
            db.sqlite_connect.run_insert('예약운전모드', '예약운전', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), '예약운전모드', '예약운전'))
        else:
            tk.messagebox.showwarning('예약운전모드 제어 에러', 'PVT, 히트펌프 연결 상태를 확인하세요')

    def manual_control(self):
        try:
            comd.read_cmd.manual_mode()
            db.sqlite_connect.automode_update('manual')
        except Exception as ex:
            print(ex)

    def stop_control(self):
        comd.read_cmd.stop_mode()
        db.sqlite_connect.automode_update('stop')
        db.sqlite_connect.run_insert('운전모드', '정지', now_time())
        ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                     values=(now_time(), '운전모드', '정지'))

    def cool_control(self):
        if comd.var.heatpump_connect_status:
            comd.read_cmd.mode_control(0)
            comd.var.hot_mode = False
            db.sqlite_connect.run_insert('히트펌프모드', '냉방모드', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), '히트펌프모드', '냉방모드'))
        else:
            tk.messagebox.showwarning('히트펌프모드 제어 에러', '히트펌프 연결 상태를 확인하세요')

    def heat_control(self):
        if comd.var.heatpump_connect_status:
            comd.read_cmd.mode_control(1)
            comd.var.hot_mode = True
            db.sqlite_connect.run_insert('히트펌프모드', '난방모드', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), '히트펌프모드', '난방모드'))
        else:
            tk.messagebox.showwarning('히트펌프모드 제어 에러', '히트펌프 연결 상태를 확인하세요')

    def boil_control(self):
        if comd.var.heatpump_connect_status:
            comd.read_cmd.mode_control(2)
            comd.var.hot_mode = False
            db.sqlite_connect.run_insert('히트펌프모드', '급탕모드', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), '히트펌프모드', '급탕모드'))
        else:
            tk.messagebox.showwarning('히트펌프모드 제어 에러', '히트펌프 연결 상태를 확인하세요')

    def keep_control(self):
        if comd.var.heatpump_connect_status:
            comd.read_cmd.mode_control(3)
            comd.var.hot_mode = False
            db.sqlite_connect.run_insert('히트펌프모드', '제상모드', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), '히트펌프모드', '제상모드'))
        else:
            tk.messagebox.showwarning('히트펌프모드 제어 에러', '히트펌프 연결 상태를 확인하세요')

    def damper_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.damper_on()
            db.sqlite_connect.run_insert('PVT 수동운전', '댐퍼 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), 'PVT 수동운전', '댐퍼 ON'))

    def damper_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.damper_off()
            db.sqlite_connect.run_insert('PVT 수동운전', '댐퍼 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), 'PVT 수동운전', '댐퍼 OFF'))

    def fan_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.fan_on()
            db.sqlite_connect.run_insert('PVT 수동운전', '팬 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()),
                                                         values=(now_time(), 'PVT 수동운전', '팬 ON'))

    def fan_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.fan_off()
            db.sqlite_connect.run_insert('PVT 수동운전', '팬 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), 'PVT 수동운전', '팬 OFF'))

    def exchanger_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.exchanger_on()
            db.sqlite_connect.run_insert('PVT 수동운전', '열교환기 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), 'PVT 수동운전', '열교환기 ON'))

    def exchanger_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.exchanger_off()
            db.sqlite_connect.run_insert('PVT 수동운전', '열교환기 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), 'PVT 수동운전', '열교환기 OFF'))
    def buffer_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.buffer_on()
            db.sqlite_connect.run_insert('PVT 수동운전', '버퍼탱크 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), 'PVT 수동운전', '버퍼탱크 ON'))

    def buffer_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.bipvt_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', 'PVT 연결 상태를 확인하세요')
        else:
            comd.read_cmd.buffer_off()
            db.sqlite_connect.run_insert('PVT 수동운전', '버퍼탱크 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), 'PVT 수동운전', '버퍼탱크 OFF'))

    def doublecoil_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.doublecoil_on()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '이중코일 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()), values=(now_time(), '히트펌프 수동운전', '이중코일 ON'))

    def doublecoil_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.doublecoil_off()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '이중코일 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '이중코일 OFF'))

    def heatpump_outair_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.heatpump_outair_on()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '히트펌프 외기 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '히트펌프 외기 ON'))

    def heatpump_outair_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.heatpump_outair_off()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '히트펌프 외기 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '히트펌프 외기 OFF'))

    def dhw_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.dhw_on()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '온수탱크 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '온수탱크 ON'))

    def dhw_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.dhw_off()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '온수탱크 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '온수탱크 OFF'))

    def storage_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.storage_on()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '저장탱크 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '저장탱크 ON'))

    def storage_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.storage_off()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '저장탱크 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '저장탱크 OFF'))

    def heatpump_on_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.heatpump_on()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '히트펌프 ON', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '히트펌프 ON'))

    def heatpump_off_control(self):
        if not comd.var.manual_mode:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '수동운전모드 제어 상태를 확인하세요')
        elif not comd.var.heatpump_connect_status:
            tk.messagebox.showwarning('수동운전모드 제어 에러', '히트펌프 연결 상태를 확인하세요')
        else:
            comd.read_cmd.heatpump_off()
            db.sqlite_connect.run_insert('히트펌프 수동운전', '히트펌프 OFF', now_time())
            ui.run_Activity.run_Activity.run_list.insert('', index=0, text=int(run_len()) ,
                                                         values=(now_time(), '히트펌프 수동운전', '히트펌프 OFF'))

    def insert_start_hour(self, event):
        notification.insert_keypad.put_start_hour_value(self, '값 입력')
    def insert_start_min(self, event):
        notification.insert_keypad.put_start_min_value(self, '값 입력')
    def insert_end_hour(self, event):
        notification.insert_keypad.put_end_hour_value(self, '값 입력')
    def insert_end_min(self, event):
        notification.insert_keypad.put_end_min_value(self, '값 입력')

    def schedule_apply(self):
        start_time = '%s:%s' % (self.start_hour_entry.get(), self.start_min_entry.get())
        end_time = '%s:%s' % (self.end_hour_entry.get(), self.end_min_entry.get())
        if self.start_hour_entry.get() == '' or self.start_min_entry.get() == '' or self.end_hour_entry.get() == '' or self.end_min_entry.get() == '':
            tkinter.messagebox.showwarning('설정오류', '설정 시간을 입력하세요')
        elif start_time == end_time:
            tkinter.messagebox.showwarning('설정오류', '동일한 시간으로 설정할 수 없습니다.')
        else:
            res_msg = tkinter.messagebox.askyesno('설정', '입력하신 내용으로 설정하시겠습니까?')

            if res_msg:
                db.sqlite_connect.schedule_update(self.start_hour_entry.get(), self.start_min_entry.get(), self.end_hour_entry.get(), self.end_min_entry.get())
