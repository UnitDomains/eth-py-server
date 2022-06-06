from database.database import conn, cur
from database.event.EnsRegistry.model.NewTLDOwnerEventData import NewTLDOwnerEventData
from database.info.DomainInfo import update_domain_info_controller
from database.utils import get_uuid

ens_registry_event_new_tld_owner_table_columns = [
    'pk_id', 'node', 'node_label', 'owner', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_ens_registry_event_new_tld_owner(block_number,
                                            tx_hash,
                                            log_index,
                                            network_id,
                                            node,
                                            nodelabel,
                                            owner,
                                            timestamp):
    delete_ens_registry_event_new_tld_owner(network_id,
                                            block_number,
                                            tx_hash,
                                            log_index)
    sql = """
        INSERT INTO ens_registry_event_new_tld_owner(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            node,
            node_label,
            owner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, nodelabel, owner, timestamp)

    try:
        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_domain_info_controller(network_id,
                                          nodelabel,
                                          owner)



    except Exception as e:
        print("insert_ens_registry_event_new_owner")
        print(e)
        conn.rollback()


def delete_ens_registry_event_new_tld_owner(network_id,
                                            block_number,
                                            tx_hash,
                                            log_index):
    sql = """
        DELETE FROM ens_registry_event_new_tld_owner 
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


def delete_ens_registry_event_new_tld_owner_after_block(network_id,
                                                        block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM ens_registry_event_new_tld_owner 
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
        print("delete_ens_registry_event_new_tld_owner_after_block")
        print(e)
        conn.rollback()


def convertRow2NewTLDOwnerEventData(row):
    '''
    pk_id, node, node_label,owner, network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    node = row[1]
    node_label = row[2]
    owner = row[3]
    network_id = row[4]
    block_number = row[5]
    tx_hash = row[6]
    log_index = row[7]
    timestamp = row[8]
    op_time = row[9]

    return NewTLDOwnerEventData(pk_id,
                                node,
                                node_label,
                                owner,
                                network_id,
                                block_number,
                                tx_hash,
                                log_index,
                                timestamp,
                                op_time)


def get_ens_registry_event_new_tld_owner(network_id,
                                         node
                                         ):
    """
    """

    sql = """
            SELECT pk_id, node, node_label,owner, network_id, block_number, tx_hash, log_index, timestamp, op_time 
            FROM ens_registry_event_new_tld_owner 
            WHERE network_id=%s AND node_label=%s
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

            return convertRow2NewTLDOwnerEventData(row)

        return None


    except Exception as e:

        print("get_ens_registry_event_new_tld_owner")

        print(e)
        return None


def get_all_ens_registry_event_new_tld_owner(network_id,
                                             node
                                             ):
    """
    """

    sql = """
            SELECT pk_id, node, node_label,owner, network_id, block_number, tx_hash, log_index, timestamp, op_time
            FROM ens_registry_event_new_tld_owner 
            WHERE network_id=%s AND node_label=%s
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
                result.append(convertRow2NewTLDOwnerEventData(row))

            return result

        return None


    except Exception as e:

        print("get_all_ens_registry_event_new_tld_owner")

        print(e)
        return None
