from database.database import conn, cur
from database.utils import get_uuid


def insert_ens_registry_event_new_owner(block_number,
                                        tx_hash,
                                        log_index,
                                        network_id,
                                        node,
                                        label,
                                        owner,
                                        timestamp):
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
        print(e)
        conn.rollback()


def insert_ens_registry_event_transfer(block_number,
                                       tx_hash,
                                       log_index,
                                       network_id,
                                       node,
                                       owner,
                                       timestamp):
    sql = """
    INSERT INTO ens_registry_event_transfer(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        owner,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, owner, timestamp)

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


def insert_ens_registry_event_approval_for_all(block_number,
                                               tx_hash,
                                               log_index,
                                               network_id,
                                               owner,
                                               operator,
                                               approved,
                                               timestamp):
    sql = """
    INSERT INTO ens_registry_event_approval_for_all(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        owner,
        operator,
        approvedr,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, owner, operator, approved, timestamp)

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


def insert_ens_registry_event_new_resolver(block_number,
                                           tx_hash,
                                           log_index,
                                           network_id,
                                           node,
                                           resolver,
                                           timestamp):
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

    except Exception as e:
        print(e)
        conn.rollback()


def insert_ens_registry_event_new_ttl(block_number,
                                      tx_hash,
                                      log_index,
                                      network_id,
                                      node,
                                      ttl,
                                      timestamp):
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
        print(e)
        conn.rollback()
