import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_ens_registry_event_new_owner(network_id,node, label, owner, timestamp):
    """
    处理NewOwner事件
    1.删除旧记录
    2.存入新纪录
    :return:
    """

    delete_ens_registry_event_new_owner(label)

    sql = """
        INSERT INTO ens_registry_event_new_owner(pk_id,network_id,node,label,owner,timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(),network_id, node, label, owner, timestamp)

    try:
        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)


        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_owner(network_id,label):
    """

    :return:
    """

    sql = "DELETE FROM ens_registry_event_new_owner WHERE network_id=%s AND label=%s"
    param = (network_id,label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)


        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_ens_registry_event_transfer(network_id,node, owner, timestamp):
    """

    :return:
    """

    delete_ens_registry_event_transfer(node)

    sql = "INSERT INTO ens_registry_event_transfer(pk_id,network_id,node,owner,timestamp) VALUES (%s,%s,%s,%s,%s)"
    param = (get_uuid(), network_id,node, owner, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_ens_registry_event_transfer(network_id,node):
    """
    处理Transfer事件
    删除tokenid记录
    :return:
    """

    sql = "DELETE FROM ens_registry_event_transfer WHERE network_id=%s AND node=%s"
    param = (network_id,node)

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
