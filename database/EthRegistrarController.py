import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_eth_registrar_controller_event_name_registered(
        name, label, owner, cost, expires, baseNodeIndex, timestamp):
    """

    :return:
    """

    delete_eth_registrar_controller_event_name_registered(label)

    sql = "INSERT INTO eth_registrar_controller_event_name_registered(pk_id,name,label,owner,cost,expires,baseNodeIndex,timestamp) values (%s,%s,%s,%s,%s,%s,%s,%s)"
    param = (
        get_uuid(),
        name,
        label,
        owner,
        cost,
        expires,
        baseNodeIndex,
        timestamp)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_eth_registrar_controller_event_ownership_transferred(
        previousOwner, newOwner, timestamp):
    """

    :return:
    """

    sql = "INSERT INTO eth_registrar_controller_event_ownership_transferred(pk_id,previousOwner,newOwner,timestamp) values (%s,%s,%s,%s)"
    param = (get_uuid(), previousOwner, newOwner, timestamp)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_eth_registrar_controller_event_name_renewed(
        name, label, cost, expires, baseNodeIndex, timestamp):
    delete_eth_registrar_controller_event_name_renewed(label)

    sql = "INSERT INTO eth_registrar_controller_event_name_renewed(pk_id,name,label,cost,expires,baseNodeIndex,timestamp) values (%s,%s,%s,%s,%s,%s,%s)"
    param = (get_uuid(), name, label, cost, expires, baseNodeIndex, timestamp)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_name_registered(label):
    """

    :return:
    """

    sql = "DELETE FROM eth_registrar_controller_event_name_registered WHERE label=%s"
    param = (label)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_ownership_transferred(node):
    """

    :return:
    """

    sql = "DELETE FROM ens_registry_event_transfer WHERE node=%s"
    param = (node)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_name_renewed(label):
    """

    :return:
    """

    sql = "DELETE FROM eth_registrar_controller_event_name_renewed WHERE label=%s"
    param = (label)

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
