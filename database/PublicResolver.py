import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_public_resolver_event_addr_changed(network_id,node, addr, timestamp):
    """
    event AddrChanged(bytes32 indexed node, address addr);
    :return:
    """

    delete_public_resolver_event_addr_changed(node)

    sql = """
    INSERT INTO public_resolver_event_addr_changed(pk_id,network_id,node,addr,timestamp) 
    VALUES (%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id,node, addr, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_public_resolver_event_name_changed(network_id,node, name, timestamp):
    """
    event NameChanged(bytes32 indexed node, string name);
    :return:
    """

    delete_public_resolver_event_name_changed(node)

    sql = """
    INSERT INTO public_resolver_event_name_changed(pk_id,network_id,node,name,timestamp) 
    VALUES (%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id,node, name, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_public_resolver_event_addr_changed(network_id,node):
    """

    :return:
    """

    sql = """
    DELETE FROM public_resolver_event_addr_changed 
    WHERE network_id=%s AND node=%s
    """
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


def delete_public_resolver_event_name_changed(network_id,node):
    """

    :return:
    """

    sql = """
    DELETE FROM public_resolver_event_name_changed 
    WHERE network_id=%s AND node=%s
    """
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
