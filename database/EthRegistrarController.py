from database.DomainInfo import insert_domain_info, update_domain_info_expires
from database.database import conn, cur
from database.utils import get_uuid


def insert_eth_registrar_controller_event_name_registered(block_number,
                                                          tx_hash,
                                                          log_index,
                                                          network_id,
                                                          name,
                                                          label,
                                                          owner,
                                                          cost,
                                                          expires,
                                                          baseNodeIndex,
                                                          timestamp):
    """

    :return:
    """

    sql = """
        INSERT INTO eth_registrar_controller_event_name_registered(
            pk_id,
            block_number,tx_hash,log_index,
            network_id,
            name,
            label,
            owner,
            cost,
            expires,
            base_node_index,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (
        get_uuid(), block_number, tx_hash, log_index,
        network_id,
        name,
        label,
        owner,
        cost,
        expires,
        baseNodeIndex,
        timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            # insert_domain_info( network_id,label,name,base_node_index, owner, expires)
            insert_domain_info(network_id,
                               label,
                               name,
                               baseNodeIndex,
                               owner,
                               expires)

    except Exception as e:
        print(e)
        conn.rollback()


def insert_eth_registrar_controller_event_ownership_transferred(block_number,
                                                                tx_hash,
                                                                log_index,
                                                                network_id,
                                                                previousOwner,
                                                                newOwner,
                                                                timestamp):
    """

    :return:
    """

    sql = """
        INSERT INTO eth_registrar_controller_event_ownership_transferred(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            previousOwner,
            newOwner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, previousOwner, newOwner, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_eth_registrar_controller_event_name_renewed(block_number,
                                                       tx_hash,
                                                       log_index,
                                                       network_id,
                                                       name,
                                                       label,
                                                       cost,
                                                       expires,
                                                       baseNodeIndex,
                                                       timestamp):
    sql = """
        INSERT INTO eth_registrar_controller_event_name_renewed(        
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        name,
        label,
        cost,
        expires,
        base_node_index,
        timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (
    get_uuid(), block_number, tx_hash, log_index, network_id, name, label, cost, expires, baseNodeIndex, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_domain_info_expires(network_id,
                                       label,
                                       expires)

    except Exception as e:
        print(e)
        conn.rollback()
