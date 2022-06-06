from database.database import conn, cur
from database.utils import get_uuid

ens_registry_event_new_owner_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_ens_registry_event_new_owner(block_number,
                                        tx_hash,
                                        log_index,
                                        network_id,
                                        node,
                                        label,
                                        owner,
                                        timestamp):
    delete_ens_registry_event_new_owner(network_id,
                                        block_number,
                                        tx_hash,
                                        log_index)
    sql = """
        INSERT INTO ens_registry_event_new_owner(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            node,
            label,
            owner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, label, owner, timestamp)

    try:
        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()



    except Exception as e:
        print("insert_ens_registry_event_new_owner")
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_owner(network_id,
                                        block_number,
                                        tx_hash,
                                        log_index):
    sql = """
        DELETE FROM ens_registry_event_new_owner 
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
        print("delete_ens_registry_event_new_owner")
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_owner_after_block(network_id,
                                                    block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM ens_registry_event_new_owner 
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
        print("delete_ens_registry_event_new_owner_after_block")
        print(e)
        conn.rollback()


def get_ens_registry_event_new_owner(network_id,
                                     node,
                                     label,
                                     ):
    """
    """

    sql = """
            SELECT * 
            FROM ens_registry_event_new_owner 
            WHERE network_id=%s AND node=%s AND label=%s
            ORDER BY block_number DESC ,log_index DESC 
            LIMIT 0,1
            """
    param = (network_id, node, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            return row

        return None


    except Exception as e:

        print("get_ens_registry_event_new_owner")

        print(e)
        return None
