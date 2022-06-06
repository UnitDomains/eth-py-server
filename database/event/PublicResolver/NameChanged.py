from database.database import conn, cur
from database.info.ReverseInfo import update_reverse_info
from database.utils import get_uuid

public_resolver_event_name_changed_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


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
    delete_public_resolver_event_name_changed(network_id,
                                              block_number,
                                              tx_hash,
                                              log_index)
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

            update_reverse_info(network_id,
                                node,
                                name)

    except Exception as e:
        print("insert_public_resolver_event_name_changed")
        print(e)
        conn.rollback()


def delete_public_resolver_event_name_changed(network_id,
                                              block_number,
                                              tx_hash,
                                              log_index):
    sql = """
        DELETE FROM public_resolver_event_name_changed 
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
        print("delete_public_resolver_event_name_changed")
        print(e)
        conn.rollback()


def delete_public_resolver_event_name_changed_after_block(network_id,
                                                          block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM public_resolver_event_name_changed 
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
        print("delete_public_resolver_event_name_changed_after_block")
        print(e)
        conn.rollback()
