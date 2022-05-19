import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_domain_info(network_id,
                       label,
                       name,
                       base_node_index,
                       owner,
                       expires):
    """

    :return:
    """
    delete_domain_info(network_id,
                       label)



    sql = """
        INSERT INTO domain_info(
            pk_id,
            network_id,
            label,
            name,
            base_node_index,
            owner,
            expires
            ) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, label, name, base_node_index, owner, expires)

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


def update_domain_info_expires(network_id,
                               label,
                               expires):
    """

    :return:
    """

    sql = "UPDATE domain_info SET expires =%s WHERE network_id=%s AND  label=%s"
    param = (expires, network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def update_domain_info_transfer(network_id,
                                label,
                                from_addr,
                                to_addr):
    """
    :return:
    """

    sql = "UPDATE domain_info SET owner =%s WHERE network_id=%s AND  label=%s AND owner=%s"
    param = (to_addr, network_id, label, from_addr)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()





def delete_domain_info(network_id,
                       label):
    sql = """
        DELETE FROM domain_info 
        WHERE network_id=%s AND label=%s
        """
    param = (network_id, label)

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
