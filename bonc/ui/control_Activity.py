import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter as tk
from tkinter.tix import *
import tkinter.simpledialog
import tkinter.messagebox
import datetime
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

        # 상단 메뉴바
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, ipady=5)

        self.logo_image = tk.PhotoImage(file="images/bonc.png")
        logo_label = Label(menu_frame, image=self.logo_image, highlightbackground="#111111", activebackground='#111111', bd=0, bg='#111111')
        logo_label.pack(side=LEFT, padx=20)

        self.setting_image = tk.PhotoImage(file='images/setting_btn_off.gif')
        setting_label = Button(menu_frame, image=self.setting_image, highlightbackground="#111111", activebackground='#111111',bd=0, bg='#111111', command=lambda: controller.show_frame("setting_Activity"))
        setting_label.pack(side=RIGHT, padx=(20, 40))

        self.control_image = tk.PhotoImage(file='images/control_btn.gif')
        control_label = Button(menu_frame, image=self.control_image, highlightbackground="#111111", activebackground='#111111',bd=0, bg='#111111', command=lambda: controller.show_frame("control_Activity"))
        control_label.pack(side=RIGHT, padx=20)

        self.main_image = tk.PhotoImage(file='images/main_btn_off.gif')
        main_label = Button(menu_frame, image=self.main_image, highlightbackground="#111111", activebackground='#111111',bd=0, bg='#111111', command=lambda: controller.show_frame("main_Activity"))
        main_label.pack(side=RIGHT, padx=20)

        # left frame
        center_frame = Frame(self, bg='#2f323b')
        center_frame.pack(fill=BOTH, side=TOP, expand=True)

        auto_mode_label = Label(center_frame, text='운전모드 제어', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        auto_mode_label.place(x=50, y=30)

        auto_frame = Frame(center_frame, bg='#2f323b')
        auto_frame.place(x=50, y=75)

        control_Activity.auto_mode_btn = Button(auto_frame, text='자동운전', fg='white', bg='#96c63e', font=('arial', 20, 'bold'), command=lambda : self.auto_control())
        control_Activity.auto_mode_btn.pack(side=LEFT)

        control_Activity.reserve_mode_btn = Button(auto_frame, text='예약운전', fg='white', bg='#96c63e', font=('arial', 20, 'bold'), command=lambda : self.reserve_control())
        control_Activity.reserve_mode_btn.pack(side=LEFT, padx=(5,0))

        control_Activity.manual_mode_btn = Button(auto_frame, text='수동운전', fg='white', bg='#007ad1', font=('arial', 20, 'bold'), command=lambda : self.manual_control())
        control_Activity.manual_mode_btn.pack(side=LEFT, padx=5)

        control_Activity.stop_mode_btn = Button(auto_frame, text='정    지', fg='white', bg='red', font=('arial', 20, 'bold'), command=lambda : self.stop_control())
        control_Activity.stop_mode_btn.pack(side=LEFT)

        heatpump_mode_label = Label(center_frame, text='히트펌프모드 제어', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        heatpump_mode_label.place(x=50, y=160)

        mode_frame = Frame(center_frame, bg='#2f323b')
        mode_frame.place(x=50, y=205)

        control_Activity.cool_mode_btn = Button(mode_frame, text='냉    방', fg='white', bg='#007ad1', font=('arial', 20, 'bold'), command=lambda : self.cool_control())
        control_Activity.cool_mode_btn.pack(side=LEFT, ipadx=2)

        control_Activity.heat_mode_btn = Button(mode_frame, text='난    방', fg='white', bg='#007ad1', font=('arial', 20, 'bold'), command=lambda : self.heat_control())
        control_Activity.heat_mode_btn.pack(side=LEFT, padx=20, ipadx=2)

        control_Activity.boil_mode_btn = Button(mode_frame, text='급    탕', fg='white', bg='#007ad1', font=('arial', 20, 'bold'), command=lambda : self.boil_control())
        control_Activity.boil_mode_btn.pack(side=LEFT, padx=(0, 20), ipadx=2)

        control_Activity.keep_mode_btn = Button(mode_frame, text='제    상', fg='white', bg='#007ad1', font=('arial', 20, 'bold'), command=lambda : self.keep_control())
        control_Activity.keep_mode_btn.pack(side=LEFT, ipadx=2)

        manual_mode_label = Label(center_frame, text='설비상태 / 수동운전모드 제어', fg='white', bg='#2f323b',
                                  font=('arial', 20, 'bold'))
        manual_mode_label.place(x=710, y=30)

        manual_frame = Frame(center_frame, bg='#2f323b')
        manual_frame.place(x=710, y=75)

        # 댐퍼
        damper_frame = Frame(manual_frame, bg='#2f323b')
        damper_frame.pack()

        damper_label = Label(damper_frame, text='댐   퍼', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        damper_label.pack(side=LEFT)

        control_Activity.damper_on_btn = Button(damper_frame, text='O   N', fg='white', bg='lightgray',
                                                font=('arial', 20, 'bold'), command=lambda: self.damper_on_control())
        control_Activity.damper_on_btn.pack(side=LEFT, padx=(78, 20))

        control_Activity.damper_off_btn = Button(damper_frame, text='O F F', fg='white', bg='lightgray',
                                                 font=('arial', 20, 'bold'), command=lambda: self.damper_off_control())
        control_Activity.damper_off_btn.pack(side=LEFT)

        Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 팬
        fan_frame = Frame(manual_frame, bg='#2f323b')
        fan_frame.pack()

        fan_label = Label(fan_frame, text='팬 흐 름 ', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        fan_label.pack(side=LEFT)

        control_Activity.fan_on_btn = Button(fan_frame, text='O   N', fg='white', bg='lightgray',
                                             font=('arial', 20, 'bold'), command=lambda: self.fan_on_control())
        control_Activity.fan_on_btn.pack(side=LEFT, padx=(51, 20))

        control_Activity.fan_off_btn = Button(fan_frame, text='O F F', fg='white', bg='lightgray',
                                              font=('arial', 20, 'bold'), command=lambda: self.fan_off_control())
        control_Activity.fan_off_btn.pack(side=LEFT)

        Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 열교환기
        exchanger_frame = Frame(manual_frame, bg='#2f323b')
        exchanger_frame.pack()

        exchanger_label = Label(exchanger_frame, text='열교환기', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        exchanger_label.pack(side=LEFT)

        control_Activity.exchanger_on_btn = Button(exchanger_frame, text='O   N', fg='white', bg='lightgray',
                                                   font=('arial', 20, 'bold'),
                                                   command=lambda: self.exchanger_on_control())
        control_Activity.exchanger_on_btn.pack(side=LEFT, padx=(48, 20))

        control_Activity.exchanger_off_btn = Button(exchanger_frame, text='O F F', fg='white', bg='lightgray',
                                                    font=('arial', 20, 'bold'),
                                                    command=lambda: self.exchanger_off_control())
        control_Activity.exchanger_off_btn.pack(side=LEFT)

        Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 버퍼탱크
        buffer_frame = Frame(manual_frame, bg='#2f323b')
        buffer_frame.pack()

        buffer_label = Label(buffer_frame, text='버퍼 탱크', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        buffer_label.pack(side=LEFT)

        control_Activity.buffer_on_btn = Button(buffer_frame, text='O   N', fg='white', bg='lightgray',
                                                font=('arial', 20, 'bold'), command=lambda: self.buffer_on_control())
        control_Activity.buffer_on_btn.pack(side=LEFT, padx=(40, 20))

        control_Activity.buffer_off_btn = Button(buffer_frame, text='O F F', fg='white', bg='lightgray',
                                                 font=('arial', 20, 'bold'), command=lambda: self.buffer_off_control())
        control_Activity.buffer_off_btn.pack(side=LEFT)

        Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 이중코일
        doublecoil_frame = Frame(manual_frame, bg='#2f323b')
        doublecoil_frame.pack()

        doublecoil_label = Label(doublecoil_frame, text='이중 코일', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        doublecoil_label.pack(side=LEFT)

        control_Activity.doublecoil_on_btn = Button(doublecoil_frame, text='O   N', fg='white', bg='lightgray',
                                                    font=('arial', 20, 'bold'),
                                                    command=lambda: self.doublecoil_on_control())
        control_Activity.doublecoil_on_btn.pack(side=LEFT, padx=(40, 20))

        control_Activity.doublecoil_off_btn = Button(doublecoil_frame, text='O F F', fg='white', bg='lightgray',
                                                     font=('arial', 20, 'bold'),
                                                     command=lambda: self.doublecoil_off_control())
        control_Activity.doublecoil_off_btn.pack(side=LEFT)

        Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 히트펌프외기
        # heatpump_outair_frame = Frame(manual_frame, bg='#2f323b')
        # heatpump_outair_frame.pack()
        #
        # heatpump_outair_label = Label(heatpump_outair_frame, text='외부 공기', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        # heatpump_outair_label.pack(side=LEFT)
        #
        # control_Activity.heatpump_outair_on_btn = Button(heatpump_outair_frame, text='O   N', fg='white', bg='lightgray', font=('arial', 20, 'bold'), command=lambda : self.heatpump_outair_on_control())
        # control_Activity.heatpump_outair_on_btn.pack(side=LEFT, padx=(40, 20))
        #
        # control_Activity.heatpump_outair_off_btn = Button(heatpump_outair_frame, text='O F F', fg='white', bg='lightgray', font=('arial', 20, 'bold'), command=lambda : self.heatpump_outair_off_control())
        # control_Activity.heatpump_outair_off_btn.pack(side=LEFT)
        #
        # Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 온수탱크
        dhw_frame = Frame(manual_frame, bg='#2f323b')
        dhw_frame.pack()

        dhw_label = Label(dhw_frame, text='온수 탱크', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        dhw_label.pack(side=LEFT)

        control_Activity.dhw_on_btn = Button(dhw_frame, text='O   N', fg='white', bg='lightgray',
                                             font=('arial', 20, 'bold'), command=lambda: self.dhw_on_control())
        control_Activity.dhw_on_btn.pack(side=LEFT, padx=(40, 20))

        control_Activity.dhw_off_btn = Button(dhw_frame, text='O F F', fg='white', bg='lightgray',
                                              font=('arial', 20, 'bold'), command=lambda: self.dhw_off_control())
        control_Activity.dhw_off_btn.pack(side=LEFT)

        Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 저장탱크
        storage_frame = Frame(manual_frame, bg='#2f323b')
        storage_frame.pack()

        storage_label = Label(storage_frame, text='저장 탱크', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        storage_label.pack(side=LEFT)

        control_Activity.storage_on_btn = Button(storage_frame, text='O   N', fg='white', bg='lightgray',
                                                 font=('arial', 20, 'bold'), command=lambda: self.storage_on_control())
        control_Activity.storage_on_btn.pack(side=LEFT, padx=(40, 20))

        control_Activity.storage_off_btn = Button(storage_frame, text='O F F', fg='white', bg='lightgray',
                                                  font=('arial', 20, 'bold'),
                                                  command=lambda: self.storage_off_control())
        control_Activity.storage_off_btn.pack(side=LEFT)

        Label(manual_frame, bg='#2f323b', font=('arial', 1)).pack()

        # 히트펌프
        heatpump_frame = Frame(manual_frame, bg='#2f323b')
        heatpump_frame.pack()

        heatpump_label = Label(heatpump_frame, text='히트 펌프', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        heatpump_label.pack(side=LEFT)

        control_Activity.heatpump_on_btn = Button(heatpump_frame, text='O   N', fg='white', bg='lightgray',
                                                  font=('arial', 20, 'bold'),
                                                  command=lambda: self.heatpump_on_control())
        control_Activity.heatpump_on_btn.pack(side=LEFT, padx=(40, 20))

        control_Activity.heatpump_off_btn = Button(heatpump_frame, text='O F F', fg='white', bg='lightgray',
                                                   font=('arial', 20, 'bold'),
                                                   command=lambda: self.heatpump_off_control())
        control_Activity.heatpump_off_btn.pack(side=LEFT)

        # 운전 예약
        start_control_label = Label(center_frame, text='예약운전 시간설정', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        start_control_label.place(x=50, y=350)

        schedule_frame = Frame(center_frame, bg='#2f323b')
        schedule_frame.place(x=50, y=400)

        control_Activity.start_hour_entry = Entry(schedule_frame, width=8, font=('arial', 15, 'bold'), justify='center')
        control_Activity.start_hour_entry.pack(side=LEFT)
        control_Activity.start_hour_entry.bind('<FocusIn>', self.insert_start_hour)

        Label(schedule_frame, text='시 ', font=('arial', 15, 'bold'), bg='#2f323b', fg='white').pack(side=LEFT, padx=2)

        control_Activity.start_min_entry = Entry(schedule_frame, width=8, font=('arial', 15, 'bold'), justify='center')
        control_Activity.start_min_entry.pack(side=LEFT)
        control_Activity.start_min_entry.bind('<FocusIn>', self.insert_start_min)

        Label(schedule_frame, text='분', font=('arial', 15, 'bold'), bg='#2f323b', fg='white').pack(side=LEFT, padx=2)
        Label(schedule_frame, text='~', font=('arial', 20, 'bold'), bg='#2f323b', fg='white').pack(side=LEFT, padx=10)

        control_Activity.end_hour_entry = Entry(schedule_frame, width=8, font=('arial', 15, 'bold'), justify='center')
        control_Activity.end_hour_entry.pack(side=LEFT)
        control_Activity.end_hour_entry.bind('<FocusIn>', self.insert_end_hour)

        Label(schedule_frame, text='시 ', font=('arial', 15, 'bold'), bg='#2f323b', fg='white').pack(side=LEFT, padx=2)

        control_Activity.end_min_entry = Entry(schedule_frame, width=8, font=('arial', 15, 'bold'), justify='center')
        control_Activity.end_min_entry.pack(side=LEFT)
        control_Activity.end_min_entry.bind('<FocusIn>', self.insert_end_min)

        Label(schedule_frame, text='분', font=('arial', 15, 'bold'), bg='#2f323b', fg='white').pack(side=LEFT, padx=2)

        self.help_image = tk.PhotoImage(file='images/help.png')
        schedule_help_btn = Label(center_frame, bg='#2f323b', image=self.help_image)
        schedule_help_btn.place(x=285, y=353)
        CreateToolTip(schedule_help_btn, '운전모드에서 예약운전 선택 시 작동합니다.', 0)

        # self.help_image = tk.PhotoImage(file='images/help.png')
        manual_help_btn = Label(center_frame, bg='#2f323b', image=self.help_image)
        manual_help_btn.place(x=1075, y=30)
        CreateToolTip(manual_help_btn, '운전모드에서 수동운전 선택 시 작동합니다.', -150)

        schedule_apply_btn = Button(center_frame, text='적  용', font=('arial', 15, 'bold'), command=lambda :self.schedule_apply())
        schedule_apply_btn.place(x=493, y=350)

        # 제어 이력
        start_control_label = Label(center_frame, text='제어이력 조회', fg='white', bg='#2f323b',
                                    font=('arial', 20, 'bold'))
        start_control_label.place(x=50, y=500)

        control_history_btn = Button(center_frame, text='제어이력보기',  fg='white', bg='lightgray', font=('arial', 20, 'bold'), command=lambda : controller.show_frame("run_Activity"))
        control_history_btn.place(x=50, y=550, height=80)

        # 에러 이력
        error_control_label = Label(center_frame, text='에러이력 조회', fg='white', bg='#2f323b', font=('arial', 20, 'bold'))
        error_control_label.place(x=270, y=500)

        control_error_btn = Button(center_frame, text='에러이력보기', fg='white', bg='lightgray', font=('arial', 20, 'bold'), command=lambda :controller.show_frame("error_Activity"))
        control_error_btn.place(x=270, y=550, height=80)

    def auto_control(self):
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
