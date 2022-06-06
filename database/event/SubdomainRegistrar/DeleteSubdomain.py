from database.database import conn, cur
from database.event.SubdomainRegistrar.model.DeleteSubdomainEventData import DeleteSubdomainEventData
from database.info.SubdomainInfo import delete_subdomain_info
from database.utils import get_uuid

subdomain_registrar_event_delete_subdomain_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_subdomain_registrar_event_delete_subdomain(block_number,
                                                      tx_hash,
                                                      log_index,
                                                      network_id,
                                                      node,
                                                      label,
                                                      timestamp):
    """
     event DeleteSubdomain(bytes32 indexed node, bytes32 indexed label);
    :return:
    """
    delete_subdomain_registrar_event_delete_subdomain(network_id,
                                                      block_number,
                                                      tx_hash,
                                                      log_index)
    sql = """
            INSERT INTO subdomain_registrar_event_delete_subdomain(
                pk_id,
                block_number,
                tx_hash,
                log_index,
                network_id,
                node,
                label,
                timestamp) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (
        get_uuid(), block_number, tx_hash, log_index, network_id, node, label, timestamp)
    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            delete_subdomain_info(network_id,
                                  node,
                                  label)

    except Exception as e:
        print("insert_subdomain_registrar_event_delete_subdomain")
        print(e)
        conn.rollback()


def delete_subdomain_registrar_event_delete_subdomain(network_id,
                                                      block_number,
                                                      tx_hash,
                                                      log_index):
    sql = """
        DELETE FROM subdomain_registrar_event_delete_subdomain 
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
        print("delete_subdomain_registrar_event_delete_subdomain")
        print(e)
        conn.rollback()


def delete_subdomain_registrar_event_delete_subdomain_after_block(network_id,
                                                                  block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM subdomain_registrar_event_delete_subdomain 
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
        print("delete_subdomain_registrar_event_delete_subdomain_after_block")
        print(e)
        conn.rollback()


def get_subdomain_registrar_event_delete_subdomain(network_id,
                                                   node
                                                   ):
    """
    """

    sql = """
            SELECT pk_id, node, addr, network_id, block_number, tx_hash, log_index, timestamp, op_time 
            FROM subdomain_registrar_event_delete_subdomain 
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

            pk_id = row[0]
            node = row[1]
            addr = row[2]
            network_id = row[3]
            block_number = row[4]
            tx_hash = row[5]
            log_index = row[6]
            timestamp = row[7]
            op_time = row[8]

            return DeleteSubdomainEventData(pk_id,
                                            node,
                                            addr,
                                            network_id,
                                            block_number,
                                            tx_hash,
                                            log_index,
                                            timestamp,
                                            op_time)

        return None


    except Exception as e:

        print("get_public_resolver_event_addr_changed")

        print(e)
        return None


def get_all_subdomain_registrar_event_delete_subdomain(network_id,
                                                       node
                                                       ):
    """
    """

    sql = """
            SELECT pk_id, node, addr, network_id, block_number, tx_hash, log_index, timestamp, op_time
            FROM subdomain_registrar_event_delete_subdomain 
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
                pk_id = row[0]
                node = row[1]
                addr = row[2]
                network_id = row[3]
                block_number = row[4]
                tx_hash = row[5]
                log_index = row[6]
                timestamp = row[7]
                op_time = row[8]

                res = DeleteSubdomainEventData(pk_id,
                                               node,
                                               addr,
                                               network_id,
                                               block_number,
                                               tx_hash,
                                               log_index,
                                               timestamp,
                                               op_time)
                result.append(res)

            return result

        return None


    except Exception as e:

        print("get_all_public_resolver_event_addr_changed")

        print(e)
        return None
