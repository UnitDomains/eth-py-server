import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_base_registrar_event_name_registered(id, owner, expires, timestamp):
    """
    插入
    :return:
    """
    delete_base_registrar_event_name_registered(id)
    sql = "INSERT INTO base_registrar_event_name_registered(pk_id,id,owner,expires,timestamp) values (%s,%s,%s,%s,%s)"
    param = (get_uuid(), id, owner, expires, timestamp)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def update_base_registrar_event_name_renewed(id, expires, timestamp):
    """
    更新域名
    :return:
    """

    """
    delete_base_registrar_event_name_renewed(id);
    """
    sql = "UPDATE base_registrar_event_name_registered SET expires =%s WHERE id=%s"
    param = (expires, id)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_base_registrar_event_transfer(
        from_addr, to_addr, tokenId, timestamp):
    """
    处理Transfer事件
    1:把旧的记录删除掉
    2.只保留最新的
    :return:
    """
    delete_base_registrar_event_transfer(tokenId)

    sql = "INSERT INTO base_registrar_event_transfer(pk_id,from_addr,to_addr,tokenId,timestamp) values (%s,%s,%s,%s,%s)"
    param = (get_uuid(), from_addr, to_addr, tokenId, timestamp)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_base_registrar_event_name_registered(id):
    """
    处理Transfer事件
    删除tokenid记录
    :return:
    """

    sql = "DELETE FROM base_registrar_event_name_registered WHERE id=%s"
    param = (id)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_base_registrar_event_name_renewed(id):
    """
    处理Transfer事件
    删除tokenid记录
    :return:
    """

    sql = "DELETE FROM base_registrar_event_name_renewed WHERE id=%s"
    param = (id)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_base_registrar_event_transfer(tokenId):
    """
    处理Transfer事件
    删除tokenid记录
    :return:
    """


    sql = "DELETE FROM base_registrar_event_transfer WHERE tokenId=%s"
    param = (tokenId)

    try:

        # 检查连接是否断开，如果断开就进行重连
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

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        cur.execute(sql)

        if cur.rowcount > 0:
            row = cur.fetchone()

            if row[0] == 1:
                return True

        return False

    except pymysql.ProgrammingError as e:
        return False
