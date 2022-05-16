import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter as tk
from tkinter.tix import *
import tkinter.simpledialog
import tkinter.messagebox
from PIL import Image, ImageTk
import datetime
import notification.insert_keypad
import db.sqlite_connect
import ui.run_Activity
import ui.error_Activity

import comd.var


def setFont(size=15):
    font = 'SCDream5', size, 'bold'
    return font


class detail_Activity(tk.Frame):
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
        detail_Activity.weather_value = Label(title_frame, highlightbackground='#111111', image=self.weather_image,
                                              activebackground='#111111', bd=0, bg='#111111',
                                              font=('SCDream5', 16, 'bold'),
                                              fg='white')
        detail_Activity.weather_value.pack(side=LEFT, pady=(8, 0))

        temperature_menu = Label(title_frame, text='| 기온', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_menu.pack(side=LEFT, padx=(10, 10), pady=(8, 0))

        detail_Activity.temperature_value = Label(title_frame, text='32.5', highlightbackground='#111111',
                                                  activebackground='#111111', bd=0, bg='#111111',
                                                  font=('SCDream5', 16, 'bold'),
                                                  fg='white')
        detail_Activity.temperature_value.pack(side=LEFT, pady=(8, 0))

        temperature_unit = Label(title_frame, text=' ℃', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_unit.pack(side=LEFT, pady=(8, 0))

        humi_menu = Label(title_frame, text='| 습도', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        detail_Activity.humi_value = Label(title_frame, text='44.3', highlightbackground='#111111',
                                           activebackground='#111111', bd=0, bg='#111111',
                                           font=('SCDream5', 16, 'bold'),
                                           fg='white')
        detail_Activity.humi_value.pack(side=LEFT, pady=(8, 0))

        humi_unit = Label(title_frame, text='%', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_unit.pack(side=LEFT, pady=(8, 0))

        detail_Activity.time_label2 = Label(title_frame, text='-', highlightbackground='#111111',
                                            activebackground='#111111', bd=0, bg='#111111',
                                            font=('SCDream5', 18, 'bold'),
                                            fg='#96c63e')
        detail_Activity.time_label2.pack(side=RIGHT, padx=(10, 30), pady=(8, 0))

        detail_Activity.time_label1 = Label(title_frame, text='-', highlightbackground='#111111',
                                            activebackground='#111111', bd=0, bg='#111111',
                                            font=('SCDream5', 18, 'bold'),
                                            fg='white')
        detail_Activity.time_label1.pack(side=RIGHT, pady=(8, 0))

        self.date_image = tk.PhotoImage(file='images/date.png')
        date_menu = Label(title_frame, image=self.date_image, highlightbackground='#111111', activebackground='#111111',
                          bd=0, bg='#111111')
        date_menu.pack(side=RIGHT, padx=(0, 5), pady=(8, 0))

        ########################### 메뉴 버튼 ###############################
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, side=TOP, ipady=10)

        self.main_image = tk.PhotoImage(file='images/main_btn_off.png')
        self.detail_image = tk.PhotoImage(file='images/detail_btn.png')
        self.control_image = tk.PhotoImage(file='images/control_btn_off.png')
        self.setting_image = tk.PhotoImage(file='images/setting_btn_off.png')

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
        detail_Activity.top_canvas = Canvas(top_frame, bg='#111111', highlightbackground='#111111', width=870,
                                            height=200)
        detail_Activity.top_canvas.pack(padx=15, fill=X, pady=(15, 0))

        above1_frame = Frame(detail_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above1_frame.pack(side=LEFT, fill=BOTH, expand=True, )

        above1_title = Label(above1_frame, text='일일 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above1_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        detail_Activity.above1_value = Label(above1_frame, text=' - ', fg='#CFDD8E', bg='#2f323b',
                                             font=('SCDream5', 25, 'bold'))
        detail_Activity.above1_value.pack(fill=X, pady=10)

        above1_unit = Label(above1_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above1_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above2_frame = Frame(detail_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above2_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(15, 0))

        above2_title = Label(above2_frame, text='누적 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above2_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        detail_Activity.above2_value = Label(above2_frame, text=' - ', fg='#6ECEDA', bg='#2f323b',
                                             font=('SCDream5', 25, 'bold'))
        detail_Activity.above2_value.pack(fill=X, pady=10)

        above2_unit = Label(above2_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above2_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above3_frame = Frame(detail_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above3_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=15)

        above3_title = Label(above3_frame, text='일일 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above3_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        detail_Activity.above3_value = Label(above3_frame, text=' - ', fg='#B97687', bg='#2f323b',
                                             font=('SCDream5', 25, 'bold'))
        detail_Activity.above3_value.pack(fill=X, pady=10)

        above3_unit = Label(above3_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above3_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above4_frame = Frame(detail_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above4_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above4_title = Label(above4_frame, text='누적 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above4_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        detail_Activity.above4_value = Label(above4_frame, text=' - ', fg='#d18063', bg='#2f323b',
                                             font=('SCDream5', 25, 'bold'))
        detail_Activity.above4_value.pack(fill=X, pady=10)

        above4_unit = Label(above4_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above4_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        # center top frame
        center_frame = Frame(self, bg='#111111')
        center_frame.pack(fill=BOTH, side=TOP, expand=True)

        # detail Canvas
        detail_canvas = Canvas(center_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=1600)
        detail_canvas.pack(padx=15, fill=BOTH, pady=15, expand=True)

        # 데이터 타이틀
        data_title = Label(detail_canvas, text='데이터 상세정보', font=(setFont(25)), fg='white', bg='#2f323b')
        data_title.place(x=20, y=13)

        data_header_frame = Frame(detail_canvas, bg='#2f323b')
        data_header_frame.place(x=20, y=80)

        # detail_canvas.create_line(65, 120, 1024, 120, fill='white', width=5)
        self.line_image = tk.PhotoImage(file='images/line.png')
        self.line_image2 = tk.PhotoImage(file='images/line2.png')
        Label(detail_canvas, image=self.line_image, width=960).place(x=65, y=120)
        Label(detail_canvas, image=self.line_image, width=960).place(x=65, y=470)
        Label(detail_canvas, image=self.line_image, width=960).place(x=65, y=600)
        Label(detail_canvas, image=self.line_image, width=960).place(x=65, y=780)
        Label(detail_canvas, image=self.line_image, width=960).place(x=65, y=955)
        Label(detail_canvas, image=self.line_image, width=960).place(x=65, y=1175)
        Label(detail_canvas, image=self.line_image2, height=1440).place(x=415, y=80)

        data_header_item = Label(data_header_frame, text='위치', font=setFont(20), fg='white', bg='#2f323b', width=15)
        data_header_item.grid(row=0, column=0)

        data_header_loc = Label(data_header_frame, text='항목', font=setFont(20), fg='white', bg='#2f323b', width=8)
        data_header_loc.grid(row=0, column=1)

        data_header_real = Label(data_header_frame, text='실시간', font=setFont(20), fg='white', bg='#2f323b', width=7)
        data_header_real.grid(row=0, column=2)

        data_header_max = Label(data_header_frame, text='최대', font=setFont(20), fg='white', bg='#2f323b', width=7)
        data_header_max.grid(row=0, column=3)

        data_header_min = Label(data_header_frame, text='최소', font=setFont(20), fg='white', bg='#2f323b', width=7)
        data_header_min.grid(row=0, column=4)

        data_header_avg = Label(data_header_frame, text='평균', font=setFont(20), fg='white', bg='#2f323b', width=7)
        data_header_avg.grid(row=0, column=5)

        data_header_unit = Label(data_header_frame, text='단위', font=setFont(20), fg='white', bg='#2f323b', width=4)
        data_header_unit.grid(row=0, column=6)

        Label(data_header_frame, text='PVT 컬렉터', font=setFont(), fg='white', bg='#2f323b', width=12).grid(row=1,
                                                                                                          column=0,
                                                                                                          pady=(10, 5),
                                                                                                          rowspan=8)
        Label(data_header_frame, text='버퍼 탱크', font=setFont(), fg='white', bg='#2f323b', width=12).grid(row=9, column=0,
                                                                                                        pady=7,
                                                                                                        rowspan=3)
        Label(data_header_frame, text='저장 탱크', font=setFont(), fg='white', bg='#2f323b', width=12).grid(row=12,
                                                                                                        column=0,
                                                                                                        pady=7,
                                                                                                        rowspan=4)
        Label(data_header_frame, text='급탕 탱크', font=setFont(), fg='white', bg='#2f323b', width=12).grid(row=16,
                                                                                                        column=0,
                                                                                                        pady=7,
                                                                                                        rowspan=4)
        Label(data_header_frame, text='부하 전력', font=setFont(), fg='white', bg='#2f323b', width=12).grid(row=20,
                                                                                                        column=0,
                                                                                                        pady=7,
                                                                                                        rowspan=5)
        Label(data_header_frame, text='웨더스테이션', font=setFont(), fg='white', bg='#2f323b', width=12).grid(row=25,
                                                                                                         column=0,
                                                                                                         pady=7,
                                                                                                         rowspan=8)

        # PVT 컬렉터
        Label(data_header_frame, text='발전량', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=1, column=1,
                                                                                                      pady=(10, 5))
        Label(data_header_frame, text='내부온도1', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=2, column=1,
                                                                                                        pady=7)
        Label(data_header_frame, text='내부온도2', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=3, column=1,
                                                                                                        pady=7)
        Label(data_header_frame, text='내부온도3', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=4, column=1,
                                                                                                        pady=7)
        Label(data_header_frame, text='입구온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=5, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='입구습도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=6, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='출구온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=7, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='출구습도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=8, column=1,
                                                                                                       pady=7)
        # 버퍼탱크
        Label(data_header_frame, text='탱크온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=9, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='입구온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=10, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='유체유량', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=11, column=1,
                                                                                                       pady=7)
        # 저장탱크
        Label(data_header_frame, text='입구온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=12, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='출구온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=13, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='입구유량', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=14, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='출구유량', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=15, column=1,
                                                                                                       pady=7)
        # 급탕탱크
        Label(data_header_frame, text='탱크온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=16, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='입구온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=17, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='출구온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=18, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='유체유량', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=19, column=1,
                                                                                                       pady=7)
        # 부하 전력
        Label(data_header_frame, text='히트펌프', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=20, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='버퍼탱크', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=21, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='저장탱크', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=22, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='급탕탱크', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=23, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='열   선', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=24,
                                                                                                        column=1,
                                                                                                        pady=7)
        # 웨더스테이션
        Label(data_header_frame, text='외기온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=25, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='외기습도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=26, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='일 사 량', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=27,
                                                                                                        column=1,
                                                                                                        pady=7)
        Label(data_header_frame, text='풍    속', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=28,
                                                                                                         column=1,
                                                                                                         pady=7)
        Label(data_header_frame, text='강 수 량', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=29,
                                                                                                        column=1,
                                                                                                        pady=7)
        Label(data_header_frame, text='실내온도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=30, column=1,
                                                                                                       pady=7)
        Label(data_header_frame, text='실내습도', font=setFont(), fg='white', bg='#2f323b', width=10).grid(row=31, column=1,
                                                                                                       pady=7)

        # 실시간 데이터
        detail_Activity.pvt_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                          width=7)
        detail_Activity.pvt_power.grid(row=1, column=2)

        detail_Activity.pvt_inside_temp1 = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.pvt_inside_temp1.grid(row=2, column=2)

        detail_Activity.pvt_inside_temp2 = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.pvt_inside_temp2.grid(row=3, column=2)

        detail_Activity.pvt_inside_temp3 = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.pvt_inside_temp3.grid(row=4, column=2)

        detail_Activity.pvt_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.pvt_inner_temp.grid(row=5, column=2)

        detail_Activity.pvt_inner_humi = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.pvt_inner_humi.grid(row=6, column=2)

        detail_Activity.pvt_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.pvt_outer_temp.grid(row=7, column=2)

        detail_Activity.pvt_outer_humi = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.pvt_outer_humi.grid(row=8, column=2)

        detail_Activity.buffer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                            width=7)
        detail_Activity.buffer_temp.grid(row=9, column=2)

        detail_Activity.buffer_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                  width=7)
        detail_Activity.buffer_inner_temp.grid(row=10, column=2)

        detail_Activity.buffer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                            width=7)
        detail_Activity.buffer_flux.grid(row=11, column=2)

        detail_Activity.storage_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b', width=7)
        detail_Activity.storage_inner_temp.grid(row=12, column=2)

        detail_Activity.storage_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b', width=7)
        detail_Activity.storage_outer_temp.grid(row=13, column=2)

        detail_Activity.storage_inner_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b', width=7)
        detail_Activity.storage_inner_flux.grid(row=14, column=2)

        detail_Activity.storage_outer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b', width=7)
        detail_Activity.storage_outer_flux.grid(row=15, column=2)

        detail_Activity.dhw_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b', width=7)
        detail_Activity.dhw_temp.grid(row=16, column=2)

        detail_Activity.dhw_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.dhw_inner_temp.grid(row=17, column=2)

        detail_Activity.dhw_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.dhw_outer_temp.grid(row=18, column=2)

        detail_Activity.dhw_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b', width=7)
        detail_Activity.dhw_flux.grid(row=19, column=2)

        detail_Activity.heatpump_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.heatpump_power.grid(row=20, column=2)

        detail_Activity.buffer_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.buffer_power.grid(row=21, column=2)

        detail_Activity.storage_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                              width=7)
        detail_Activity.storage_power.grid(row=22, column=2)

        detail_Activity.dhw_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                          width=7)
        detail_Activity.dhw_power.grid(row=23, column=2)

        detail_Activity.heatline_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.heatline_power.grid(row=24, column=2)

        detail_Activity.outside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.outside_temp.grid(row=25, column=2)

        detail_Activity.outside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.outside_humi.grid(row=26, column=2)

        detail_Activity.insolation = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                           width=7)
        detail_Activity.insolation.grid(row=27, column=2)

        detail_Activity.wind_speed = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                           width=7)
        detail_Activity.wind_speed.grid(row=28, column=2)

        # detail_Activity.pressure = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
        #                                  width=7)
        # detail_Activity.pressure.grid(row=29, column=2)

        detail_Activity.rainfall = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                         width=7)
        detail_Activity.rainfall.grid(row=29, column=2)

        detail_Activity.inside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                            bg='#2f323b', width=7)
        detail_Activity.inside_temp.grid(row=30, column=2)

        detail_Activity.inside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                            bg='#2f323b', width=7)
        detail_Activity.inside_humi.grid(row=31, column=2)

        # 최대 데이터
        detail_Activity.max_pvt_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                              width=7)
        detail_Activity.max_pvt_power.grid(row=1, column=3)

        detail_Activity.max_pvt_inside_temp1 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.max_pvt_inside_temp1.grid(row=2, column=3)

        detail_Activity.max_pvt_inside_temp2 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.max_pvt_inside_temp2.grid(row=3, column=3)

        detail_Activity.max_pvt_inside_temp3 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.max_pvt_inside_temp3.grid(row=4, column=3)

        detail_Activity.max_pvt_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_pvt_inner_temp.grid(row=5, column=3)

        detail_Activity.max_pvt_inner_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_pvt_inner_humi.grid(row=6, column=3)

        detail_Activity.max_pvt_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_pvt_outer_temp.grid(row=7, column=3)

        detail_Activity.max_pvt_outer_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_pvt_outer_humi.grid(row=8, column=3)

        detail_Activity.max_buffer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                width=7)
        detail_Activity.max_buffer_temp.grid(row=9, column=3)

        detail_Activity.max_buffer_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                      bg='#2f323b',
                                                      width=7)
        detail_Activity.max_buffer_inner_temp.grid(row=10, column=3)

        detail_Activity.max_buffer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                width=7)
        detail_Activity.max_buffer_flux.grid(row=11, column=3)

        detail_Activity.max_storage_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.max_storage_inner_temp.grid(row=12, column=3)

        detail_Activity.max_storage_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.max_storage_outer_temp.grid(row=13, column=3)

        detail_Activity.max_storage_inner_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.max_storage_inner_flux.grid(row=14, column=3)

        detail_Activity.max_storage_outer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.max_storage_outer_flux.grid(row=15, column=3)

        detail_Activity.max_dhw_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.max_dhw_temp.grid(row=16, column=3)

        detail_Activity.max_dhw_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_dhw_inner_temp.grid(row=17, column=3)

        detail_Activity.max_dhw_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_dhw_outer_temp.grid(row=18, column=3)

        detail_Activity.max_dhw_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.max_dhw_flux.grid(row=19, column=3)

        detail_Activity.max_heatpump_power = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_heatpump_power.grid(row=20, column=3)

        detail_Activity.max_buffer_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.max_buffer_power.grid(row=21, column=3)

        detail_Activity.max_storage_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                  width=7)
        detail_Activity.max_storage_power.grid(row=22, column=3)

        detail_Activity.max_dhw_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                              width=7)
        detail_Activity.max_dhw_power.grid(row=23, column=3)

        detail_Activity.max_heatline_power = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.max_heatline_power.grid(row=24, column=3)

        detail_Activity.max_outside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.max_outside_temp.grid(row=25, column=3)

        detail_Activity.max_outside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.max_outside_humi.grid(row=26, column=3)

        detail_Activity.max_insolation = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.max_insolation.grid(row=27, column=3)

        detail_Activity.max_wind_speed = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.max_wind_speed.grid(row=28, column=3)

        detail_Activity.max_rainfall = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                             bg='#2f323b', width=7)
        detail_Activity.max_rainfall.grid(row=29, column=3)

        detail_Activity.max_inside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                bg='#2f323b', width=7)
        detail_Activity.max_inside_temp.grid(row=30, column=3)

        detail_Activity.max_inside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                bg='#2f323b', width=7)
        detail_Activity.max_inside_humi.grid(row=31, column=3)

        # 최소 데이터
        detail_Activity.min_pvt_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                              width=7)
        detail_Activity.min_pvt_power.grid(row=1, column=4)

        detail_Activity.min_pvt_inside_temp1 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.min_pvt_inside_temp1.grid(row=2, column=4)

        detail_Activity.min_pvt_inside_temp2 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.min_pvt_inside_temp2.grid(row=3, column=4)

        detail_Activity.min_pvt_inside_temp3 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.min_pvt_inside_temp3.grid(row=4, column=4)

        detail_Activity.min_pvt_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_pvt_inner_temp.grid(row=5, column=4)

        detail_Activity.min_pvt_inner_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_pvt_inner_humi.grid(row=6, column=4)

        detail_Activity.min_pvt_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_pvt_outer_temp.grid(row=7, column=4)

        detail_Activity.min_pvt_outer_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_pvt_outer_humi.grid(row=8, column=4)

        detail_Activity.min_buffer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                width=7)
        detail_Activity.min_buffer_temp.grid(row=9, column=4)

        detail_Activity.min_buffer_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                      bg='#2f323b',
                                                      width=7)
        detail_Activity.min_buffer_inner_temp.grid(row=10, column=4)

        detail_Activity.min_buffer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                width=7)
        detail_Activity.min_buffer_flux.grid(row=11, column=4)

        detail_Activity.min_storage_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.min_storage_inner_temp.grid(row=12, column=4)

        detail_Activity.min_storage_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.min_storage_outer_temp.grid(row=13, column=4)

        detail_Activity.min_storage_inner_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.min_storage_inner_flux.grid(row=14, column=4)

        detail_Activity.min_storage_outer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.min_storage_outer_flux.grid(row=15, column=4)

        detail_Activity.min_dhw_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.min_dhw_temp.grid(row=16, column=4)

        detail_Activity.min_dhw_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_dhw_inner_temp.grid(row=17, column=4)

        detail_Activity.min_dhw_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_dhw_outer_temp.grid(row=18, column=4)

        detail_Activity.min_dhw_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.min_dhw_flux.grid(row=19, column=4)

        detail_Activity.min_heatpump_power = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_heatpump_power.grid(row=20, column=4)

        detail_Activity.min_buffer_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.min_buffer_power.grid(row=21, column=4)

        detail_Activity.min_storage_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                  width=7)
        detail_Activity.min_storage_power.grid(row=22, column=4)

        detail_Activity.min_dhw_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                              width=7)
        detail_Activity.min_dhw_power.grid(row=23, column=4)

        detail_Activity.min_heatline_power = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.min_heatline_power.grid(row=24, column=4)

        detail_Activity.min_outside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.min_outside_temp.grid(row=25, column=4)

        detail_Activity.min_outside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.min_outside_humi.grid(row=26, column=4)

        detail_Activity.min_insolation = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.min_insolation.grid(row=27, column=4)

        detail_Activity.min_wind_speed = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.min_wind_speed.grid(row=28, column=4)

        detail_Activity.min_rainfall = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                             bg='#2f323b', width=7)
        detail_Activity.min_rainfall.grid(row=29, column=4)

        detail_Activity.min_inside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                bg='#2f323b', width=7)
        detail_Activity.min_inside_temp.grid(row=30, column=4)

        detail_Activity.min_inside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                bg='#2f323b', width=7)
        detail_Activity.min_inside_humi.grid(row=31, column=4)

        # 평균 데이터
        detail_Activity.avg_pvt_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                              width=7)
        detail_Activity.avg_pvt_power.grid(row=1, column=5)

        detail_Activity.avg_pvt_inside_temp1 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.avg_pvt_inside_temp1.grid(row=2, column=5)

        detail_Activity.avg_pvt_inside_temp2 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.avg_pvt_inside_temp2.grid(row=3, column=5)

        detail_Activity.avg_pvt_inside_temp3 = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                     bg='#2f323b',
                                                     width=7)
        detail_Activity.avg_pvt_inside_temp3.grid(row=4, column=5)

        detail_Activity.avg_pvt_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_pvt_inner_temp.grid(row=5, column=5)

        detail_Activity.avg_pvt_inner_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_pvt_inner_humi.grid(row=6, column=5)

        detail_Activity.avg_pvt_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_pvt_outer_temp.grid(row=7, column=5)

        detail_Activity.avg_pvt_outer_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_pvt_outer_humi.grid(row=8, column=5)

        detail_Activity.avg_buffer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                width=7)
        detail_Activity.avg_buffer_temp.grid(row=9, column=5)

        detail_Activity.avg_buffer_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                      bg='#2f323b',
                                                      width=7)
        detail_Activity.avg_buffer_inner_temp.grid(row=10, column=5)

        detail_Activity.avg_buffer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                width=7)
        detail_Activity.avg_buffer_flux.grid(row=11, column=5)

        detail_Activity.avg_storage_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.avg_storage_inner_temp.grid(row=12, column=5)

        detail_Activity.avg_storage_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.avg_storage_outer_temp.grid(row=13, column=5)

        detail_Activity.avg_storage_inner_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.avg_storage_inner_flux.grid(row=14, column=5)

        detail_Activity.avg_storage_outer_flux = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                       bg='#2f323b', width=7)
        detail_Activity.avg_storage_outer_flux.grid(row=15, column=5)

        detail_Activity.avg_dhw_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.avg_dhw_temp.grid(row=16, column=5)

        detail_Activity.avg_dhw_inner_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_dhw_inner_temp.grid(row=17, column=5)

        detail_Activity.avg_dhw_outer_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_dhw_outer_temp.grid(row=18, column=5)

        detail_Activity.avg_dhw_flux = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                             width=7)
        detail_Activity.avg_dhw_flux.grid(row=19, column=5)

        detail_Activity.avg_heatpump_power = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_heatpump_power.grid(row=20, column=5)

        detail_Activity.avg_buffer_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.avg_buffer_power.grid(row=21, column=5)

        detail_Activity.avg_storage_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                  width=7)
        detail_Activity.avg_storage_power.grid(row=22, column=5)

        detail_Activity.avg_dhw_power = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                              width=7)
        detail_Activity.avg_dhw_power.grid(row=23, column=5)

        detail_Activity.avg_heatline_power = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                   bg='#2f323b',
                                                   width=7)
        detail_Activity.avg_heatline_power.grid(row=24, column=5)

        detail_Activity.avg_outside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.avg_outside_temp.grid(row=25, column=5)

        detail_Activity.avg_outside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                                 width=7)
        detail_Activity.avg_outside_humi.grid(row=26, column=5)

        detail_Activity.avg_insolation = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.avg_insolation.grid(row=27, column=5)

        detail_Activity.avg_wind_speed = Label(data_header_frame, text='-', font=setFont(), fg='white', bg='#2f323b',
                                               width=7)
        detail_Activity.avg_wind_speed.grid(row=28, column=5)

        detail_Activity.avg_rainfall = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                             bg='#2f323b', width=7)
        detail_Activity.avg_rainfall.grid(row=29, column=5)

        detail_Activity.avg_inside_temp = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                bg='#2f323b', width=7)
        detail_Activity.avg_inside_temp.grid(row=30, column=5)

        detail_Activity.avg_inside_humi = Label(data_header_frame, text='-', font=setFont(), fg='white',
                                                bg='#2f323b', width=7)
        detail_Activity.avg_inside_humi.grid(row=31, column=5)

        # 단위 데이터
        Label(data_header_frame, text='W', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=1, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=2, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=3, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=4, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=5, column=6)
        Label(data_header_frame, text='%', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=6, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=7, column=6)
        Label(data_header_frame, text='%', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=8, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=9, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=10, column=6)
        Label(data_header_frame, text='LPM', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=11, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=12, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=13, column=6)
        Label(data_header_frame, text='LPM', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=14, column=6)
        Label(data_header_frame, text='LPM', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=15, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=16, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=17, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=18, column=6)
        Label(data_header_frame, text='LPM', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=19, column=6)
        Label(data_header_frame, text='W', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=20, column=6)
        Label(data_header_frame, text='W', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=21, column=6)
        Label(data_header_frame, text='W', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=22, column=6)
        Label(data_header_frame, text='W', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=23, column=6)
        Label(data_header_frame, text='W', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=24, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=25, column=6)
        Label(data_header_frame, text='%', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=26, column=6)
        Label(data_header_frame, text='W/m²', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=27, column=6)
        Label(data_header_frame, text='m/s', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=28, column=6)
        Label(data_header_frame, text='mm/h', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=29, column=6)
        Label(data_header_frame, text='℃', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=30, column=6)
        Label(data_header_frame, text='%', font=setFont(), fg='white', bg='#2f323b', width=8).grid(row=31, column=6)
