from database.database import conn, cur
from database.utils import get_uuid


def insert_reverse_info(network_id,
                        addr,
                        node):
    """

    :return:
    """
    delete_reverse_info(network_id,
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
        print("insert_reverse_info")
        print(e)
        conn.rollback()


def delete_reverse_info(network_id,
                        node):
    sql = """
        DELETE FROM reverse_info 
        WHERE network_id=%s AND node=%s
        """
    param = (network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("delete_reverse_info")
        print(e)
        conn.rollback()


def insert_reverse_info_name(network_id,
                             node,
                             name):
    """

    :return:
    """
    delete_reverse_info(network_id,
                        node)

    sql = """
        INSERT INTO reverse_info(
            pk_id,
            network_id,
            node,
            name          
            ) 
        VALUES (%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, node, name)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("insert_reverse_info")
        print(e)
        conn.rollback()


def update_reverse_info_name(network_id,
                             node,
                             name):
    sql = "UPDATE reverse_info SET name =%s WHERE network_id=%s and node=%s"
    param = (name, network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("update_reverse_info_name")
        print(e)
        conn.rollback()


def update_reverse_info_addr(network_id,
                             node,
                             addr):
    sql = "UPDATE reverse_info SET addr =%s WHERE network_id=%s and node=%s"
    param = (addr, network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("update_reverse_info_addr")
        print(e)
        conn.rollback()


def update_reverse_info(network_id,
                        node,
                        name):
    """

    :return:
    """
    if name == '0x0000000000000000000000000000000000000000':
        delete_reverse_info(network_id,
                            node)
    elif is_exist_reverse_info(network_id,
                               node):
        update_reverse_info_name(network_id,
                                 node,
                                 name)
    else:
        insert_reverse_info_name(network_id,
                                 node,
                                 name)


def is_exist_reverse_info(network_id,
                          node):
    """
    """
 
    sql = """
        SELECT count(*) 
        FROM reverse_info
        WHERE network_id=%s and node=%s
    """
    param = (network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            if row[0] == 1:
                return True

        return False


    except Exception as e:

        print("is_exist_reverse_info")

        print(e)
        return False
