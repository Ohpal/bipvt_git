import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")


from tkinter import *
import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
import datetime

def setFont(size=15):
    font = 'SCDream5', size, 'bold'
    return font



class put_start_hour_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)
            # print(value, "pressed")

        def ok_pressed():
            try:
                self.pin = self.e1.get()
                print("pin", self.pin)

                if not 0 <= int(self.pin) <= 23:
                    raise

                if 0 < len(self.pin) < 2:
                    self.pin = '0' + str(self.pin)

                if len(self.pin) > 2:
                    raise

                self.master.start_hour_entry.delete(0, END)
                self.master.start_hour_entry.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except Exception as ex:
                print('??',ex)
                tk.messagebox.showwarning('시 범위 에러', '0~23 사이의 값을 입력하세요')
                self.e1.delete(0, END)

        self.geometry("400x400")

        # insert data

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22)
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_start_min_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)
            # print(value, "pressed")

        def ok_pressed():
            try:
                self.pin = self.e1.get()
                print("pin", self.pin)

                if not 0 <= int(self.pin) <= 59:
                    raise

                if 0 < len(self.pin) < 2:
                    self.pin = '0' + str(self.pin)

                if len(self.pin) > 2:
                    raise

                self.master.start_min_entry.delete(0, END)
                self.master.start_min_entry.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('분 범위 에러', '0~59 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        # insert data

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22)
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_end_hour_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)
            # print(value, "pressed")

        def ok_pressed():
            try:
                self.pin = self.e1.get()
                print("pin", self.pin)

                if not 0 <= int(self.pin) <= 23:
                    raise

                if 0 < len(self.pin) < 2:
                    self.pin = '0' + str(self.pin)

                if len(self.pin) > 2:
                    raise
                self.master.end_hour_entry.delete(0, END)
                self.master.end_hour_entry.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('시 범위 에러', '0~23 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        # insert data

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22)
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_end_min_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)
            # print(value, "pressed")

        def ok_pressed():
            try:
                self.pin = self.e1.get()
                print("pin", self.pin)

                if not 0 <= int(self.pin) <= 59:
                    raise

                if 0 < len(self.pin) < 2:
                    self.pin = '0' + str(self.pin)

                if len(self.pin) > 2:
                    raise

                self.master.end_min_entry.delete(0, END)
                self.master.end_min_entry.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('분 범위 에러', '0~59 사이의 값을 입력하세요')
                self.e1.delete(0, END)

        self.geometry("400x400")

        # insert data

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22)
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_ip_value1(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 223:
                    raise

                self.master.bipvt_entry1.delete(0, END)
                self.master.bipvt_entry1.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~223 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_ip_value2(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.bipvt_entry2.delete(0, END)
                self.master.bipvt_entry2.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_ip_value3(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.bipvt_entry3.delete(0, END)
                self.master.bipvt_entry3.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_ip_value4(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.bipvt_entry4.delete(0, END)
                self.master.bipvt_entry4.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_ip_value1(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 223:
                    raise

                self.master.heatpump_entry1.delete(0, END)
                self.master.heatpump_entry1.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~223 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_ip_value2(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.heatpump_entry2.delete(0, END)
                self.master.heatpump_entry2.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_ip_value3(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.heatpump_entry3.delete(0, END)
                self.master.heatpump_entry3.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_ip_value4(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.heatpump_entry4.delete(0, END)
                self.master.heatpump_entry4.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_ip_value1(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 223:
                    raise

                self.master.fcu_entry1.delete(0, END)
                self.master.fcu_entry1.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~223 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        print(self.winfo_screenwidth()/2, self.winfo_screenheight()/2)
        self.geometry("400x400+960+540")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_ip_value2(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.fcu_entry2.delete(0, END)
                self.master.fcu_entry2.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_ip_value3(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.fcu_entry3.delete(0, END)
                self.master.fcu_entry3.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_ip_value4(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.fcu_entry4.delete(0, END)
                self.master.fcu_entry4.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('IP 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_port_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)

                if not 0 <= int(self.pin) <= 65535:
                    raise

                self.master.bipvt_entry5.delete(0, END)
                self.master.bipvt_entry5.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~65535 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_port_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 65535:
                    raise

                self.master.heatpump_entry5.delete(0, END)
                self.master.heatpump_entry5.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~65535 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_port_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 65535:
                    raise

                self.master.fcu_entry5.delete(0, END)
                self.master.fcu_entry5.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~65535 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)

# BIPVT 시리얼 입력
class put_bipvt_serial_value1(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.bipvt_serial_entry1.delete(0, END)
                self.master.bipvt_serial_entry1.insert("end", 'COM'+self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_serial_value2(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.bipvt_serial_entry2.delete(0, END)
                self.master.bipvt_serial_entry2.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_serial_value3(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.bipvt_serial_entry3.delete(0, END)
                self.master.bipvt_serial_entry3.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_bipvt_serial_value4(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.bipvt_serial_entry4.delete(0, END)
                self.master.bipvt_serial_entry4.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)

# 히트펌프 시리얼 입력
class put_heatpump_serial_value1(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.heatpump_serial_entry1.delete(0, END)
                self.master.heatpump_serial_entry1.insert("end", 'COM'+self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_serial_value2(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.heatpump_serial_entry2.delete(0, END)
                self.master.heatpump_serial_entry2.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_serial_value3(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.heatpump_serial_entry3.delete(0, END)
                self.master.heatpump_serial_entry3.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_heatpump_serial_value4(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.heatpump_serial_entry4.delete(0, END)
                self.master.heatpump_serial_entry4.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


# FCU 시리얼 입력
class put_fcu_serial_value1(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                if not 0 <= int(self.pin) <= 255:
                    raise

                self.master.fcu_serial_entry1.delete(0, END)
                self.master.fcu_serial_entry1.insert("end", 'COM'+self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_serial_value2(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.fcu_serial_entry2.delete(0, END)
                self.master.fcu_serial_entry2.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_serial_value3(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.fcu_serial_entry3.delete(0, END)
                self.master.fcu_serial_entry3.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_fcu_serial_value4(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)
                # if not 0 <= int(self.pin) <= 255:
                #     raise

                self.master.fcu_serial_entry4.delete(0, END)
                self.master.fcu_serial_entry4.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('PORT 범위 에러', '0~255 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=setFont()).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=setFont(), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'), font=setFont())
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'), font=setFont())
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'), font=setFont())
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'), font=setFont())
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'), font=setFont())
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'), font=setFont())
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'), font=setFont())
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'), font=setFont())
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'), font=setFont())
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'), font=setFont())
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_dot = tk.Button(master, text='.', command=lambda: button_pressed('.'), font=setFont())
        self.btn_dot.grid(row=5, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear, font=setFont())
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=setFont(), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)


class put_insolation_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)

                if not 350 <= int(self.pin) <= 450:
                    raise

                self.master.insolation_value.delete(0, END)
                self.master.insolation_value.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('조도 범위 에러', '350~450 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=('SCDream5', 13)).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=('SCDream5', 12), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'))
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'))
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'))
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'))
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'))
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'))
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'))
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'))
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'))
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'))
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear)
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=('SCDream5', 13), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)

class put_bipvt_inner_temp_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)

                if not 35 <= int(self.pin) <= 45:
                    raise

                self.master.bipvt_inner_temp_value.delete(0, END)
                self.master.bipvt_inner_temp_value.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('BIPVT 내부 온도 설정 에러', '35~45 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=('SCDream5', 13)).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=('SCDream5', 12), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'))
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'))
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'))
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'))
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'))
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'))
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'))
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'))
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'))
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'))
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear)
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=('SCDream5', 13), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)

class put_cool_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)

                if not 0 <= int(self.pin) <= 10:
                    raise

                self.master.cool_value.delete(0, END)
                self.master.cool_value.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('냉방 온도 설정 에러', '0~10 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=('SCDream5', 13)).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=('SCDream5', 12), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'))
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'))
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'))
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'))
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'))
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'))
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'))
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'))
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'))
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'))
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear)
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=('SCDream5', 13), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)

class put_hot_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)

                if not 30 <= int(self.pin) <= 40:
                    raise

                self.master.hot_value.delete(0, END)
                self.master.hot_value.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('난방 온도 설정 에러', '30~40 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=('SCDream5', 13)).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=('SCDream5', 12), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'))
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'))
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'))
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'))
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'))
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'))
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'))
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'))
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'))
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'))
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear)
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=('SCDream5', 13), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)

class put_dhw_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)

                if not 40 <= int(self.pin) <= 50:
                    raise

                self.master.dhw_value.delete(0, END)
                self.master.dhw_value.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('급탕 온도 설정 에러', '40~50 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=('SCDream5', 13)).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=('SCDream5', 12), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'))
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'))
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'))
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'))
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'))
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'))
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'))
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'))
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'))
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'))
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear)
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=('SCDream5', 13), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)

class put_doublecoil_value(tkinter.simpledialog.Dialog):
    def body(self, master):
        def clear():
            self.e1.delete(0, END)
            return

        def button_pressed(value):
            self.e1.insert("end", value)

        def ok_pressed():
            try:
                self.pin = self.e1.get()

                print("pin", self.pin)

                if not 0 <= int(self.pin) <= 5:
                    raise

                self.master.doublecoil_value.delete(0, END)
                self.master.doublecoil_value.insert("end", self.pin)
                self.destroy()
                self.master.focus()
            except:
                tk.messagebox.showwarning('이중코일 동작온도 설정 에러', '0~5 사이의 값을 입력하세요.')
                self.e1.delete(0, END)

        self.geometry("400x400")

        tk.Label(master, text="값을 입력하세요", font=('SCDream5', 13)).grid(row=0, column=0, columnspan=3)

        self.e1 = tk.Entry(master, bg='#ffffff', fg='#2a2f35', font=('SCDream5', 12), width=22, justify='center')
        self.e1.grid(row=1, column=0, columnspan=3)
        # return self.insert_value  # initial focus
        self.btn1 = tk.Button(master, text='1', command=lambda: button_pressed('1'))
        self.btn1.grid(row=2, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn2 = tk.Button(master, text='2', command=lambda: button_pressed('2'))
        self.btn2.grid(row=2, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn3 = tk.Button(master, text='3', command=lambda: button_pressed('3'))
        self.btn3.grid(row=2, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn4 = tk.Button(master, text='4', command=lambda: button_pressed('4'))
        self.btn4.grid(row=3, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn5 = tk.Button(master, text='5', command=lambda: button_pressed('5'))
        self.btn5.grid(row=3, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn6 = tk.Button(master, text='6', command=lambda: button_pressed('6'))
        self.btn6.grid(row=3, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn7 = tk.Button(master, text='7', command=lambda: button_pressed('7'))
        self.btn7.grid(row=4, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn8 = tk.Button(master, text='8', command=lambda: button_pressed('8'))
        self.btn8.grid(row=4, column=1, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn9 = tk.Button(master, text='9', command=lambda: button_pressed('9'))
        self.btn9.grid(row=4, column=2, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_0 = tk.Button(master, text='0', command=lambda: button_pressed('0'))
        self.btn_0.grid(row=5, column=0, ipadx=16, ipady=8, padx=3, pady=3)

        self.btn_del = tk.Button(master, text='DEL', command=clear)
        self.btn_del.grid(row=5, column=1, ipadx=45, ipady=8, padx=3, pady=3, columnspan=2)

        self.btn_ok = tk.Button(master, text='확인', bg='#2a2f35', fg='#ffffff', font=('SCDream5', 13), command=ok_pressed)
        self.btn_ok.grid(row=6, column=0, ipadx=82, ipady=8, padx=3, pady=4, columnspan=3)