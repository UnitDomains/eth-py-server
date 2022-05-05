"""
数据库
"""
import pymysql

conn = pymysql.connect(host="localhost",
                       user="root",
                       passwd="biticai_404",
                       db="unit_domains",
                       charset='utf8')
cur = conn.cursor()


def close_database():
    cur.close()
    conn.close()
