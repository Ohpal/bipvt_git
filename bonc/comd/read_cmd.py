import os, sys
import comd.var

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.client.sync import ModbusSerialClient
import comd.var

bipvt_client = False
heatpump_client = False
fcu_client = False


# Modbus Client Function
def bipvt_client():
    global bipvt_client

    try:
        hosting = comd.var.bipvt_ip
        porting = int(comd.var.bipvt_port)

        bipvt_client = ModbusTcpClient(hosting, porting)
        bipvt_client.inter_char_timeout = 3

        return bipvt_client
    except Exception as ex:
        print('bipvt_client() Exception -> ', ex)
        comd.var.bipvt_connect_status = False


def heatpump_client():
    global heatpump_client
    try:
        hosting = comd.var.heatpump_ip
        porting = int(comd.var.heatpump_port)

        heatpump_client = ModbusTcpClient(hosting, porting)
        heatpump_client.inter_char_timeout = 3

        return heatpump_client
    except Exception as ex:
        print('heatpump_clinet() Exception -> ', ex)
        comd.var.heatpump_connect_status = False


def heatpump_serial_client():
    global heatpump_client
    try:
        serial_porting = comd.var.heatpump_serial_port
        brate = comd.var.heatpump_brate
        parity = 'N'
        stopbit = comd.var.heatpump_stopbit

        heatpump_client = ModbusSerialClient(method='rtu', port=serial_porting, baudrate=int(brate), stopbits=int(stopbit), parity=parity)
        heatpump_client.inter_char_timeout = 3

        return heatpump_client
    except Exception as ex:
        print('heatpump_serial_client() Exception -> ', ex)
        comd.var.heatpump_connect_status = False


# Modbus Connection Function
def connect_bipvt():
    global bipvt_client
    try:
        bipvt_connection = bipvt_client.connect()
        return bipvt_connection
    except Exception as ex:
        print('connect_bipvt() Exception -> ', ex)
        comd.var.bipvt_connect_status = False


def connect_heatpump():
    global heatpump_client
    try:
        heatpump_connection = heatpump_client.connect()
        return heatpump_connection
    except Exception as ex:
        # print('connect_heatpump() Exception -> ', ex)
        comd.var.heatpump_connect_status = False


# BIPVT Data Read and Write Function
def bipvt_read_data():
    global bipvt_client
    try:
        bipvt_read_data = bipvt_client.read_input_registers(0, 10, unit=1)
        assert (bipvt_read_data.function_code <= 0x84)
        return bipvt_read_data
    except Exception as ex:
        print('bipvt_read_data() Exception -> ', ex)
        comd.var.bipvt_connect_status = False


def bipvt_read_status():
    global bipvt_client
    try:
        bipvt_read_status = bipvt_client.read_coils(0, 5, unit=1)
        assert (bipvt_read_status.function_code <= 0x84)
        return bipvt_read_status
    except Exception as ex:
        print('bipvt_read_status() Exception -> ', ex)


# Heatpump Read and Write Function
def heatpump_read_data():
    global heatpump_client
    try:
        heatpump_read_data = heatpump_client.read_input_registers(1, 8, unit=1)
        assert (heatpump_read_data.function_code <= 0x84)
        return heatpump_read_data
    except Exception as ex:
        print('heatpump_read_data() Exception -> ', ex)
        comd.var.heatpump_connect_status = False


def heatpump_mode_data():
    global heatpump_client
    try:
        heatpump_read_mode = heatpump_client.read_holding_registers(10, 1, unit=1)
        assert(heatpump_read_mode.function_code <= 0x84)
        return heatpump_read_mode
    except Exception as ex:
        print('heatpump_mode_data() Exception -> ', ex)
        comd.var.heatpump_connect_status = False

def heatpump_mode_status():
    global heatpump_client
    try:
        heatpump_mode_status = heatpump_client.read_holding_registers(18, 1, unit=1)
        assert(heatpump_mode_status.function_code <= 0x84)
        return heatpump_mode_status
    except Exception as ex:
        print('heatpump_mode_status() Exception ->', ex)



def heatpump_read_status():
    global heatpump_client
    try:
        heatpump_read_status = heatpump_client.read_coils(1, 1, unit=1)
        assert (heatpump_read_status.function_code <= 0x84)
        return heatpump_read_status
    except Exception as ex:
        print('heatpump_read_status() Exception -> ', ex)


def heatpump_remote_status():
    global heatpump_client
    try:
        heatpump_remote_status = heatpump_client.read_coils(3, 1, unit=1)
        assert(heatpump_remote_status.function_code <= 0x84)
        return heatpump_remote_status
    except Exception as ex:
        print('heatpump_remote_status() Exception -> ', ex)


def heatpump_temp_setting():
    global heatpump_client
    try:
        heatpump_read_setting = heatpump_client.read_holding_registers(11, 7, unit=1)
        assert (heatpump_read_setting.function_code <= 0x84)
        return heatpump_read_setting
    except Exception as ex:
        print('heatpump_temp_setting() Exception -> ', ex)


def heatpump_cool_setTemp(val):
    global heatpump_client
    try:
        heatpump_client.write_registers(11, val * 10, unit=1)
    except Exception as ex:
        print('heatpump_cool_setTemp() Exception -> ', ex)


def heatpump_hot_setTemp(val):
    global heatpump_client
    try:
        heatpump_client.write_registers(12, val * 10, unit=1)
    except Exception as ex:
        print('heatpump_hot_setTemp() Exception -> ', ex)


def heatpump_dhwcool_setTemp(val):
    global heatpump_client
    try:
        heatpump_client.write_registers(14, val * 10, unit=1)
    except Exception as ex:
        print('heatpump_dhwcool_setTemp() Exception -> ', ex)


def heatpump_dhwhot_setTemp(val):
    global heatpump_client
    try:
        heatpump_client.write_registers(15, val * 10, unit=1)
    except Exception as ex:
        print('heatpump_dhwhot_setTemp() Exception -> ', ex)


def heatpump_on():
    global heatpump_client
    try:
        heatpump_client.write_coil(3, 1, unit=1)
        print('@@@@@@@@@???????????? ON')
    except Exception as ex:
        print('heatpump_on() Exception -> ', ex)


def heatpump_off():
    global heatpump_client
    try:
        heatpump_client.write_coil(3, 0, unit=1)
        print('@@@@@@@@???????????? OFF')
    except Exception as ex:
        print('heatpump_off() Exception -> ', ex)


def drive_on():
    global heatpump_client
    try:
        heatpump_client.write_register(0, 1, unit=1)
    except Exception as ex:
        print('drive_on() Exception -> ', ex)


def drive_off():
    global heatpump_client
    try:
        heatpump_client.write_register(0, 0, unit=1)
    except Exception as ex:
        print('drive_off() Exception -> ', ex)


def mode_control(val):
    global heatpump_client
    try:
        if val == 0:
            mode = '??????'
        elif val == 1:
            mode ='??????'
        elif val == 2:
            mode = '??????'
        elif val == 3:
            mode = '??????'
        heatpump_client.write_registers(18, val, unit=1)
        print('@@@@@@@@@@@@@',mode, '??????')
    except Exception as ex:
        print('mode_control() Exception -> ', ex)


# System Read and Write Function
def auto_mode():
    comd.var.auto_mode = True
    comd.var.reserve_mode = False
    comd.var.manual_mode = False
    comd.var.stop_mode = False


def reserve_mode():
    comd.var.auto_mode = False
    comd.var.reserve_mode = True
    comd.var.manual_mode = False
    comd.var.stop_mode = False


def manual_mode():
    comd.var.auto_mode = False
    comd.var.reserve_mode = False
    comd.var.manual_mode = True
    comd.var.stop_mode = False


def stop_mode():
    comd.var.auto_mode = False
    comd.var.reserve_mode = False
    comd.var.manual_mode = False
    comd.var.stop_mode = True

    # if comd.var.bipvt_connect_status:
    #     exchanger_off()
    #     fan_off()
    #     buffer_off()
    #     damper_off()
    #
    if comd.var.heatpump_connect_status:
        heatpump_off()
    #     dhw_off()
    #     doublecoil_off()
    #     heatpump_off()
    #     storage_off()
