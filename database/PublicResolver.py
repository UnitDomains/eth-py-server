import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_public_resolver_event_addr_changed(node, addr, timestamp):
    """
    event AddrChanged(bytes32 indexed node, address addr);
    :return:
    """

    delete_public_resolver_event_addr_changed(node)

    sql = "INSERT INTO public_resolver_event_addr_changed(pk_id,node,addr,timestamp) values (%s,%s,%s,%s)"
    param = (get_uuid(), node, addr, timestamp)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_public_resolver_event_name_changed(node, name, timestamp):
    """
    event NameChanged(bytes32 indexed node, string name);
    :return:
    """

    delete_public_resolver_event_name_changed(node)

    sql = "INSERT INTO public_resolver_event_name_changed(pk_id,node,name,timestamp) values (%s,%s,%s,%s)"
    param = (get_uuid(), node, name, timestamp)

    try:

        # 检查连接是否断开，如果断开就进行重连
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_public_resolver_event_addr_changed(node):
    """

    :return:
    """

    sql = "DELETE FROM public_resolver_event_addr_changed WHERE node=%s"
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


def delete_public_resolver_event_name_changed(node):
    """

    :return:
    """

    sql = "DELETE FROM public_resolver_event_name_changed WHERE node=%s"
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
