import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_reverse_info(network_id,
                        addr,
                        node):
    """

    :return:
    """
    delete_reverse_info(network_id,
                        addr,
                        node)

    sql = """
        INSERT INTO reverse_info(
            pk_id,
            network_id,
            addr,
            node          
            ) 
        VALUES (%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, addr, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_reverse_info(network_id,
                        addr,
                        node):
    sql = """
        DELETE FROM reverse_info 
        WHERE network_id=%s AND addr=%s AND node=%s
        """
    param = (network_id, addr, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
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
