import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

name = 'bipvt_heatpump'

bipvt_ip = ''
bipvt_port = ''

heatpump_ip = ''
heatpump_port = ''

fcu_ip = ''
fcu_port = ''

bipvt_connect_status = False
heatpump_connect_status = False
fcu_connect_status = False

bipvt_error = False
heatpump_error = False
fcu_error = False

fan_state = False

auto_mode = False
manual_mode = False
stop_mode = False
reserve_mode = False
reserve_trigger = False

hot_mode = False
hot_time = 0
keep_mode = False

start_hour = ''
start_min = ''
end_hour = ''
end_min = ''

insolation_value = ''
inner_temp_value = ''
cool_value = ''
hot_value = ''
dhw_value = ''
doublecoil_value = ''

bipvt_read = False
heatpump_read = False
fcu_read = False

day_pv_power = []
total_pv_power = []
day_load_power = []
total_load_power = []