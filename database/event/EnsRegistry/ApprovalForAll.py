from database.database import conn, cur
from database.event.EnsRegistry.model.ApprovalForAllEventData import ApprovalForAllEventData
from database.utils import get_uuid

ens_registry_event_approval_for_all_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_ens_registry_event_approval_for_all(block_number,
                                               tx_hash,
                                               log_index,
                                               network_id,
                                               owner,
                                               operator,
                                               approved,
                                               timestamp):
    delete_ens_registry_event_approval_for_all(network_id,
                                               block_number,
                                               tx_hash,
                                               log_index)
    sql = """
    INSERT INTO ens_registry_event_approval_for_all(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        owner,
        operator,
        approved,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, owner, operator, approved, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("insert_ens_registry_event_approval_for_all")
        print(e)
        conn.rollback()


def delete_ens_registry_event_approval_for_all(network_id,
                                               block_number,
                                               tx_hash,
                                               log_index):
    sql = """
        DELETE FROM ens_registry_event_approval_for_all 
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
        print("delete_ens_registry_event_approval_for_all")
        print(e)
        conn.rollback()


def delete_ens_registry_event_approval_for_all_after_block(network_id,
                                                           block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM ens_registry_event_approval_for_all 
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
        print("delete_ens_registry_event_approval_for_all_after_block")
        print(e)
        conn.rollback()


def convertRow2ApprovalForAllEventData(row):
    '''
    pk_id, owner,operator,approved, network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    owner = row[1]
    operator = row[2]
    approved = row[3]
    network_id = row[4]
    block_number = row[5]
    tx_hash = row[6]
    log_index = row[7]
    timestamp = row[8]
    op_time = row[9]

    return ApprovalForAllEventData(pk_id,
                                   owner,
                                   operator,
                                   approved,
                                   network_id,
                                   block_number,
                                   tx_hash,
                                   log_index,
                                   timestamp,
                                   op_time)


def get_ens_registry_event_approval_for_all(network_id,
                                            node
                                            ):
    """
    """

    sql = """
            SELECT pk_id, owner,operator,approved, network_id, block_number, tx_hash, log_index, timestamp, op_time  
            FROM ens_registry_event_approval_for_all 
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

            return convertRow2ApprovalForAllEventData(row)

        return None


    except Exception as e:

        print("get_ens_registry_event_approval_for_all")

        print(e)
        return None
