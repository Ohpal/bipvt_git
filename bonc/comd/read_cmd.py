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


def fcu_client():
    global fcu_client
    try:
        hosting = comd.var.fcu_ip
        porting = int(comd.var.fcu_port)

        fcu_client = ModbusTcpClient(hosting, porting)
        fcu_client.inter_char_timeout = 3

        return fcu_client
    except Exception as ex:
        print('fcu_client() Exception -> ', ex)
        comd.var.fcu_connect_status = False


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
        print('connect_heatpump() Exception -> ', ex)
        comd.var.heatpump_connect_status = False


def connect_fcu():
    global fcu_client
    try:
        fcu_connection = fcu_client.connect()
        return fcu_connection
    except Exception as ex:
        print('connect_fcu() Exception -> ', ex)
        comd.var.fcu_connect_status = False


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


def damper_on():
    global bipvt_client
    try:
        bipvt_client.write_coil(0, 1, unit=1)
    except Exception as ex:
        print('damper_on() Exception -> ', ex)


def damper_off():
    global bipvt_client
    try:
        bipvt_client.write_coil(0, 0, unit=1)
    except Exception as ex:
        print('damper_off() Exception -> ', ex)


def fan_on():
    global bipvt_client
    try:
        bipvt_client.write_coil(1, 1, unit=1)
        comd.var.fan_state = True
    except Exception as ex:
        print('fan_on() Exception -> ', ex)


def fan_off():
    global bipvt_client
    try:
        bipvt_client.write_coil(1, 0, unit=1)
        comd.var.fan_state = False
    except Exception as ex:
        print('fan_off() Exception -> ', ex)


def exchanger_on():
    global bipvt_client
    try:
        bipvt_client.write_coil(2, 1, unit=1)
    except Exception as ex:
        print('water_heat_on() Exception -> ', ex)


def exchanger_off():
    global bipvt_client
    try:
        bipvt_client.write_coil(2, 0, unit=1)
    except Exception as ex:
        print('water_heat_off() Exception -> ', ex)


def buffer_on():
    global bipvt_client
    try:
        bipvt_client.write_coil(3, 1, unit=1)
    except Exception as ex:
        print('buffer_on() Exception -> ', ex)


def buffer_off():
    global bipvt_client
    try:
        bipvt_client.write_coil(3, 0, unit=1)
    except Exception as ex:
        print('buffer_off() Exception -> ', ex)


# Heatpump Read and Write Function
def heatpump_read_data():
    global heatpump_client
    try:
        heatpump_read_data = heatpump_client.read_input_registers(0, 11, unit=1)
        assert (heatpump_read_data.function_code <= 0x84)
        return heatpump_read_data
    except Exception as ex:
        print('heatpump_read_data() Exception -> ', ex)
        comd.var.heatpump_connect_status = False


def heatpump_read_status():
    global heatpump_client
    try:
        heatpump_read_status = heatpump_client.read_coils(0, 5, unit=1)
        assert (heatpump_read_status.function_code <= 0x84)
        return heatpump_read_status
    except Exception as ex:
        print('heatpump_read_status() Exception -> ', ex)


def doublecoil_on():
    global heatpump_client
    try:
        heatpump_client.write_coil(0, 1, unit=1)
    except Exception as ex:
        print('doublecoil_on() Exception -> ', ex)


def doublecoil_off():
    global heatpump_client
    try:
        heatpump_client.write_coil(0, 0, unit=1)
    except Exception as ex:
        print('doublecoil_off() Exception -> ', ex)


def dhw_on():
    global heatpump_client
    try:
        heatpump_client.write_coil(2, 1, unit=1)
    except Exception as ex:
        print('doublecoil_on() Exception -> ', ex)


def dhw_off():
    global heatpump_client
    try:
        heatpump_client.write_coil(2, 0, unit=1)
    except Exception as ex:
        print('dhw_off() Exception -> ', ex)


def storage_on():
    global heatpump_client
    try:
        heatpump_client.write_coil(3, 1, unit=1)
    except Exception as ex:
        print('storage_on() Exception -> ', ex)


def storage_off():
    global heatpump_client
    try:
        heatpump_client.write_coil(3, 0, unit=1)
    except Exception as ex:
        print('storage_off() Exception -> ', ex)


def heatpump_on():
    global heatpump_client
    try:
        heatpump_client.write_coil(1, 1, unit=1)
    except Exception as ex:
        print('heatpump_on() Exception -> ', ex)


def heatpump_off():
    global heatpump_client
    try:
        heatpump_client.write_coil(1, 0, unit=1)
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
        heatpump_client.write_registers(1, val, unit=1)
    except Exception as ex:
        print('mode_control() Exception -> ', ex)


# FCU Read and Write Function
def fcu_read_data():
    global fcu_client
    try:
        fcu_read_data = fcu_client.read_coils(0, 24, unit=1)
        assert (fcu_read_data.function_code <= 0x84)
        return fcu_read_data
    except Exception as ex:
        print('fcu_read_data() Exception -> ', ex)


def fcu_drive_on():
    global fcu_client
    try:
        fcu_client.write_register(16, 1, unit=1)
    except Exception as ex:
        print('fcu_drive_on() Exception -> ', ex)


def fcu_drive_off():
    global fcu_client
    try:
        fcu_client.write_register(16, 0, unit=1)
    except Exception as ex:
        print('fcu_drive_off() Exception -> ', ex)


def fcu_turbo_on():
    global fcu_client
    try:
        fcu_client.write_register(12, 1, unit=1)
    except Exception as ex:
        print('fcu_turbo_on() Exception -> ', ex)


def fcu_turbo_off():
    global fcu_client
    try:
        fcu_client.write_register(12, 0, unit=1)
    except Exception as ex:
        print('fcu_turbo_off() Exception -> ', ex)


def fcu_auto_on():
    global fcu_client
    try:
        fcu_client.write_register(8, 1, unit=1)
    except Exception as ex:
        print('fcu_auto_on() Exception -> ', ex)


def fcu_auto_off():
    global fcu_client
    try:
        fcu_client.write_register(8, 0, unit=1)
    except Exception as ex:
        print('fcu_auto_off() Exception -> ', ex)


def fcu_cool_on():
    global fcu_client
    try:
        fcu_client.write_register(1, 1, unit=1)
    except Exception as ex:
        print('fcu_cool_on() Exception -> ', ex)


def fcu_hot_on():
    global fcu_client
    try:
        fcu_client.write_register(2, 1, unit=1)
    except Exception as ex:
        print('fcu_hot_on() Exception -> ', ex)


def fcu_wind_on():
    global fcu_client
    try:
        fcu_client.write_register(3, 1, unit=1)
    except Exception as ex:
        print('fcu_wind_on() Exception -> ', ex)


def fcu_blow_on():
    global fcu_client
    try:
        fcu_client.write_register(3, 1, unit=1)
    except Exception as ex:
        print('fcu_wind_on() Exception -> ', ex)


def fcu_fan_off():
    global fcu_client
    try:
        fcu_client.write_register(4, 1, unit=1)
    except Exception as ex:
        print('fcu_fan_off() Exception -> ', ex)


def fcu_fan_low():
    global fcu_client
    try:
        fcu_client.write_register(5, 1, unit=1)
    except Exception as ex:
        print('fcu_fan_low() Exception -> ', ex)


def fcu_fan_middle():
    global fcu_client
    try:
        fcu_client.write_register(6, 1, unit=1)
    except Exception as ex:
        print('fcu_fan_middle() Exception -> ', ex)


def fcu_fan_high():
    global fcu_client
    try:
        fcu_client.write_register(7, 1, unit=1)
    except Exception as ex:
        print('fcu_fan_high() Exception -> ', ex)


def fcu_swing_on():
    global fcu_client
    try:
        fcu_client.write_register(13, 1, unit=1)
    except Exception as ex:
        print('fcu_swing_on() Exception -> ', ex)


def fcu_swing_off():
    global fcu_client
    try:
        fcu_client.write_register(13, 0, unit=1)
    except Exception as ex:
        print('fcu_swing_off() Exception -> ', ex)


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

    if comd.var.bipvt_connect_status:
        exchanger_off()
        fan_off()
        buffer_off()
        damper_off()

    if comd.var.heatpump_connect_status:
        dhw_off()
        doublecoil_off()
        heatpump_off()
        storage_off()
