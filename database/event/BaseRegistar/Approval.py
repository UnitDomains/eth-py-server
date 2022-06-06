from database.database import conn, cur
from database.event.BaseRegistar.model.ApprovalEventData import ApprovalEventData
from database.utils import get_uuid

base_registrar_event_approval_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_base_registrar_event_approval(block_number,
                                         tx_hash,
                                         log_index,
                                         network_id,
                                         owner,
                                         approved,
                                         token_id,
                                         timestamp):
    delete_base_registrar_event_approval(network_id,
                                         block_number,
                                         tx_hash,
                                         log_index)

    sql = """
        INSERT INTO base_registrar_event_approval(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            owner,
            approved,
            token_id,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, owner, approved, token_id, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("insert_base_registrar_event_approval")
        print(e)
        conn.rollback()


def delete_base_registrar_event_approval(network_id,
                                         block_number,
                                         tx_hash,
                                         log_index):
    sql = """
        DELETE FROM base_registrar_event_approval 
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
        print("delete_base_registrar_event_approval")
        print(e)
        conn.rollback()


def delete_base_registrar_event_approval_after_block(network_id,
                                                     block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM base_registrar_event_approval 
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
        print("delete_base_registrar_event_approval_after_block")
        print(e)
        conn.rollback()


def convertRow2ApprovalEventData(row):
    '''
    pk_id, owner, approved,token_id,network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    owner = row[1]
    approved = row[2]
    token_id = row[3]
    network_id = row[4]
    block_number = row[5]
    tx_hash = row[6]
    log_index = row[7]
    timestamp = row[8]
    op_time = row[9]

    return ApprovalEventData(pk_id,
                             owner,
                             approved,
                             token_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)


def get_base_registrar_event_approval(network_id,
                                      node
                                      ):
    """
    """

    sql = """
            SELECT pk_id, owner, approved,token_id,network_id, block_number, tx_hash, log_index, timestamp, op_time  
            FROM base_registrar_event_approval 
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

            return convertRow2ApprovalEventData(row)

        return None


    except Exception as e:

        print("delete_base_registrar_event_approval")

        print(e)
        return None
