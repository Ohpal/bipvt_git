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

from time import sleep
import tkinter.simpledialog
import tkinter.messagebox
import comd.var


class run_Activity(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 상단 메뉴바
        menu_frame = Frame(self, bg='#111111')
        menu_frame.pack(fill=X, ipady=5)

        self.logo_image = tk.PhotoImage(file="images/bonc.png")
        logo_label = Label(menu_frame, image=self.logo_image, highlightbackground="#111111", activebackground='#111111',
                           bd=0, bg='#111111')
        logo_label.pack(side=LEFT, padx=20)

        self.setting_image = tk.PhotoImage(file='images/setting_btn_off.gif')
        setting_label = Button(menu_frame, image=self.setting_image, highlightbackground="#111111",
                               activebackground='#111111', bd=0, bg='#111111',
                               command=lambda: controller.show_frame("setting_Activity"))
        setting_label.pack(side=RIGHT, padx=(20, 40))

        self.control_image = tk.PhotoImage(file='images/control_btn.gif')
        control_label = Button(menu_frame, image=self.control_image, highlightbackground="#111111",
                               activebackground='#111111', bd=0, bg='#111111',
                               command=lambda: controller.show_frame("control_Activity"))
        control_label.pack(side=RIGHT, padx=20)

        self.main_image = tk.PhotoImage(file='images/main_btn_off.gif')
        main_label = Button(menu_frame, image=self.main_image, highlightbackground="#111111",
                            activebackground='#111111', bd=0, bg='#111111',
                            command=lambda: controller.show_frame("main_Activity"))
        main_label.pack(side=RIGHT, padx=20)

        # left frame
        center_frame = Frame(self, bg='#2f323b')
        center_frame.pack(fill=BOTH, side=TOP, expand=True)

        top_set_contents_frame = Frame(center_frame, bg="#2f323b", highlightbackground="#2f323b")
        top_set_contents_frame.pack(side=TOP, ipadx=0, padx=10, pady=10)

        # run_list_Title
        battery_state_label = Label(top_set_contents_frame, text="제어이력 조회", font=('arial', 15, 'bold'),
                                    fg='#23A96E', bg='#2f323b')
        battery_state_label.pack()

        # height black
        label1 = Label(top_set_contents_frame, bg="#2f323b")
        label1.pack()

        run_xframe = Frame(top_set_contents_frame, bg="#2f323b")
        run_xframe.pack(fill=BOTH, expand=True)

        # height black
        label1 = Label(top_set_contents_frame, bg="#2f323b")
        label1.pack()

        run_Activity.run_list = ttk.Treeview(run_xframe, columns=['1', '2', '3'], height=27)
        run_Activity.run_list.pack(side=LEFT, fill=BOTH)

        style = ttk.Style()

        run_scroll = ttk.Scrollbar(run_xframe, orient='vertical', command=run_Activity.run_list.yview)
        run_Activity.run_list.configure(yscrollcommand=run_scroll.set)
        run_scroll.pack(expand=True, side=LEFT, fill=Y)


        style.configure('Treeview.Heading', font=('arial', 16))
        style.configure('Treeview', font=('arial', 14))

        run_Activity.run_list.heading('#0', text='순번')
        run_Activity.run_list.heading('#1', text='일시')
        run_Activity.run_list.heading('#2', text='항목')
        run_Activity.run_list.heading('#3', text='내용')

        run_Activity.run_list.column('#0', width=100, anchor='center')
        run_Activity.run_list.column('#1', width=300, anchor='center')
        run_Activity.run_list.column('#2', width=300, anchor='center')
        run_Activity.run_list.column('#3', width=400, anchor='center')

        rows = db.sqlite_connect.run_all()
        run_len = len(rows)

        for row in rows:
            run_Activity.run_list.insert('', 'end', text=run_len, values=(row[2], row[0], row[1]))

            run_len = run_len - 1


