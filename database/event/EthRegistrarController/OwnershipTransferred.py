from database.database import conn, cur
from database.utils import get_uuid

eth_registrar_controller_event_ownership_transferred_table_columns = [
    'pk_id', 'node', 'owner', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_eth_registrar_controller_event_ownership_transferred(block_number,
                                                                tx_hash,
                                                                log_index,
                                                                network_id,
                                                                previousOwner,
                                                                newOwner,
                                                                timestamp):
    """

    :return:
    """
    delete_eth_registrar_controller_event_ownership_transferred(network_id,
                                                                block_number,
                                                                tx_hash,
                                                                log_index)
    sql = """
        INSERT INTO eth_registrar_controller_event_ownership_transferred(
                pk_id,
                block_number,
                tx_hash,
                log_index,
                network_id,
                previous_owner,
                new_owner,
                timestamp
                ) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, previousOwner, newOwner, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("insert_eth_registrar_controller_event_ownership_transferred")
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_ownership_transferred(network_id,
                                                                block_number,
                                                                tx_hash,
                                                                log_index):
    sql = """
        DELETE FROM eth_registrar_controller_event_ownership_transferred 
        WHERE network_id=%s AND block_number=%s AND tx_hash=%s AND log_index=%s
        """
    param = (network_id, block_number, tx_hash, log_index)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("delete_eth_registrar_controller_event_ownership_transferred")
        print(e)
        conn.rollback()


def delete_eth_registrar_controller_event_ownership_transferred_after_block(network_id,
                                                                            block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM eth_registrar_controller_event_ownership_transferred 
        WHERE network_id=%s AND block_number>=%s 
        """
    param = (network_id, block_number)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("delete_eth_registrar_controller_event_ownership_transferred_after_block")
        print(e)
        conn.rollback()
