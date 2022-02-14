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
                       'bipvt_ip varchar(32),' \
                       'bipvt_port varchar(32),' \
                       'heatpump_ip varchar(32),' \
                       'heatpump_port varchar(32)' \
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

    comd.var.bipvt_ip = protocol_rows[1]
    comd.var.bipvt_port = protocol_rows[2]
    comd.var.heatpump_ip = protocol_rows[3]
    comd.var.heatpump_port = protocol_rows[4]


def setting_protocol():
    cur, conn = lite_conn()
    sql = 'select * from protocol'
    cur.execute(sql)
    protocol_rows = cur.fetchall()
    protocol_rows = protocol_rows[0]

    bipvt_ip = protocol_rows[1].split('.')
    heatpump_ip = protocol_rows[3].split('.')

    ui.setting_Activity.setting_Activity.bipvt_entry1.insert('end', bipvt_ip[0])
    ui.setting_Activity.setting_Activity.bipvt_entry2.insert('end', bipvt_ip[1])
    ui.setting_Activity.setting_Activity.bipvt_entry3.insert('end', bipvt_ip[2])
    ui.setting_Activity.setting_Activity.bipvt_entry4.insert('end', bipvt_ip[3])
    ui.setting_Activity.setting_Activity.bipvt_entry5.insert('end', protocol_rows[2])

    ui.setting_Activity.setting_Activity.heatpump_entry1.insert('end', heatpump_ip[0])
    ui.setting_Activity.setting_Activity.heatpump_entry2.insert('end', heatpump_ip[1])
    ui.setting_Activity.setting_Activity.heatpump_entry3.insert('end', heatpump_ip[2])
    ui.setting_Activity.setting_Activity.heatpump_entry4.insert('end', heatpump_ip[3])
    ui.setting_Activity.setting_Activity.heatpump_entry5.insert('end', protocol_rows[4])

    comd.var.bipvt_ip = protocol_rows[1]
    comd.var.bipvt_port = protocol_rows[2]
    comd.var.heatpump_ip = protocol_rows[3]
    comd.var.heatpump_port = protocol_rows[4]


def protocol_update(entry1, entry2, value1, value2):
    cur, conn = lite_conn()

    print('UPDATE : ', entry1, entry2, value1, value2)

    sql = 'update protocol set ' + entry1 + '= ?, ' + entry2 + '= ? where id = 1'
    cur.execute(sql, (value1, value2))
    conn.commit()

    item = entry1.split('_')[0]
    ip_split = value1.split('.')

    if item == 'bipvt':

        ui.setting_Activity.setting_Activity.bipvt_entry1.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry2.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry3.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry4.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry5.delete(0, 'end')
        ui.setting_Activity.setting_Activity.bipvt_entry1.insert('end', ip_split[0])
        ui.setting_Activity.setting_Activity.bipvt_entry2.insert('end', ip_split[1])
        ui.setting_Activity.setting_Activity.bipvt_entry3.insert('end', ip_split[2])
        ui.setting_Activity.setting_Activity.bipvt_entry4.insert('end', ip_split[3])
        ui.setting_Activity.setting_Activity.bipvt_entry5.insert('end', value2)
        comd.var.bipvt_ip = value1
        comd.var.bipvt_port = value2
    elif item == 'heatpump':
        ui.setting_Activity.setting_Activity.heatpump_entry1.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry2.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry3.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry4.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry5.delete(0, 'end')
        ui.setting_Activity.setting_Activity.heatpump_entry1.insert('end', ip_split[0])
        ui.setting_Activity.setting_Activity.heatpump_entry2.insert('end', ip_split[1])
        ui.setting_Activity.setting_Activity.heatpump_entry3.insert('end', ip_split[2])
        ui.setting_Activity.setting_Activity.heatpump_entry4.insert('end', ip_split[3])
        ui.setting_Activity.setting_Activity.heatpump_entry5.insert('end', value2)
        comd.var.heatpump_ip = value1
        comd.var.heatpump_port = value2

    hosting = 'Hosting Change >> %s : %s \t|\t %s : %s' % (entry1, value1, entry2, value2)
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
    rows = rows[0]

    ui.control_Activity.control_Activity.start_hour_entry.insert('end', rows[1])
    ui.control_Activity.control_Activity.start_min_entry.insert('end', rows[2])
    ui.control_Activity.control_Activity.end_hour_entry.insert('end', rows[3])
    ui.control_Activity.control_Activity.end_min_entry.insert('end', rows[4])

    comd.var.start_hour = rows[1]
    comd.var.start_min = rows[2]
    comd.var.end_hour = rows[3]
    comd.var.end_min = rows[4]


def schedule_update(entry1, entry2, entry3, entry4):
    cur, conn = lite_conn()

    print('UPDATE : ', entry1, entry2, entry3, entry4)

    sql = 'update schedules set start_hour = ?, start_min = ?, end_hour = ?, end_min = ? where id = 1'
    cur.execute(sql, (entry1, entry2, entry3, entry4))
    conn.commit()

    ui.control_Activity.control_Activity.start_hour_entry.delete(0, 'end')
    ui.control_Activity.control_Activity.start_min_entry.delete(0, 'end')
    ui.control_Activity.control_Activity.end_hour_entry.delete(0, 'end')
    ui.control_Activity.control_Activity.end_min_entry.delete(0, 'end')
    ui.control_Activity.control_Activity.start_hour_entry.insert('end', entry1)
    ui.control_Activity.control_Activity.start_min_entry.insert('end', entry2)
    ui.control_Activity.control_Activity.end_hour_entry.insert('end', entry3)
    ui.control_Activity.control_Activity.end_min_entry.insert('end', entry4)
    comd.var.start_hour = entry1
    comd.var.start_min = entry2
    comd.var.end_hour = entry3
    comd.var.end_min = entry4


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

    comd.var.insolation_value = system_rows[1]
    comd.var.inner_temp_value = system_rows[2]
    comd.var.cool_value = system_rows[3]
    comd.var.hot_value = system_rows[4]
    comd.var.dhw_value = system_rows[5]
    comd.var.doublecoil_value = system_rows[6]


def setting_system():
    cur, conn = lite_conn()
    sql = 'select * from setting'
    cur.execute(sql)
    system_rows = cur.fetchall()
    system_rows = system_rows[0]

    ui.setting_Activity.setting_Activity.insolation_value.insert('end', system_rows[1])
    ui.setting_Activity.setting_Activity.bipvt_inner_temp_value.insert('end', system_rows[2])
    ui.setting_Activity.setting_Activity.cool_value.insert('end', system_rows[3])
    ui.setting_Activity.setting_Activity.hot_value.insert('end', system_rows[4])
    ui.setting_Activity.setting_Activity.dhw_value.insert('end', system_rows[5])
    ui.setting_Activity.setting_Activity.doublecoil_value.insert('end', system_rows[6])

    comd.var.insolation_value = system_rows[1]
    comd.var.inner_temp_value = system_rows[2]
    comd.var.cool_value = system_rows[3]
    comd.var.hot_value = system_rows[4]
    comd.var.dhw_value = system_rows[5]
    comd.var.doublecoil_value = system_rows[6]


def system_update(insolation, bipvt_inner_temp, cool, hot, dhw, doublecoil):
    cur, conn = lite_conn()

    print('Update System Setting')

    sql = 'UPDATE setting SET insolation=?, inner_temp=?,cool_temp=?, hot_temp=?,dhw_temp=?,doublecoil=? where id=1'
    cur.execute(sql, (insolation, bipvt_inner_temp, cool, hot, dhw, doublecoil))
    conn.commit()

    ui.setting_Activity.setting_Activity.insolation_value.delete(0, "end")
    ui.setting_Activity.setting_Activity.bipvt_inner_temp_value.delete(0, "end")
    ui.setting_Activity.setting_Activity.cool_value.delete(0, "end")
    ui.setting_Activity.setting_Activity.hot_value.delete(0, "end")
    ui.setting_Activity.setting_Activity.dhw_value.delete(0, "end")
    ui.setting_Activity.setting_Activity.doublecoil_value.delete(0, "end")

    ui.setting_Activity.setting_Activity.insolation_value.insert('end', insolation)
    ui.setting_Activity.setting_Activity.bipvt_inner_temp_value.insert('end', bipvt_inner_temp)
    ui.setting_Activity.setting_Activity.cool_value.insert('end', cool)
    ui.setting_Activity.setting_Activity.hot_value.insert('end', hot)
    ui.setting_Activity.setting_Activity.dhw_value.insert('end', dhw)
    ui.setting_Activity.setting_Activity.doublecoil_value.insert('end', doublecoil)

    comd.var.insolation_value = insolation
    comd.var.inner_temp_value = bipvt_inner_temp
    comd.var.cool_value = cool
    comd.var.hot_value = hot
    comd.var.dhw_value = dhw
    comd.var.doublecoil_value = doublecoil


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