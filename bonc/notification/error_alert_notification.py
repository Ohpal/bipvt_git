import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

# fault and warning error message

# pcs fault
def pcs_fault(errorText):
    top = tkinter.Toplevel()
    top.attributes('-topmost', True)
    top.focus_force()
    top.title('PCS_FAULT')
    frame = Frame(top)
    frame.grid()

    error_massage = Label(frame, text=errorText, font=("alrial", 13), fg='red', padx=20, pady=20)
    error_massage.grid(row=1, column=3, sticky=N)
    okbtn = Button(frame, text="OK", font=("alrial", 12), command=top.destroy)
    okbtn.grid(row=2, column=3)


# battery_warning
def battery_warning(errorText):
    top = tkinter.Toplevel()
    top.attributes('-topmost', True)
    top.focus_force()
    top.title('BATTERY_WARNING')
    frame = Frame(top)
    frame.grid()

    error_massage = Label(frame, text=errorText, font=("alrial", 13), fg='red', padx=20, pady=20)
    error_massage.grid(row=1, column=3, sticky=N)
    okbtn = Button(frame, text="OK", font=("alrial", 12), command=top.destroy)
    okbtn.grid(row=2, column=3)


# battery_fault
def battery_fault(errorText):
    top = tkinter.Toplevel()
    top.attributes('-topmost', True)
    top.focus_force()
    top.title('BATTERY_FAULT')
    frame = Frame(top)
    frame.grid()

    error_massage = Label(frame, text=errorText, font=("alrial", 13), fg='red', padx=20, pady=20)
    error_massage.grid(row=1, column=3, sticky=N)
    okbtn = Button(frame, text="OK", font=("alrial", 12), command=top.destroy)
    okbtn.grid(row=2, column=3)


# grid_link fault
def grid_link_fault(errorText):
    top = tkinter.Toplevel()
    top.attributes('-topmost', True)
    top.focus_force()
    top.title('Grid Link Fault')
    frame = Frame(top)
    frame.grid()

    error_massage = Label(frame, text=errorText, font=("arial", 13), fg='red', padx=20, pady=20)
    error_massage.grid(row=1, column=3, sticky=N)
    okbtn = Button(frame, text="OK", font=("arial", 12), command=top.destroy)
    okbtn.grid(row=2, column=3)


# connection error
def bipvt_connection_error():
    top = tkinter.Toplevel()
    top.attributes('-topmost', True)
    top.focus_force()
    top.title('BIPVT 연결오류')
    frame = Frame(top)
    frame.grid()

    error_massage = Label(frame, text="BIPVT 연결상태를 확인하세요.", font=("arial", 13), padx=20, pady=20)
    error_massage.grid(row=1, column=3, sticky=N)
    okbtn = Button(frame, text="OK", font=("arial", 12), command=top.destroy)
    okbtn.grid(row=2, column=3)


def heatpump_connection_error():
    top = tkinter.Toplevel()
    top.attributes('-topmost', True)
    top.focus_force()
    top.title('히트펌프 연결오류')
    frame = Frame(top)
    frame.grid()

    error_massage = Label(frame, text="히트펌프 연결상태를 확인하세요.", font=("arial", 13), padx=20, pady=20)
    error_massage.grid(row=1, column=3, sticky=N)
    okbtn = Button(frame, text="OK", font=("arial", 12), command=top.destroy)
    okbtn.grid(row=2, column=3)
