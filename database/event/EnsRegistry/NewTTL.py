from database.database import conn, cur
from database.event.EnsRegistry.model.NewTTLEventData import NewTTLEventData
from database.utils import get_uuid

ens_registry_event_new_ttl_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_ens_registry_event_new_ttl(block_number,
                                      tx_hash,
                                      log_index,
                                      network_id,
                                      node,
                                      ttl,
                                      timestamp):
    delete_ens_registry_event_new_ttl(network_id,
                                      block_number,
                                      tx_hash,
                                      log_index)

    sql = """
    INSERT INTO ens_registry_event_new_ttl(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        ttl,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, ttl, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("insert_ens_registry_event_new_ttl")
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_ttl(network_id,
                                      block_number,
                                      tx_hash,
                                      log_index):
    sql = """
        DELETE FROM ens_registry_event_new_ttl 
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
        print("delete_ens_registry_event_new_ttl")
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_ttl_after_block(network_id,
                                                  block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM ens_registry_event_new_ttl 
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
        print("delete_ens_registry_event_new_ttl_after_block")
        print(e)
        conn.rollback()


def convertRow2NewTTLEventData(row):
    '''
    pk_id, node, node_label,owner, network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    node = row[1]
    owner = row[2]
    network_id = row[3]
    block_number = row[4]
    tx_hash = row[5]
    log_index = row[6]
    timestamp = row[7]
    op_time = row[8]

    return NewTTLEventData(pk_id,
                           node,
                           owner,
                           network_id,
                           block_number,
                           tx_hash,
                           log_index,
                           timestamp,
                           op_time)


def get_ens_registry_event_transfer(network_id,
                                    node
                                    ):
    """
    """

    sql = """
            SELECT pk_id, node, ttl, network_id, block_number, tx_hash, log_index, timestamp, op_time  
            FROM ens_registry_event_new_ttl 
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

            return convertRow2NewTTLEventData(row)

        return None


    except Exception as e:

        print("get_ens_registry_event_transfer")

        print(e)
        return None
