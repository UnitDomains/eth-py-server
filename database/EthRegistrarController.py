import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_eth_registrar_controller_event_name_registered(network_id,
                                                          name, label, owner,
                                                          cost, expires, baseNodeIndex, timestamp):
    """

    :return:
    """

    delete_eth_registrar_controller_event_name_registered(label)

    sql = """
        INSERT INTO eth_registrar_controller_event_name_registered(
            pk_id,
            network_id,
            name,
            label,
            owner,
            cost,
            expires,
            baseNodeIndex,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (
        get_uuid(),
        network_id,
        name,
        label,
        owner,
        cost,
        expires,
        baseNodeIndex,
        timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_eth_registrar_controller_event_ownership_transferred(network_id,
                                                                previousOwner, newOwner, timestamp):
    """

    :return:
    """

    sql = """
        INSERT INTO eth_registrar_controller_event_ownership_transferred(
            pk_id,
            network_id,
            previousOwner,
            newOwner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, previousOwner, newOwner, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_eth_registrar_controller_event_name_renewed(network_id,
                                                       name, label, cost, expires, baseNodeIndex, timestamp):
    delete_eth_registrar_controller_event_name_renewed(label)

    sql = """
        INSERT INTO eth_registrar_controller_event_name_renewed(
        pk_id,
        network_id,
        name,
        label,
        cost,
        expires,
        baseNodeIndex,
        timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), network_id, name, label, cost, expires, baseNodeIndex, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_name_registered(network_id, label):
    """

    :return:
    """

    sql = """
        DELETE FROM eth_registrar_controller_event_name_registered 
        WHERE network_id=%s AND label=%s
        """
    param = (network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_ownership_transferred(network_id, node):
    """

    :return:
    """

    sql = "DELETE FROM ens_registry_event_transfer WHERE network_id=%s AND node=%s"
    param = (network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_name_renewed(network_id, label):
    """

    :return:
    """

    sql = "DELETE FROM eth_registrar_controller_event_name_renewed WHERE network_id=%s AND label=%s"
    param = (network_id, label)

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
