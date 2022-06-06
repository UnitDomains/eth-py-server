from database.database import conn, cur
from database.event.SubdomainRegistrar.model.NewSubdomainRegistrationEventData import NewSubdomainRegistrationEventData
from database.info.SubdomainInfo import insert_subdomain_info
from database.utils import get_uuid

subdomain_registrar_event_new_subdomain_registration_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_subdomain_registrar_event_new_subdomain_registration(block_number,
                                                                tx_hash,
                                                                log_index,
                                                                network_id,
                                                                label,
                                                                sub_domain,
                                                                owner,
                                                                timestamp):
    """
    event NewSubdomainRegistration(
                bytes32 indexed label,
                string subdomain,
                address indexed owner
             );
    :return:
    """

    delete_subdomain_registrar_event_new_subdomain_registration(network_id,
                                                                block_number,
                                                                tx_hash,
                                                                log_index)

    sql = """
        INSERT INTO subdomain_registrar_event_new_subdomain_registration(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            label,
            sub_domain,
            owner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (
        get_uuid(), block_number, tx_hash, log_index, network_id, label, sub_domain, owner, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            insert_subdomain_info(network_id,
                                  label,
                                  sub_domain,
                                  owner)

    except Exception as e:
        print("insert_subdomain_registrar_event_new_subdomain_registration")
        print(e)
        conn.rollback()


def delete_subdomain_registrar_event_new_subdomain_registration(network_id,
                                                                block_number,
                                                                tx_hash,
                                                                log_index):
    sql = """
        DELETE FROM subdomain_registrar_event_new_subdomain_registration 
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
        print("delete_subdomain_registrar_event_new_subdomain_registration")
        print(e)
        conn.rollback()


def delete_subdomain_registrar_event_new_subdomain_registration_after_block(network_id,
                                                                            block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM subdomain_registrar_event_new_subdomain_registration 
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
        print("delete_subdomain_registrar_event_new_subdomain_registration_after_block")
        print(e)
        conn.rollback()


def convertRow2NewSubdomainRegistrationEventData(row):
    pk_id = row[0]
    label = row[1]
    sub_domain = row[2]
    owner = row[3]
    network_id = row[4]
    block_number = row[5]
    tx_hash = row[6]
    log_index = row[7]
    timestamp = row[8]
    op_time = row[9]

    return NewSubdomainRegistrationEventData(pk_id,
                                             label,
                                             sub_domain,
                                             owner,
                                             network_id,
                                             block_number,
                                             tx_hash,
                                             log_index,
                                             timestamp,
                                             op_time)


def get_subdomain_registrar_event_new_subdomain_registration(network_id,
                                                             node
                                                             ):
    """
    """

    sql = """
            SELECT pk_id, label, sub_domain,owner, network_id, block_number, tx_hash, log_index, timestamp, op_time 
            FROM subdomain_registrar_event_new_subdomain_registration 
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

            return convertRow2NewSubdomainRegistrationEventData(row)

        return None


    except Exception as e:

        print("get_public_resolver_event_addr_changed")

        print(e)
        return None


def get_all_subdomain_registrar_event_new_subdomain_registration(network_id,
                                                                 node
                                                                 ):
    """
    """

    sql = """
            SELECT pk_id, label, sub_domain,owner, network_id, block_number, tx_hash, log_index, timestamp, op_time
            FROM subdomain_registrar_event_new_subdomain_registration 
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
                result.append(convertRow2NewSubdomainRegistrationEventData(row))

            return result

        return None


    except Exception as e:

        print("get_all_public_resolver_event_addr_changed")

        print(e)
        return None
