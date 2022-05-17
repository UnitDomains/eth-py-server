"""
数据库
"""
import configparser

import pymysql

config_db = configparser.ConfigParser()
config_db.read("databaseConfig.ini",
               encoding='utf-8')

config_db_items = dict(config_db.items("database"))

config_db_host = config_db_items["host"]
config_db_user = config_db_items["user"]
config_db_passwd = config_db_items["passwd"]
config_db_db = config_db_items["db"]

conn = pymysql.connect(host=config_db_host,
                       user=config_db_user,
                       passwd=config_db_passwd,
                       db=config_db_db,
                       charset='utf8')
cur = conn.cursor()


def close_database():
    cur.close()
    conn.close()
