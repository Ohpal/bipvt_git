import os, sys

# from dbm.ndbm import _dbm

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

import tkinter as tk
import threading
import datetime

import db.sqlite_connect
import comd.main_cmd
import comd.var

import ui.main_Activity
import ui.detail_Activity
import ui.setting_Activity
import ui.control_Activity
import ui.run_Activity
import ui.error_Activity
import notification.error_alert_notification


def now_time():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    return now


def error_len():
    cnt = db.sqlite_connect.error_count()
    return cnt


class start_app(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # self.geometry('1280x720')
        # self.geometry('1024x1280')
        self.geometry('1080x1920')
        self.configure(background='#2f323b')
        self.title('BIPVT-HeatPump')
        self.iconbitmap('images/b_logo.ico')
        # self.attributes('-fullscreen', True)

        container = tk.Frame(self)
        container.config(background='#111111')
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        mainActivity = ui.main_Activity.main_Activity
        detailActivity = ui.detail_Activity.detail_Activity
        controlActivity = ui.control_Activity.control_Activity
        settingActivity = ui.setting_Activity.setting_Activity
        runActivity = ui.run_Activity.run_Activity
        errorActivity = ui.error_Activity.error_Activity

        self.frames = {}

        for F in (mainActivity, detailActivity, controlActivity, settingActivity, runActivity, errorActivity):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame("main_Activity")

        # protocol setting by sqlite3
        db.sqlite_connect.setting_protocol()
        # db.sqlite_connect.setting_schedule()
        # db.sqlite_connect.setting_system()

        # # connection_check
        # bipvt_connection = comd.read_cmd.bipvt_client().connect()
        # print('BIPVT Connection : ', bipvt_connection)
        # if not bipvt_connection:
        #     # notification.error_alert_notification.bipvt_connection_error()
        #     comd.var.bipvt_connect_status = False
        # else:
        #     comd.var.bipvt_connect_status = True
        #
        # heatpump_connection = comd.read_cmd.heatpump_client().connect()
        # print('HeatPump Connection : ', heatpump_connection)
        # if not heatpump_connection:
        #     # notification.error_alert_notification.heatpump_connection_error()
        #     comd.var.hydro_connect_status = False
        # else:
        #     comd.var.hydro_connect_status = True

        db.sqlite_connect.automode_select()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        self.now_frame = page_name
        frame.tkraise()

    def setInterval(self, func, time):
        e = threading.Event()
        while not e.wait(time):
            func()

    def data_receive(self):
        try:
            comd.main_cmd.mainLoop()
        except Exception as ex:
            print('mainLoop_error', ex)

    def facility_connect(self):
        try:
            if not comd.var.bipvt_connect_status:
                bipvt_connection = comd.read_cmd.connect_bipvt()
                print('BIPVT Connection : ', bipvt_connection)
                if bipvt_connection:
                    comd.var.bipvt_connect_status = True
                    comd.var.bipvt_error = False
                else:
                    if not comd.var.bipvt_error:
                        db.sqlite_connect.error_insert('BIPVT', '통신 에러', now_time())
                        ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                           values=(now_time(), 'BIPVT', '통신 에러'))
                        comd.var.bipvt_error = True

            if not comd.var.heatpump_connect_status:
                heatpump_connection = comd.read_cmd.connect_heatpump()
                print('HeatPump Connection : ', heatpump_connection)
                if heatpump_connection:
                    comd.var.heatpump_connect_status = True
                    comd.var.heatpump_error = False
                else:
                    if not comd.var.heatpump_error:
                        db.sqlite_connect.error_insert('히트펌프', '통신 에러', now_time())
                        ui.error_Activity.error_Activity.error_list.insert('', index=0, text=int(error_len()),
                                                                           values=(now_time(), '히트펌프', '통신 에러'))
                        comd.var.heatpump_error = True

        except Exception as ex:
            print('facility_connect_error ', ex)

    def hot_mode_save(self):
        try:
            if comd.var.hot_mode and (comd.var.auto_mode or comd.var.reserve_mode):
                comd.var.hot_time = comd.var.hot_time + 1
            # else:
            # print(comd.var.hot_mode, comd.var.auto_mode, comd.var.reserve_mode)

        except Exception as ex:
            print('Jesang ERR', ex)


if __name__ == '__main__':
    try:
        # database check
        # db.sqlite_connect.start_check_lite()
        #
        # db.sqlite_connect.select_protocol()
        # db.sqlite_connect.schedule_select()
        # db.sqlite_connect.automode_select()
        # db.sqlite_connect.select_system()

        app = start_app()
        thread = threading.Thread(target=app.setInterval, args=(app.data_receive, 0.9))
        thread.setDaemon(True)
        thread.start()
        thread2 = threading.Thread(target=app.setInterval, args=(app.facility_connect, 1.0))
        thread2.setDaemon(True)
        thread2.start()
        thread3 = threading.Thread(target=app.setInterval, args=(app.hot_mode_save, 1.0))
        thread3.setDaemon(True)
        thread3.start()
        app.mainloop()

    except Exception as ex:
        print('mainLoop', ex)
