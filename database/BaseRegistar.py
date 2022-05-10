import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_base_registrar_event_name_registered( network_id,id, owner, expires, timestamp):
    """

    :return:
    """
    delete_base_registrar_event_name_registered(id)
    sql = """
        INSERT INTO base_registrar_event_name_registered(pk_id,network_id,id,owner,expires,timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id,id, owner, expires, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def update_base_registrar_event_name_renewed(network_id,id, expires, timestamp):
    """

    :return:
    """

    """
    delete_base_registrar_event_name_renewed(id);
    """
    sql = "UPDATE base_registrar_event_name_registered SET expires =%s WHERE network_id=%s AND  id=%s"
    param = (expires, network_id,id)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_base_registrar_event_transfer(network_id,
        from_addr, to_addr, tokenId, timestamp):
    """
    处理Transfer事件
    1:把旧的记录删除掉
    2.只保留最新的
    :return:
    """
    delete_base_registrar_event_transfer(tokenId)

    sql = """
        INSERT INTO base_registrar_event_transfer(pk_id,network_id,from_addr,to_addr,tokenId,timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(),network_id, from_addr, to_addr, tokenId, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_base_registrar_event_name_registered(network_id,id):
    """
    处理Transfer事件
    删除tokenid记录
    :return:
    """

    sql = "DELETE FROM base_registrar_event_name_registered WHERE network_id=%s AND id=%s"
    param = (network_id,id)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_base_registrar_event_name_renewed(network_id,id):
    """
    处理Transfer事件
    删除tokenid记录
    :return:
    """

    sql = "DELETE FROM base_registrar_event_name_renewed WHERE network_id=%s AND id=%s"
    param = (network_id,id)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_base_registrar_event_transfer(network_id,tokenId):
    """
    处理Transfer事件
    删除tokenid记录
    :return:
    """


    sql = "DELETE FROM base_registrar_event_transfer WHERE network_id=%s AND tokenId=%s"
    param = (network_id,tokenId)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def is_exist_phrase(word):
    """
    """

    sql = 'select count(*) from t_word where word= "%s"' % word

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql)

        if cur.rowcount > 0:
            row = cur.fetchone()

            if row[0] == 1:
                return True

        return False

    except pymysql.ProgrammingError as e:
        return False
