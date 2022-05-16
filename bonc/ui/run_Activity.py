import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import ui.main_Activity
import ui.control_Activity
import ui.setting_Activity

import db.sqlite_connect
from PIL import ImageTk, Image

from time import sleep
import tkinter.simpledialog
import tkinter.messagebox
import comd.var


class run_Activity(tk.Frame):
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
        run_Activity.gps_menu = Label(title_frame, image=self.gps_image, highlightbackground='#111111',
                                          activebackground='#111111', bd=0, bg='#111111')
        run_Activity.gps_menu.pack(side=LEFT, padx=(0, 10), pady=(8, 0))

        weather_menu = Label(title_frame, text='날씨', highlightbackground='#111111', activebackground='#111111', bd=0,
                             bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        weather_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        weather_img = Image.open('images/weather/01d.png')
        weather_img = weather_img.resize((40, 40), Image.ANTIALIAS)
        self.weather_image = ImageTk.PhotoImage(weather_img)
        run_Activity.weather_value = Label(title_frame, highlightbackground='#111111', image=self.weather_image,
                                               activebackground='#111111', bd=0, bg='#111111',
                                               font=('SCDream5', 16, 'bold'),
                                               fg='white')
        run_Activity.weather_value.pack(side=LEFT, pady=(8, 0))

        temperature_menu = Label(title_frame, text='| 기온', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_menu.pack(side=LEFT, padx=(10, 10), pady=(8, 0))

        run_Activity.temperature_value = Label(title_frame, text='32.5', highlightbackground='#111111',
                                                   activebackground='#111111', bd=0, bg='#111111',
                                                   font=('SCDream5', 16, 'bold'),
                                                   fg='white')
        run_Activity.temperature_value.pack(side=LEFT, pady=(8, 0))

        temperature_unit = Label(title_frame, text=' ℃', highlightbackground='#111111',
                                 activebackground='#111111', bd=0, bg='#111111', font=('SCDream5', 16, 'bold'),
                                 fg='white')
        temperature_unit.pack(side=LEFT, pady=(8, 0))

        humi_menu = Label(title_frame, text='| 습도', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_menu.pack(side=LEFT, padx=10, pady=(8, 0))

        run_Activity.humi_value = Label(title_frame, text='44.3', highlightbackground='#111111',
                                            activebackground='#111111', bd=0, bg='#111111',
                                            font=('SCDream5', 16, 'bold'),
                                            fg='white')
        run_Activity.humi_value.pack(side=LEFT, pady=(8, 0))

        humi_unit = Label(title_frame, text='%', highlightbackground='#111111', activebackground='#111111', bd=0,
                          bg='#111111', font=('SCDream5', 16, 'bold'), fg='white')
        humi_unit.pack(side=LEFT, pady=(8, 0))

        run_Activity.time_label2 = Label(title_frame, text='-', highlightbackground='#111111',
                                             activebackground='#111111', bd=0, bg='#111111',
                                             font=('SCDream5', 18, 'bold'),
                                             fg='#96c63e')
        run_Activity.time_label2.pack(side=RIGHT, padx=(10, 30), pady=(8, 0))

        run_Activity.time_label1 = Label(title_frame, text='-', highlightbackground='#111111',
                                             activebackground='#111111', bd=0, bg='#111111',
                                             font=('SCDream5', 18, 'bold'),
                                             fg='white')
        run_Activity.time_label1.pack(side=RIGHT, pady=(8, 0))

        self.date_image = tk.PhotoImage(file='images/date.png')
        date_menu = Label(title_frame, image=self.date_image, highlightbackground='#111111', activebackground='#111111',
                          bd=0, bg='#111111')
        date_menu.pack(side=RIGHT, padx=(0, 5), pady=(8, 0))

        ########################### 메뉴 버튼 ###############################
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, side=TOP, ipady=10)

        self.main_image = tk.PhotoImage(file='images/main_btn_off.png')
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
        run_Activity.top_canvas = Canvas(top_frame, bg='#111111', highlightbackground='#111111', width=870,
                                             height=200, bd=0)
        run_Activity.top_canvas.pack(padx=15, fill=X, pady=(15, 0))

        above1_frame = Frame(run_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above1_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above1_title = Label(above1_frame, text='일일 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above1_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        run_Activity.above1_value = Label(above1_frame, text=' - ', fg='#CFDD8E', bg='#2f323b',
                                              font=('SCDream5', 25, 'bold'))
        run_Activity.above1_value.pack(fill=X, pady=10)

        above1_unit = Label(above1_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above1_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above2_frame = Frame(run_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above2_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(15, 0))

        above2_title = Label(above2_frame, text='누적 태양광 발전량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above2_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        run_Activity.above2_value = Label(above2_frame, text=' - ', fg='#6ECEDA', bg='#2f323b',
                                              font=('SCDream5', 25, 'bold'))
        run_Activity.above2_value.pack(fill=X, pady=10)

        above2_unit = Label(above2_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above2_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above3_frame = Frame(run_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above3_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=15)

        above3_title = Label(above3_frame, text='일일 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above3_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        run_Activity.above3_value = Label(above3_frame, text=' - ', fg='#B97687', bg='#2f323b',
                                              font=('SCDream5', 25, 'bold'))
        run_Activity.above3_value.pack(fill=X, pady=10)

        above3_unit = Label(above3_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above3_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        above4_frame = Frame(run_Activity.top_canvas, bg='#2f323b', height=180, width=250)
        above4_frame.pack(side=LEFT, fill=BOTH, expand=True)

        above4_title = Label(above4_frame, text='누적 부하 사용량', fg='white', bg='#2f323b', font=('SCDream5', 15, 'bold'),
                             anchor='w')
        above4_title.pack(fill=X, padx=(10, 0), pady=(10, 0))

        run_Activity.above4_value = Label(above4_frame, text=' - ', fg='#d18063', bg='#2f323b',
                                              font=('SCDream5', 25, 'bold'))
        run_Activity.above4_value.pack(fill=X, pady=10)

        above4_unit = Label(above4_frame, text='kWh', fg='white', bg='#2f323b', font=('SCDream5', 20, 'bold'),
                            anchor='e')
        above4_unit.pack(fill=X, padx=(0, 15), pady=(0, 10))

        # left frame
        center_frame = Frame(self, bg='#111111')
        center_frame.pack(fill=BOTH, side=TOP, expand=True)

        run_canvas = Canvas(center_frame, bg='#2f323b', highlightbackground='#2f323b', width=870, height=1600)
        run_canvas.pack(padx=15, fill=BOTH, pady=15, expand=True)

        top_set_contents_frame = Frame(run_canvas, bg="#2f323b", highlightbackground="#2f323b")
        top_set_contents_frame.pack(side=TOP, ipadx=0, padx=10, pady=20)

        # run_list_Title
        battery_state_label = Label(top_set_contents_frame, text="스마트그리드 제어이력 조회", font=('SCDream5', 20, 'bold'),
                                    fg='#96c63e', bg='#2f323b')
        battery_state_label.pack()

        # height black
        label1 = Label(top_set_contents_frame, bg="#2f323b")
        label1.pack()

        run_xframe = Frame(top_set_contents_frame, bg="#2f323b")
        run_xframe.pack(fill=BOTH, expand=True)

        # height black
        label1 = Label(top_set_contents_frame, bg="#2f323b")
        label1.pack()

        run_Activity.run_list = ttk.Treeview(run_xframe, columns=['1', '2', '3'], height=90)
        run_Activity.run_list.pack(side=LEFT, fill=BOTH, )

        style = ttk.Style()

        run_scroll = ttk.Scrollbar(run_xframe, orient='vertical', command=run_Activity.run_list.yview)
        run_Activity.run_list.configure(yscrollcommand=run_scroll.set)
        run_scroll.pack(expand=True, side=LEFT, fill=Y)

        style.configure('Treeview.Heading', rowheight=60, font=('SCDream5', 30, 'bold'))
        style.configure('Treeview', font=('SCDream5', 20, 'bold'), rowheight=30)

        run_Activity.run_list.heading('#0', text='')
        run_Activity.run_list.heading('#1', text='일시')
        run_Activity.run_list.heading('#2', text='항목')
        run_Activity.run_list.heading('#3', text='내용')

        run_Activity.run_list.column('#0', width=1, anchor='center')
        run_Activity.run_list.column('#1', width=250, anchor='center')
        run_Activity.run_list.column('#2', width=200, anchor='center')
        run_Activity.run_list.column('#3', width=500, anchor='center')

        # style.configure('Treeview.Heading', bg='blue', fg='#D9EBF9')

        rows = db.sqlite_connect.run_all()
        run_len = len(rows)

        for row in rows:
            run_Activity.run_list.insert('', 'end', text=run_len, values=(row[2], row[0], row[1]))

            run_len = run_len - 1


