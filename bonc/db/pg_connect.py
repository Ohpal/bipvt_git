import psycopg2 as pg
import comd.var
from datetime import date, timedelta

def db_conn():
    try:
        # conn_string = "host='192.168.0.200' dbname='smgrid_db' user='postgres' password='bonc123!' port='5432'"
        conn_string = "host='118.222.208.70' dbname='bipvtdb' user='postgres' password='bonc90412' port='6245' connect_timeout=3"

        conn = pg.connect(conn_string)
        cur = conn.cursor()

        return cur, conn
    except Exception as ex:
        print('DB Conn Error', ex)


def bipvt_insert(value):
    try:
        cur, conn = db_conn()
        sql = 'insert into bipvt_tb values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        cur.execute(sql, value)
        conn.commit()

        cur.close()
        conn.close()

    except Exception as ex:
        print('data_insert Error >>', ex)


def heatpump_insert(value):
    try:
        cur, conn = db_conn()
        sql = 'insert into heatpump_tb values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        cur.execute(sql, value)
        conn.commit()

        cur.close()
        conn.close()
    except Exception as ex:
        print('heatpump_insert Error >> ', ex)


def weather_insert(value):
    try:
        cur, conn = db_conn()
        sql = 'insert into weather_tb values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        cur.execute(sql, value)
        conn.commit()

        cur.close()
        conn.close()

    except Exception as ex:
        print('weather_insert Error >>', ex)


def weather_select():
    try:
        cur, conn = db_conn()
        sql = 'select weather, temp, humi, icon from weather_tb order by d_time desc'
        cur.execute(sql)
        row = cur.fetchone()

        cur.close()
        conn.close()

        return list(row)
    except Exception as ex:
        print('weather_select Error >>', ex)


def total_power_select():
    try:
        today, yesterday = today_yesterday()

        cur, conn = db_conn()
        sql = "select d_time, pv_power_total, storage_power_total, heatpump_power_total, buffer_power_total, heatline_power_total, dhw_power_total from (select *, row_number() over (PARTITION BY (to_char(d_time, 'YYYY-MM-dd hh24')) order by d_time desc) as time_rank from bipvt_tb where d_time between %s and %s) as one_time where time_rank = 1 order by d_time desc limit 1"
        cur.execute(sql, (yesterday, today))
        row = cur.fetchone()

        cur.close()
        conn.close()

        return list(row)
    except Exception as ex:
        print('total_power Error', ex)


def today_yesterday():
    today = date.today().strftime('%Y-%m-%d')
    yesterday = (date.today() - timedelta(1)).strftime('%Y-%m-%d')

    return today, yesterday


def pre_data_select():
    try:
        cur, conn = db_conn()
        sql = 'select pv_predict from solar_predict order by d_time desc limit 1'

        cur.execute(sql)
        row = cur.fetchone()[0]

        cur.close()
        conn.close()

        return row
    except Exception as ex:
        print('pre_data_select Error ', ex)


# def