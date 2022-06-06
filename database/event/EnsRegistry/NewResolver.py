from database.database import conn, cur
from database.event.EnsRegistry.model.NewResolverEventData import NewResolverEventData
from database.utils import get_uuid

ens_registry_event_new_resolver_table_columns = [
    'pk_id', 'node', 'resolver', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_ens_registry_event_new_resolver(block_number,
                                           tx_hash,
                                           log_index,
                                           network_id,
                                           node,
                                           resolver,
                                           timestamp):
    delete_ens_registry_event_new_resolver(network_id,
                                           block_number,
                                           tx_hash,
                                           log_index)
    sql = """
    INSERT INTO ens_registry_event_new_resolver(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        resolver,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, resolver, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            from database.info.DomainInfo import update_domain_info_resolver
            update_domain_info_resolver(network_id,
                                        node,
                                        resolver)

    except Exception as e:
        print("insert_ens_registry_event_new_resolver")
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_resolver(network_id,
                                           block_number,
                                           tx_hash,
                                           log_index):
    sql = """
        DELETE FROM ens_registry_event_new_resolver 
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
        print("delete_ens_registry_event_new_resolver")
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_resolver_after_block(network_id,
                                                       block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM ens_registry_event_new_resolver 
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
        print("delete_ens_registry_event_new_resolver_after_block")
        print(e)
        conn.rollback()


def convertRow2NewResolverEventData(row):
    '''
   pk_id, node, resolver, network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    node = row[1]
    resolver = row[2]
    network_id = row[3]
    block_number = row[4]
    tx_hash = row[5]
    log_index = row[6]
    timestamp = row[7]
    op_time = row[8]

    return NewResolverEventData(pk_id,
                                node,
                                resolver,
                                network_id,
                                block_number,
                                tx_hash,
                                log_index,
                                timestamp,
                                op_time)


def get_ens_registry_event_new_resolver(network_id,
                                        node
                                        ):
    """
    """

    sql = """
            SELECT pk_id, node, resolver, network_id, block_number, tx_hash, log_index, timestamp, op_time 
            FROM ens_registry_event_new_resolver 
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

            return convertRow2NewResolverEventData(row)

        return None


    except Exception as e:

        print("get_ens_registry_event_new_owner")

        print(e)
        return None


def get_all_ens_registry_event_new_resolver(network_id,
                                            node
                                            ):
    """
    """

    sql = """
            SELECT pk_id, node, resolver, network_id, block_number, tx_hash, log_index, timestamp, op_time 
            FROM ens_registry_event_new_resolver 
            WHERE network_id=%s AND node=%s
            ORDER BY block_number DESC ,log_index DESC 
            """
    param = (network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            rows = cur.fetchall()
            result = []
            for row in rows:
                result.append(convertRow2NewResolverEventData(row))

            return result

        return None


    except Exception as e:

        print("get_all_ens_registry_event_new_resolver")

        print(e)
        return None
