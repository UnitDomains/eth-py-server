from database.database import conn, cur
from database.event.PublicResolver.model.AddrChangedEventData import AddrChangedEventData

from database.utils import get_uuid

public_resolver_event_addr_changed_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_public_resolver_event_addr_changed(block_number,
                                              tx_hash,
                                              log_index,
                                              network_id,
                                              node,
                                              addr,
                                              timestamp):
    """
    event AddrChanged(bytes32 indexed node, address addr);
    :return:
    """
    delete_public_resolver_event_addr_changed(network_id,
                                              block_number,
                                              tx_hash,
                                              log_index)

    sql = """
    INSERT INTO public_resolver_event_addr_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        addr,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, addr, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            from database.info.DomainInfo import update_domain_info_eth_address
            update_domain_info_eth_address(network_id,
                                           node,
                                           addr)

            # Update subdomain info if the event called by subdomain
            from database.info.SubdomainInfo import update_subdomain_info_eth_address
            update_subdomain_info_eth_address(network_id,
                                              node,
                                              addr)

    except Exception as e:
        print("insert_public_resolver_event_addr_changed")
        print(e)
        conn.rollback()


def delete_public_resolver_event_addr_changed(network_id,
                                              block_number,
                                              tx_hash,
                                              log_index):
    sql = """
        DELETE FROM public_resolver_event_addr_changed 
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
        print("delete_public_resolver_event_addr_changed")
        print(e)
        conn.rollback()


def delete_public_resolver_event_addr_changed_after_block(network_id,
                                                          block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM public_resolver_event_addr_changed 
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
        print("delete_public_resolver_event_addr_changed_after_block")
        print(e)
        conn.rollback()


def get_public_resolver_event_addr_changed(network_id,
                                           node
                                           ):
    """
    """

    sql = """
            SELECT pk_id, node, addr, network_id, block_number, tx_hash, log_index, timestamp, op_time 
            FROM public_resolver_event_addr_changed 
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

            return AddrChangedEventData(pk_id,
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


def get_all_public_resolver_event_addr_changed(network_id,
                                               node
                                               ):
    """
    """

    sql = """
            SELECT pk_id, node, addr, network_id, block_number, tx_hash, log_index, timestamp, op_time
            FROM public_resolver_event_addr_changed 
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

                res = AddrChangedEventData(pk_id,
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
