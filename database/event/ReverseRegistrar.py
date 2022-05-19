from database.database import conn, cur
from database.info.ReverseInfo import insert_reverse_info
from database.utils import get_uuid


def insert_reverse_registrar_event_reverse_claimed(block_number,
                                                   tx_hash,
                                                   log_index,
                                                   network_id,
                                                   node,
                                                   addr,
                                                   expires,
                                                   timestamp):
    """

    :return:
    """

    sql = """
        INSERT INTO reverse_registrar_event_reverse_claimed(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            node,
            addr,
            expires,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, addr, expires, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            insert_reverse_info(network_id,
                                node,
                                addr)

    except Exception as e:
        print(e)
        conn.rollback()


def insert_reverse_registrar_event_controller_changed(block_number,
                                                      tx_hash,
                                                      log_index,
                                                      network_id,
                                                      controller,
                                                      enabled,
                                                      timestamp):
    """

    :return:
    """

    sql = """
            INSERT INTO reverse_registrar_event_controller_changed(
                pk_id,
                block_number,
                tx_hash,
                log_index,
                network_id,
                controller,
                enabled,
                timestamp) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, controller, enabled, timestamp)

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


def insert_reverse_registrar_event_ownership_transferred(block_number,
                                                         tx_hash,
                                                         log_index,
                                                         network_id,
                                                         previous_owner,
                                                         new_owner,
                                                         timestamp):
    sql = """
        INSERT INTO reverse_registrar_event_ownership_transferred(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            previous_owner,
            new_owner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, previous_owner, new_owner, timestamp)

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
