import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

name = 'bipvt_heatpump'

bipvt_ip = ''
bipvt_port = ''

bipvt_serial_port = ''
bipvt_brate = ''
bipvt_parity = ''
bipvt_stopbit = ''

heatpump_ip = ''
heatpump_port = ''

heatpump_serial_port = ''
heatpump_brate = ''
heatpump_parity = ''
heatpump_stopbit = ''

fcu_ip = ''
fcu_port = ''

fcu_serial_port = ''
fcu_brate = ''
fcu_parity = ''
fcu_stopbit = ''


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
# keep_mode = False

start_hour = ''
start_min = ''
end_hour = ''
end_min = ''

pv_volume = ''
load_volume = ''
insolation_volume = ''
damper_volume = ''
cool_volume = ''
heat_volume = ''
dhw_volume = ''


bipvt_read = False
heatpump_read = False
fcu_read = False

day_pv_power = []
total_pv_power = []
day_load_power = []
total_load_power = []

# socket
soc_fail_count = 0
soc_connect_fail = False

openweather = 'images/weather/01d.png'

# bipvt data storage
bipvt_temp_data = [0 for i in range(62)]

bipvt_socket_client = False

## 스케줄 설정
schedule_checking = [False,False,False,False]
schedule_start = ['00:00','00:00','00:00','00:00']
schedule_end = ['00:00','00:00','00:00','00:00']

# 상세정보 저장 리스트
pv_power = []
pv_inside1 = []
pv_inside2 = []
pv_inside3 = []
pv_inner_temp = []
pv_inner_humi = []
pv_outer_temp = []
pv_outer_humi = []
buffer_temp = []
buffer_inner_temp = []
buffer_flux = []
storage_inner_temp = []
storage_outer_temp = []
storage_inner_flux = []
storage_outer_flux = []
dhw_temp = []
dhw_inner_temp = []
dhw_outer_temp = []
dhw_flux = []
heatpump_power = []
buffer_power = []
storage_power = []
dhw_power = []
heatline_power = []
out_temp = []
out_humi = []
insolation = []
wind_speed = []
rain_fall = []
inner_temp = []
inner_humi = []

pv_pre_power = ''

bipvt_packet_data = []
heatpump_packet_data = []