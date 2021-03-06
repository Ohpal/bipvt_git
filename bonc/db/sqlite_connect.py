import os, sys

if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    os.chdir("/home/ubuntu/bipvt/smart_grid_v1/bonc")

import sqlite3
import ui.setting_Activity
import ui.control_Activity
import comd.var
import comd.read_cmd


db_name = 'embedded_ems.db'

protocol_table_query = "CREATE TABLE IF NOT EXISTS protocol(" \
                       "id INTEGER PRIMARY KEY, " \
                        "bipvt_ip             varchar(32)," \
                        "bipvt_port           varchar(32)," \
                        "heatpump_ip          varchar(32)," \
                        "heatpump_port        varchar(32)," \
                        "bipvt_serial_port    varchar(32) default 0," \
                        "bipvt_brate          varchar(32) default 0," \
                        "bipvt_parity         varchar(32) default 0," \
                        "bipvt_stopbit        varchar(32) default 0," \
                        "bipvt_type           varchar(32)," \
                        "heatpump_type        varchar(32)," \
                        "heatpump_serial_port varchar(32) default 0," \
                        "heatpump_brate       varchar(32) default 0," \
                        "heatpump_parity      varchar(32) default 0," \
                        "heatpump_stopbit     varchar(32) default 0" \
                       ")"

schedule_table_query = "CREATE TABLE IF NOT EXISTS schedules(" \
                       "id INTEGER PRIMARY KEY," \
                       "start_hour VARCHAR(30)," \
                       "start_min VARCHAR(30)," \
                       "end_hour VARCHAR(30)," \
                       "end_min VARCHAR(30))"

control_table_query = "CREATE TABLE IF NOT EXISTS controls(" \
                      "id INTEGER PRIMARY KEY," \
                      "automode varchar(32)"\
                      ")"

history_table_query = 'CREATE TABLE IF NOT EXISTS history(' \
                      'id INTEGER PRIMARY KEY,' \
                      'item VARCHAR(30),' \
                      'value VARCHAR(30),' \
                      'd_time VARCHAR(30))'

error_table_query = 'CREATE TABLE IF NOT EXISTS error(' \
                      'id INTEGER PRIMARY KEY,' \
                      'item VARCHAR(30),' \
                      'value VARCHAR(30),' \
                      'd_time VARCHAR(30))'

setting_table_query = "CREATE TABLE IF NOT EXISTS setting(" \
                      "id INTEGER PRIMARY KEY," \
                      "insolation VARCHAR(30)," \
                      "inner_temp VARCHAR(30)," \
                      "cool_temp VARCHAR(30)," \
                      "hot_temp VARCHAR(30)," \
                      "dhw_temp VARCHAR(30)," \
                      "doublecoil VARcHAR(30))"


## PMS Inner Database - sqlLite
def lite_conn():
    try:
        conn = sqlite3.connect(db_name, check_same_thread=False)
        cur = conn.cursor()

        return cur, conn
    except Exception as ex:
        print('Lite Conn Error', ex)


def start_check_lite():
    cur, conn = lite_conn()

    # protocol check
    cur.execute(protocol_table_query)

    cur.execute(schedule_table_query)

    cur.execute(control_table_query)

    # history_table
    cur.execute(history_table_query)

    cur.execute(error_table_query)

    cur.execute(setting_table_query)

    conn.commit()

    print('Success Check SQLite')


def select_protocol():
    cur, conn = lite_conn()
    sql = 'select * from protocol'
    cur.execute(sql)
    protocol_rows = cur.fetchall()
    protocol_rows = protocol_rows[0]

    if protocol_rows[9] == 'Modbus-TCP ??????' or protocol_rows[9] == 'Socket ??????':
        comd.var.bipvt_ip = protocol_rows[1]
        comd.var.bipvt_port = protocol_rows[2]
    else:
        comd.var.bipvt_serial_port = protocol_rows[5]
        comd.var.bipvt_brate = protocol_rows[6]
        comd.var.bipvt_parity = protocol_rows[7]
        comd.var.bipvt_stopbit = protocol_rows[8]

    if protocol_rows[10] == 'Modbus-TCP ??????' or protocol_rows[10] == 'Socket ??????':
        comd.var.heatpump_ip = protocol_rows[3]
        comd.var.heatpump_port = protocol_rows[4]
    else:
        comd.var.heatpump_serial_port = protocol_rows[11]
        comd.var.heatpump_brate = protocol_rows[12]
        comd.var.heatpump_parity = protocol_rows[13]
        comd.var.heatpump_stopbit = protocol_rows[14]

    if protocol_rows[21] == 'Modbus-TCP ??????' or protocol_rows[21] == 'Socket ??????':
        comd.var.fcu_ip = protocol_rows[15]
        comd.var.fcu_port = protocol_rows[16]
    else:
        comd.var.fcu_serial_port = protocol_rows[17]
        comd.var.fcu_brate = protocol_rows[18]
        comd.var.fcu_parity = protocol_rows[19]
        comd.var.fcu_stopbit = protocol_rows[20]


def setting_protocol():
    cur, conn = lite_conn()
    sql = 'select * from protocol'
    cur.execute(sql)
    protocol_rows = cur.fetchall()
    protocol_rows = protocol_rows[0]

    # ?????? ?????? ?????? ??????
    bipvt_type = protocol_rows[9]
    heatpump_type = protocol_rows[10]
    fcu_type = protocol_rows[21]

    # ??????????????? ?????? ?????? ?????? ??????
    ui.setting_Activity.setting_Activity.bipvt_combo.set(bipvt_type)
    ui.setting_Activity.setting_Activity.heatpump_combo.set(heatpump_type)
    # BIPVT IP ????????? ??????
    if bipvt_type == 'Socket ??????' or bipvt_type == 'Modbus-TCP ??????':
        ui.setting_Activity.setting_Activity.bipvt_serial_frame.pack_forget()
        ui.setting_Activity.setting_Activity.bipvt_tcp_frame.pack()

        bipvt_ip = protocol_rows[1].split('.')
        ui.setting_Activity.setting_Activity.bipvt_entry1.insert('end', bipvt_ip[0])
        ui.setting_Activity.setting_Activity.bipvt_entry2.insert('end', bipvt_ip[1])
        ui.setting_Activity.setting_Activity.bipvt_entry3.insert('end', bipvt_ip[2])
        ui.setting_Activity.setting_Activity.bipvt_entry4.insert('end', bipvt_ip[3])
        ui.setting_Activity.setting_Activity.bipvt_entry5.insert('end', protocol_rows[2])

        comd.var.bipvt_ip = protocol_rows[1]
        comd.var.bipvt_port = protocol_rows[2]
    else:   # BIPVT Serial ????????? ??????
        ui.setting_Activity.setting_Activity.bipvt_tcp_frame.pack_forget()
        ui.setting_Activity.setting_Activity.bipvt_serial_frame.pack()

        ui.setting_Activity.setting_Activity.bipvt_serial_entry1.insert('end', protocol_rows[5])
        ui.setting_Activity.setting_Activity.bipvt_serial_entry2.insert('end', protocol_rows[6])
        ui.setting_Activity.setting_Activity.bipvt_serial_entry3.insert('end', protocol_rows[7])
        ui.setting_Activity.setting_Activity.bipvt_serial_entry4.insert('end', protocol_rows[8])

        comd.var.bipvt_serial_port = protocol_rows[5]
        comd.var.bipvt_brate = protocol_rows[6]
        comd.var.bipvt_parity = protocol_rows[7]
        comd.var.bipvt_stopbit = protocol_rows[8]

    # ???????????? IP ????????? ??????
    if heatpump_type == 'Socket ??????' or heatpump_type == 'Modbus-TCP ??????':
        ui.setting_Activity.setting_Activity.heatpump_serial_frame.pack_forget()
        ui.setting_Activity.setting_Activity.heatpump_tcp_frame.pack()

        heatpump_ip = protocol_rows[3].split('.')
        ui.setting_Activity.setting_Activity.heatpump_entry1.insert('end', heatpump_ip[0])
        ui.setting_Activity.setting_Activity.heatpump_entry2.insert('end', heatpump_ip[1])
        ui.setting_Activity.setting_Activity.heatpump_entry3.insert('end', heatpump_ip[2])
        ui.setting_Activity.setting_Activity.heatpump_entry4.insert('end', heatpump_ip[3])
        ui.setting_Activity.setting_Activity.heatpump_entry5.insert('end', protocol_rows[4])

        comd.var.heatpump_ip = protocol_rows[3]
        comd.var.heatpump_port = protocol_rows[4]
    else:
        # ???????????? Serial ????????? ??????
        ui.setting_Activity.setting_Activity.heatpump_tcp_frame.pack_forget()
        ui.setting_Activity.setting_Activity.heatpump_serial_frame.pack()

        ui.setting_Activity.setting_Activity.heatpump_serial_entry1.insert('end', protocol_rows[11])
        ui.setting_Activity.setting_Activity.heatpump_serial_entry2.insert('end', protocol_rows[12])
        ui.setting_Activity.setting_Activity.heatpump_serial_entry3.insert('end', protocol_rows[13])
        ui.setting_Activity.setting_Activity.heatpump_serial_entry4.insert('end', protocol_rows[14])

        comd.var.heatpump_serial_port = protocol_rows[11]
        comd.var.heatpump_brate = protocol_rows[12]
        comd.var.heatpump_parity = protocol_rows[13]
        comd.var.heatpump_stopbit = protocol_rows[14]

    # FCU IP ????????? ??????
    # if fcu_type == 'Socket ??????' or fcu_type == 'Modbus-TCP ??????':
    #     ui.setting_Activity.setting_Activity.fcu_serial_frame.pack_forget()
    #     ui.setting_Activity.setting_Activity.fcu_tcp_frame.pack()
    #
    #     fcu_ip = protocol_rows[3].split('.')
    #     ui.setting_Activity.setting_Activity.fcu_entry1.insert('end', fcu_ip[0])
    #     ui.setting_Activity.setting_Activity.fcu_entry2.insert('end', fcu_ip[1])
    #     ui.setting_Activity.setting_Activity.fcu_entry3.insert('end', fcu_ip[2])
    #     ui.setting_Activity.setting_Activity.fcu_entry4.insert('end', fcu_ip[3])
    #     ui.setting_Activity.setting_Activity.fcu_entry5.insert('end', protocol_rows[2])
    #
    #     comd.var.fcu_ip = protocol_rows[3]
    #     comd.var.fcu_port = protocol_rows[4]
    # else:
    #     # FCU Serial ????????? ??????
    #     ui.setting_Activity.setting_Activity.fcu_tcp_frame.pack_forget()
    #     ui.setting_Activity.setting_Activity.fcu_serial_frame.pack()
    #
    #     ui.setting_Activity.setting_Activity.fcu_serial_entry1.insert('end', protocol_rows[17])
    #     ui.setting_Activity.setting_Activity.fcu_serial_entry2.insert('end', protocol_rows[18])
    #     ui.setting_Activity.setting_Activity.fcu_serial_entry3.insert('end', protocol_rows[19])
    #     ui.setting_Activity.setting_Activity.fcu_serial_entry4.insert('end', protocol_rows[20])
    #
    #     comd.var.fcu_serial_port = protocol_rows[11]
    #     comd.var.fcu_brate = protocol_rows[12]
    #     comd.var.fcu_parity = protocol_rows[13]
    #     comd.var.fcu_stopbit = protocol_rows[14]

# ???????????? ????????? ???????????? ?????????
def protocol_update(facility, types, data):
    cur, conn = lite_conn()
    print('UPDATE : ', facility, types, data)

    if facility == 'bipvt':
        sql = 'update protocol set bipvt_ip =?, bipvt_port =?, bipvt_type=? where id=1'
        cur.execute(sql, (data[0], data[1], types))

        ui.setting_Activity.setting_Activity.bipvt_entry1.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry2.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry3.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry4.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry5.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_serial_entry1.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_serial_entry2.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_serial_entry3.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_serial_entry4.delete(0, 'end')

        if types == 'Socket ??????' or types == 'Modbus-TCP ??????':
            ip_split = data[0].split('.')
            ui.setting_Activity.setting_Activity.bipvt_entry1.insert('end', ip_split[0])
            ui.setting_Activity.setting_Activity.bipvt_entry2.insert('end', ip_split[1])
            ui.setting_Activity.setting_Activity.bipvt_entry3.insert('end', ip_split[2])
            ui.setting_Activity.setting_Activity.bipvt_entry4.insert('end', ip_split[3])
            ui.setting_Activity.setting_Activity.bipvt_entry5.insert('end', data[1])
            comd.var.bipvt_ip = data[0]
            comd.var.bipvt_port = data[1]
            comd.var.bipvt_serial_port = ''
            comd.var.bipvt_brate = ''
            comd.var.bipvt_parity = ''
            comd.var.bipvt_stopbit = ''
        else:
            sql = 'update protocol set bipvt_serial_port=?, bipvt_brate=?, bipvt_parity=?, bipvt_stopbit=?, bipvt_type=? where id=1'
            cur.execute(sql, (data[0], data[1], data[2], data[3], types))

            ui.setting_Activity.setting_Activity.bipvt_serial_entry1.insert('end', data[0])
            ui.setting_Activity.setting_Activity.bipvt_serial_entry2.insert('end', data[1])
            ui.setting_Activity.setting_Activity.bipvt_serial_entry3.insert('end', data[2])
            ui.setting_Activity.setting_Activity.bipvt_serial_entry4.insert('end', data[3])
            comd.var.bipvt_ip = ''
            comd.var.bipvt_port = ''
            comd.var.bipvt_serial_port = data[0]
            comd.var.bipvt_brate = data[1]
            comd.var.bipvt_parity = data[2]
            comd.var.bipvt_stopbit = data[3]

    elif facility == 'heatpump':
        sql = 'update protocol set heatpump_ip =?, heatpump_port =?, heatpump_type=? where id=1'
        cur.execute(sql, (data[0], data[1], types))

        ui.setting_Activity.setting_Activity.heatpump_entry1.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry2.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry3.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry4.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry5.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_serial_entry1.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_serial_entry2.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_serial_entry3.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_serial_entry4.delete(0, 'end')

        if types == 'Socket ??????' or types == 'Modbus-TCP ??????':
            ip_split = data[0].split('.')
            ui.setting_Activity.setting_Activity.heatpump_entry1.insert('end', ip_split[0])
            ui.setting_Activity.setting_Activity.heatpump_entry2.insert('end', ip_split[1])
            ui.setting_Activity.setting_Activity.heatpump_entry3.insert('end', ip_split[2])
            ui.setting_Activity.setting_Activity.heatpump_entry4.insert('end', ip_split[3])
            ui.setting_Activity.setting_Activity.heatpump_entry5.insert('end', data[1])
            comd.var.heatpump_ip = data[0]
            comd.var.heatpump_port = data[1]
            comd.var.heatpump_serial_port = ''
            comd.var.heatpump_brate = ''
            comd.var.heatpump_parity = ''
            comd.var.heatpump_stopbit = ''
        else:
            sql = 'update protocol set heatpump_serial_port=?, heatpump_brate=?, heatpump_parity=?, heatpump_stopbit=?, heatpump_type=? where id=1'
            cur.execute(sql, (data[0], data[1], data[2], data[3], types))

            ui.setting_Activity.setting_Activity.heatpump_serial_entry1.insert('end', data[0])
            ui.setting_Activity.setting_Activity.heatpump_serial_entry2.insert('end', data[1])
            ui.setting_Activity.setting_Activity.heatpump_serial_entry3.insert('end', data[2])
            ui.setting_Activity.setting_Activity.heatpump_serial_entry4.insert('end', data[3])
            comd.var.heatpump_ip = ''
            comd.var.heatpump_port = ''
            comd.var.heatpump_serial_port = data[0]
            comd.var.heatpump_brate = data[1]
            comd.var.heatpump_parity = data[2]
            comd.var.heatpump_stopbit = data[3]

    conn.commit()
    hosting = 'Hosting Change >> %s\t|\t%s|\t%s ' % (facility, types, data)
    print(hosting)


def schedule_select():
    cur, conn = lite_conn()
    sql = 'select * from schedules'
    cur.execute(sql)
    rows = cur.fetchall()
    rows = rows[0]

    comd.var.start_hour = rows[1]
    comd.var.start_min = rows[2]
    comd.var.end_hour = rows[3]
    comd.var.end_min = rows[4]


def setting_schedule():
    cur, conn = lite_conn()
    sql = 'select * from schedules'
    cur.execute(sql)
    rows = cur.fetchall()

    start_hour = []
    start_min = []
    end_hour = []
    end_min = []
    checking = []

    for row in rows:
        start_hour.append(row[1])
        start_min.append(row[2])
        end_hour.append(row[3])
        end_min.append(row[4])
        checking.append(row[5])

    ui.control_Activity.control_Activity.schedule_start_hour_entry_1.insert('end', start_hour[0])
    ui.control_Activity.control_Activity.schedule_start_min_entry_1.insert('end', start_min[0])
    ui.control_Activity.control_Activity.schedule_end_hour_entry_1.insert('end', end_hour[0])
    ui.control_Activity.control_Activity.schedule_end_min_entry_1.insert('end', end_min[0])
    comd.var.schedule_start[0] = '%s:%s' % (start_hour[0], end_min[0])
    comd.var.schedule_end[0] = '%s:%s' % (end_hour[0], end_min[0])
    comd.var.schedule_checking[0] = checking[0]

    ui.control_Activity.control_Activity.schedule_start_hour_entry_2.insert('end', start_hour[1])
    ui.control_Activity.control_Activity.schedule_start_min_entry_2.insert('end', start_min[1])
    ui.control_Activity.control_Activity.schedule_end_hour_entry_2.insert('end', end_hour[1])
    ui.control_Activity.control_Activity.schedule_end_min_entry_2.insert('end', end_min[1])
    comd.var.schedule_start[1] = '%s:%s' % (start_hour[1], end_min[1])
    comd.var.schedule_end[1] = '%s:%s' % (end_hour[1], end_min[1])
    comd.var.schedule_checking[1] = checking[1]

    ui.control_Activity.control_Activity.schedule_start_hour_entry_3.insert('end', start_hour[2])
    ui.control_Activity.control_Activity.schedule_start_min_entry_3.insert('end', start_min[2])
    ui.control_Activity.control_Activity.schedule_end_hour_entry_3.insert('end', end_hour[2])
    ui.control_Activity.control_Activity.schedule_end_min_entry_3.insert('end', end_min[2])
    comd.var.schedule_start[2] = '%s:%s' % (start_hour[2], end_min[2])
    comd.var.schedule_end[2] = '%s:%s' % (end_hour[2], end_min[2])
    comd.var.schedule_checking[2] = checking[2]

    ui.control_Activity.control_Activity.schedule_start_hour_entry_4.insert('end', start_hour[3])
    ui.control_Activity.control_Activity.schedule_start_min_entry_4.insert('end', start_min[3])
    ui.control_Activity.control_Activity.schedule_end_hour_entry_4.insert('end', end_hour[3])
    ui.control_Activity.control_Activity.schedule_end_min_entry_4.insert('end', end_min[3])
    comd.var.schedule_start[3] = '%s:%s' % (start_hour[3], end_min[3])
    comd.var.schedule_end[3] = '%s:%s' % (end_hour[3], end_min[3])
    comd.var.schedule_checking[3] = checking[3]


def schedule_update(idx, check, entry1, entry2, entry3, entry4):
    cur, conn = lite_conn()

    sql = 'update schedules set start_hour = ?, start_min = ?, end_hour = ?, end_min = ?, checking = ? where id = ?'
    cur.execute(sql, (entry1, entry2, entry3, entry4, check, idx))
    conn.commit()

    print('Update : ', idx, check, entry1, entry2, entry3, entry4)

    if idx == '1':
        ui.control_Activity.control_Activity.schedule_start_hour_entry_1.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_min_entry_1.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_hour_entry_1.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_min_entry_1.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_hour_entry_1.insert('end', entry1)
        ui.control_Activity.control_Activity.schedule_start_min_entry_1.insert('end', entry2)
        ui.control_Activity.control_Activity.schedule_end_hour_entry_1.insert('end', entry3)
        ui.control_Activity.control_Activity.schedule_end_min_entry_1.insert('end', entry4)
        comd.var.schedule_start[0] = '%s:%s' % (entry1, entry2)
        comd.var.schedule_end[0] = '%s:%s' % (entry3, entry4)
        comd.var.schedule_checking[0] = check
    elif idx == '2':
        ui.control_Activity.control_Activity.schedule_start_hour_entry_2.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_min_entry_2.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_hour_entry_2.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_min_entry_2.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_hour_entry_2.insert('end', entry1)
        ui.control_Activity.control_Activity.schedule_start_min_entry_2.insert('end', entry2)
        ui.control_Activity.control_Activity.schedule_end_hour_entry_2.insert('end', entry3)
        ui.control_Activity.control_Activity.schedule_end_min_entry_2.insert('end', entry4)
        comd.var.schedule_start[1] = '%s:%s' %(entry1, entry2)
        comd.var.schedule_end[1] = '%s:%s' %(entry3, entry4)
        comd.var.schedule_checking[1] = check
    elif idx == '3':
        ui.control_Activity.control_Activity.schedule_start_hour_entry_3.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_min_entry_3.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_hour_entry_3.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_min_entry_3.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_hour_entry_3.insert('end', entry1)
        ui.control_Activity.control_Activity.schedule_start_min_entry_3.insert('end', entry2)
        ui.control_Activity.control_Activity.schedule_end_hour_entry_3.insert('end', entry3)
        ui.control_Activity.control_Activity.schedule_end_min_entry_3.insert('end', entry4)
        comd.var.schedule_start[2] = '%s:%s' % (entry1, entry2)
        comd.var.schedule_end[2] = '%s:%s' % (entry3, entry4)
        comd.var.schedule_checking[2] = check
    elif idx == '4':
        ui.control_Activity.control_Activity.schedule_start_hour_entry_4.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_min_entry_4.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_hour_entry_4.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_end_min_entry_4.delete(0, 'end')
        ui.control_Activity.control_Activity.schedule_start_hour_entry_4.insert('end', entry1)
        ui.control_Activity.control_Activity.schedule_start_min_entry_4.insert('end', entry2)
        ui.control_Activity.control_Activity.schedule_end_hour_entry_4.insert('end', entry3)
        ui.control_Activity.control_Activity.schedule_end_min_entry_4.insert('end', entry4)
        comd.var.schedule_start[3] = '%s:%s' % (entry1, entry2)
        comd.var.schedule_end[3] = '%s:%s' % (entry3, entry4)
        comd.var.schedule_checking[3] = check


def automode_select():
    cur, conn = lite_conn()
    sql = 'select * from controls'
    cur.execute(sql)
    rows = cur.fetchall()
    rows = rows[0]

    if rows[1] == 'auto':
        comd.var.auto_mode = True
        comd.var.reserve_mode = False
        comd.var.manual_mode = False
        comd.var.stop_mode = False
    elif rows[1] == 'reserve':
        comd.var.auto_mode = False
        comd.var.reserve_mode = True
        comd.var.manual_mode = False
        comd.var.stop_mode = False
    elif rows[1] == 'manual':
        comd.var.auto_mode = False
        comd.var.reserve_mode = False
        comd.var.manual_mode = True
        comd.var.stop_mode = False
    elif rows[1] == 'stop':
        comd.var.auto_mode = False
        comd.var.reserve_mode = False
        comd.var.manual_mode = False
        comd.var.stop_mode = True


def select_system():
    cur, conn = lite_conn()
    sql = 'select * from setting'
    cur.execute(sql)
    system_rows = cur.fetchall()
    system_rows = system_rows[0]

    comd.var.pv_volume = system_rows[1]
    comd.var.load_volume = system_rows[2]
    comd.var.insolation_volume = system_rows[3]
    comd.var.damper_volume = system_rows[4]
    comd.var.summer_volume = system_rows[8]
    comd.var.winter_volume = system_rows[9]
    # comd.var.cool_volume = system_rows[5]
    # comd.var.heat_volume = system_rows[6]
    # comd.var.dhw_volume = system_rows[7]


def setting_system():
    cur, conn = lite_conn()
    sql = 'select * from setting'
    cur.execute(sql)
    system_rows = cur.fetchall()
    system_rows = system_rows[0]

    ui.setting_Activity.setting_Activity.pvt_value.insert('end', system_rows[1])
    ui.setting_Activity.setting_Activity.load_value.insert('end', system_rows[2])
    ui.setting_Activity.setting_Activity.insolation_value.insert('end', system_rows[3])
    ui.setting_Activity.setting_Activity.damper_value.insert('end', system_rows[4])
    # ui.setting_Activity.setting_Activity.cooling_value.insert('end', system_rows[5])
    # ui.setting_Activity.setting_Activity.heating_value.insert('end', system_rows[6])
    # ui.setting_Activity.setting_Activity.dhw_value.insert('end', system_rows[7])
    ui.setting_Activity.setting_Activity.summer_heatpump_value.insert('end', system_rows[8])
    ui.setting_Activity.setting_Activity.winter_heatpump_value.insert('end', system_rows[9])

    comd.var.pv_volume = system_rows[1]
    comd.var.load_volume = system_rows[2]
    comd.var.insolation_volume = system_rows[3]
    comd.var.damper_volume = system_rows[4]
    comd.var.summer_volume = system_rows[8]
    comd.var.winter_volume = system_rows[9]
    # comd.var.cool_volume = system_rows[5]
    # comd.var.heat_volume = system_rows[6]
    # comd.var.dhw_volume = system_rows[7]


def system_update(volume, value):
    cur, conn = lite_conn()

    print('Update System Setting')
    sql = ''
    if volume == 'pvt':
        sql = 'Update setting SET pv_volume=? where id=1'
        ui.setting_Activity.setting_Activity.pvt_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.pvt_value.insert('end', value)
        comd.var.pv_volume = value
    elif volume == 'insolation':
        sql = 'Update setting SET insolation_volume=? where id=1'
        ui.setting_Activity.setting_Activity.insolation_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.insolation_value.insert('end', value)
        comd.var.insolation_volume = value
    elif volume == 'damper':
        sql = 'Update setting SET damper_volume=? where id=1'
        ui.setting_Activity.setting_Activity.damper_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.damper_value.insert('end', value)
        comd.var.damper_volume = value
    elif volume == 'load':
        sql = 'Update setting SET load_volume=? where id=1'
        ui.setting_Activity.setting_Activity.load_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.load_value.insert('end', value)
        comd.var.load_volume = value
    elif volume == 'cooling':
        sql = 'Update setting SET cool_volume=? where id=1'
        ui.setting_Activity.setting_Activity.cooling_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.cooling_value.insert('end', value)
        comd.var.cool_volume = value
    elif volume == 'heating':
        sql = 'Update setting SET heat_volume=? where id=1'
        ui.setting_Activity.setting_Activity.heating_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heating_value.insert('end', value)
        comd.var.heat_volume = value
    elif volume == 'dhw':
        sql = 'Update setting SET dhw_volume=? where id=1'
        ui.setting_Activity.setting_Activity.dhw_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.dhw_value.insert('end', value)
        comd.var.dhw_volume = value
    elif volume == 'summer':
        sql = 'Update setting SET summer_volume=? where id=1'
        ui.setting_Activity.setting_Activity.summer_heatpump_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.summer_heatpump_value.insert('end', value)
        comd.var.summer_volume = value
    elif volume == 'winter':
        sql = 'Update setting SET winter_volume=? where id=1'
        ui.setting_Activity.setting_Activity.winter_heatpump_value.delete(0, 'end')
        ui.setting_Activity.setting_Activity.winter_heatpump_value.insert('end', value)
        comd.var.winter_volume = value

    cur.execute(sql, (value,))
    conn.commit()


def automode_update(val):
    cur, conn = lite_conn()
    sql = "update controls set automode = ? where id = 1"
    cur.execute(sql, (val,))
    conn.commit()


def run_all():
    try:
        cur, conn = lite_conn()
        sql = 'select item, value, d_time from history order by d_time desc'

        cur.execute(sql)
        error_list = cur.fetchall()

        return error_list
    except Exception as ex:
        print('Lite history_all Error >> ', ex)


def run_count():
    try:
        cur, conn = lite_conn()
        sql = 'select count(*) from history'

        cur.execute(sql)
        history_count = cur.fetchone()

        print('count : ', history_count[0])

        return str(history_count[0])
    except Exception as ex:
        print('Lite history_count Error >> ', ex)


def run_insert(item_val, value_val, d_time_val):
    try:
        cur, conn = lite_conn()
        sql = 'insert into history(item, value, d_time) values(?,?,?)'
        cur.execute(sql, [item_val, value_val, d_time_val])

        conn.commit()
    except Exception as ex:
        print('Lite run_insert Error >> ', ex)


def error_all():
    try:
        cur, conn = lite_conn()
        sql = 'select item, value, d_time from error order by d_time desc'

        cur.execute(sql)
        error_list = cur.fetchall()

        return error_list
    except Exception as ex:
        print('Lite error_all Error >> ', ex)


def error_count():
    try:
        cur, conn = lite_conn()
        sql = 'select count(*) from error'

        cur.execute(sql)
        error_count = cur.fetchone()

        print('count : ', error_count[0])

        return str(error_count[0])
    except Exception as ex:
        print('Lite error_count Error >> ', ex)


def error_insert(item_val, value_val, d_time_val):
    try:
        cur, conn = lite_conn()
        sql = 'insert into error(item, value, d_time) values(?,?,?)'
        cur.execute(sql, [item_val, value_val, d_time_val])

        conn.commit()
    except Exception as ex:
        print('Lite error_insert Error >> ', ex)