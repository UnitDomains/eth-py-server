from database.database import conn, cur
from database.event.BaseRegistar.model.TransferEventData import TransferEventData
from database.utils import get_uuid

base_registrar_event_transfer_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_base_registrar_event_transfer(block_number,
                                         tx_hash,
                                         log_index,
                                         network_id,
                                         from_addr,
                                         to_addr,
                                         token_id,
                                         timestamp):
    """

    :param block_number:
    :param tx_hash:
    :param log_index:
    :param network_id:
    :param from_addr:
    :param to_addr:
    :param token_id:
    :param timestamp:
    :return:
    """

    delete_base_registrar_event_transfer(network_id,
                                         block_number,
                                         tx_hash,
                                         log_index)

    sql = """
        INSERT INTO base_registrar_event_transfer(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            from_addr,
            to_addr,
            token_id,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, from_addr, to_addr, token_id, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            from database.info.DomainInfo import update_domain_info_transfer
            update_domain_info_transfer(network_id,
                                        token_id,
                                        from_addr,
                                        to_addr)

    except Exception as e:
        print("insert_base_registrar_event_transfer")
        print(e)
        conn.rollback()


def delete_base_registrar_event_transfer(network_id,
                                         block_number,
                                         tx_hash,
                                         log_index):
    sql = """
        DELETE FROM base_registrar_event_transfer 
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
        print("delete_base_registrar_event_transfer")
        print(e)
        conn.rollback()


def delete_base_registrar_event_transfer_after_block(network_id,
                                                     block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM base_registrar_event_transfer 
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
        print("delete_base_registrar_event_transfer_after_block")
        print(e)
        conn.rollback()


def convertRow2TransferEventData(row):
    '''
    pk_id, from_addr, to_addr,token_id, network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    from_addr = row[1]
    to_addr = row[2]
    token_id = row[3]
    network_id = row[4]
    block_number = row[5]
    tx_hash = row[6]
    log_index = row[7]
    timestamp = row[8]
    op_time = row[9]

    return TransferEventData(pk_id,
                             from_addr,
                             to_addr,
                             token_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)


def get_base_registrar_event_transfer(network_id,
                                      token_id
                                      ):
    """
    """

    sql = """
            SELECT pk_id, from_addr, to_addr,token_id, network_id, block_number, tx_hash, log_index, timestamp, op_time  
            FROM base_registrar_event_transfer 
            WHERE network_id=%s AND token_id=%s
            ORDER BY block_number DESC ,log_index DESC 
            LIMIT 0,1
            """
    param = (network_id, token_id)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            return convertRow2TransferEventData(row)

        return None


    except Exception as e:

        print("get_base_registrar_event_transfer")

        print(e)
        return None
