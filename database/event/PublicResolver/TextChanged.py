from database.database import conn, cur
from database.info.DomainInfo import update_domain_info_record
from database.info.SubdomainInfo import update_subdomain_info_record
from database.utils import convertBytes2String, get_uuid

public_resolver_event_text_changed_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_public_resolver_event_text_changed(block_number,
                                              tx_hash,
                                              log_index,
                                              network_id,
                                              node,
                                              indexed_key,
                                              key,
                                              value,
                                              timestamp):
    """
    :return:
    """
    indexed_key = convertBytes2String(indexed_key)

    print(indexed_key)
    print(key)
    print(value)

    delete_public_resolver_event_text_changed(network_id,
                                              block_number,
                                              tx_hash,
                                              log_index)

    sql = """
    INSERT INTO public_resolver_event_text_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        indexed_key,
        text_key,
        timestamp
        ) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, indexed_key, key, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_domain_info_record(network_id,
                                      node,
                                      key,
                                      value)

            # Update subdomain info if the event called by subdomain
            update_subdomain_info_record(network_id,
                                         node,
                                         key,
                                         value)

    except Exception as e:
        print("insert_public_resolver_event_text_changed")
        print(e)
        conn.rollback()


def delete_public_resolver_event_text_changed(network_id,
                                              block_number,
                                              tx_hash,
                                              log_index):
    sql = """
        DELETE FROM public_resolver_event_text_changed 
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
        print("delete_public_resolver_event_text_changed")
        print(e)
        conn.rollback()


def delete_public_resolver_event_text_changed_after_block(network_id,
                                                          block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM public_resolver_event_text_changed 
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
        print("delete_public_resolver_event_text_changed_after_block")
        print(e)
        conn.rollback()
