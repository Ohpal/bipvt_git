import psycopg2 as pg
import comd.var

def db_conn():
    try:
        # conn_string = "host='192.168.0.200' dbname='smgrid_db' user='postgres' password='bonc123!' port='5432'"
        conn_string = "host='118.222.208.70' dbname='bipvtdb' user='postgres' password='bonc90412' port='6245' connect_timeout=3"

        conn = pg.connect(conn_string)
        cur = conn.cursor()

        return cur, conn
    except Exception as ex:
        print('DB Conn Error', ex)


def data_insert(value):
    try:
        cur, conn = db_conn()
        sql = 'insert into tems_tb values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        cur.execute(sql, value)
        conn.commit()

        cur.close()
        conn.close()

    except Exception as ex:
        print('data_insert Error >>', ex)


def weather_insert(value):
    try:
        cur, conn = db_conn()
        sql = 'insert into weather_tb values(%s,%s,%s,%s,%s,%s,%s,%s)'

        cur.execute(sql, value)
        conn.commit()

        cur.close()
        conn.close()

    except Exception as ex:
        print('weather_insert Error >>', ex)


def weather_select():
    try:
        cur, conn =  db_conn()
        sql = 'select weather, temp, humi from weather_tb order by d_time desc'
        cur.execute(sql)
        row = cur.fetchone()

        cur.close()
        conn.close()

        return list(row)
    except Exception as ex:
        print('weather_select Error >>', ex)