import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_public_resolver_event_addr_changed(block_number,
                                              tx_hash,
                                              log_index,
                                              network_id,
                                              node,
                                              addr,
                                              timestamp):
    """
    event AddrChanged(bytes32 indexed node, address addr);
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_addr_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        addr,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, addr, timestamp)

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


def insert_public_resolver_event_name_changed(block_number,
                                              tx_hash,
                                              log_index,
                                              network_id,
                                              node,
                                              name,
                                              timestamp):
    """
    event NameChanged(bytes32 indexed node, string name);
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_name_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        name,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, name, timestamp)

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
