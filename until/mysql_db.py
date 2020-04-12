# coding:utf8
import pymysql

conn = pymysql.connect('192.168.134.129', 'root', 'mkq666', 'sanguo')
cursor = conn.cursor()
try:
    select_all = ('select * from sanguozhi;')
    cursor.execute(select_all)

    data = cursor.fetchmany(2)
    print(data)
    data1 = cursor.fetchall()
    print(data1)
except:
    cursor.close()
    raise
finally:
    conn.close()
