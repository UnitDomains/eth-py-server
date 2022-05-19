import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_subdomain_info(network_id,
                          label,
                          sub_node_label,
                          sub_domain,
                          owner):
    """

    :return:
    """
    delete_subdomain_info(network_id,
                          label,
                          sub_node_label)

    reverse = 0

    sql = """
        INSERT INTO subdomain_info(
            pk_id,
            network_id,
            label,
            sub_node_label,
            sub_domain,
            owner) 
        VALUES (%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, label, sub_node_label, sub_domain, owner)

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


def delete_subdomain_info(network_id,
                          node,
                          label):
    sql = """
        DELETE FROM subdomain_info 
        WHERE network_id=%s AND node=%s AND label=%s
        """
    param = (network_id, node, label)

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
