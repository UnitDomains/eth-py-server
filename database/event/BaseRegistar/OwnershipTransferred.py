from database.database import conn, cur
from database.event.BaseRegistar.model.OwnershipTransferredEventData import OwnershipTransferredEventData
from database.utils import get_uuid

base_registrar_event_ownership_transferred_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_base_registrar_event_ownership_transferred(block_number,
                                                      tx_hash,
                                                      log_index,
                                                      network_id,
                                                      previous_owner,
                                                      new_owner,
                                                      timestamp):
    delete_base_registrar_event_ownership_transferred(network_id,
                                                      block_number,
                                                      tx_hash,
                                                      log_index)

    sql = """
        INSERT INTO base_registrar_event_ownership_transferred(
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
        print("insert_base_registrar_event_ownership_transferred")
        print(e)
        conn.rollback()


def delete_base_registrar_event_ownership_transferred(network_id,
                                                      block_number,
                                                      tx_hash,
                                                      log_index):
    sql = """
        DELETE FROM base_registrar_event_ownership_transferred 
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
        print("delete_base_registrar_event_ownership_transferred")
        print(e)
        conn.rollback()


def delete_base_registrar_event_ownership_transferred_after_block(network_id,
                                                                  block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM base_registrar_event_ownership_transferred 
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
        print("delete_base_registrar_event_ownership_transferred_after_block")
        print(e)
        conn.rollback()


def convertRow2OwnershipTransferredEventData(row):
    '''
    pk_id, previous_owner, new_owner, network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    previous_owner = row[1]
    new_owner = row[2]
    network_id = row[3]
    block_number = row[4]
    tx_hash = row[5]
    log_index = row[6]
    timestamp = row[7]
    op_time = row[8]

    return OwnershipTransferredEventData(pk_id,
                                         previous_owner,
                                         new_owner,
                                         network_id,
                                         block_number,
                                         tx_hash,
                                         log_index,
                                         timestamp,
                                         op_time)


def get_base_registrar_event_ownership_transferred(network_id,
                                                   node
                                                   ):
    """
    """

    sql = """
            SELECT pk_id, previous_owner, new_owner, network_id, block_number, tx_hash, log_index, timestamp, op_time  
            FROM base_registrar_event_ownership_transferred 
            WHERE network_id=%s AND node=%s
            ORDER BY block_number DESC ,log_index DESC 
            LIMIT 0,1
            """
    param = (network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            return convertRow2OwnershipTransferredEventData(row)

        return None


    except Exception as e:

        print("get_base_registrar_event_ownership_transferred")

        print(e)
        return None
