from database.database import conn, cur
from database.utils import convertBytes2String, get_uuid


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

    except Exception as e:
        print(e)
        conn.rollback()


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

    except Exception as e:
        print(e)
        conn.rollback()


def insert_public_resolver_event_abi_changed(block_number,
                                             tx_hash,
                                             log_index,
                                             network_id,
                                             node,
                                             content_type,
                                             timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_abi_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        content_type,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, content_type, timestamp)

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


def insert_public_resolver_event_address_changed(block_number,
                                                 tx_hash,
                                                 log_index,
                                                 network_id,
                                                 node,
                                                 new_address,
                                                 coin_type,
                                                 timestamp):
    """
    :return:
    """
   
    new_address = convertBytes2String(new_address)

    sql = """
    INSERT INTO public_resolver_event_address_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        new_address,
        coin_type,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, new_address, coin_type, timestamp)

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


def insert_public_resolver_event_approval_for_all(block_number,
                                                  tx_hash,
                                                  log_index,
                                                  network_id,
                                                  owner,
                                                  operator,
                                                  approved,
                                                  timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_approval_for_all(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        owner,
        operator,
        approved,
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


def insert_public_resolver_event_content_hash_changed(block_number,
                                                      tx_hash,
                                                      log_index,
                                                      network_id,
                                                      node,
                                                      hash,
                                                      timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_content_hash_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        hash,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, hash, timestamp)

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


def insert_public_resolver_event_DNS_record_changed(block_number,
                                                    tx_hash,
                                                    log_index,
                                                    network_id,
                                                    node,
                                                    name,
                                                    resource,
                                                    record,
                                                    timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_dns_record_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        name,
        resource,
        record,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, name, resource, record, timestamp)

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


def insert_public_resolver_event_DNS_record_deleted(block_number,
                                                    tx_hash,
                                                    log_index,
                                                    network_id,
                                                    node,
                                                    name,
                                                    resource,
                                                    timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_dns_record_deleted(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        name,
        resource,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, name, resource, timestamp)

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


def insert_public_resolver_event_DNS_zone_cleared(block_number,
                                                  tx_hash,
                                                  log_index,
                                                  network_id,
                                                  node,
                                                  timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_dns_zone_cleared(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, timestamp)

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


def insert_public_resolver_event_DNS_zone_hash_changed(block_number,
                                                       tx_hash,
                                                       log_index,
                                                       network_id,
                                                       node,
                                                       last_zone_hash,
                                                       zone_hash,
                                                       timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_dns_zone_hash_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        last_zone_hash,
        zone_hash,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, last_zone_hash, zone_hash, timestamp)

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


def insert_public_resolver_event_interface_changed(block_number,
                                                   tx_hash,
                                                   log_index,
                                                   network_id,
                                                   node,
                                                   interface_id,
                                                   implementer,
                                                   timestamp):
    """
    :return:
    """

    interface_id = convertBytes2String(interface_id)

    sql = """
    INSERT INTO public_resolver_event_interface_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        interface_id,
        implementer,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, interface_id, implementer, timestamp)

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


def insert_public_resolver_event_text_changed(block_number,
                                              tx_hash,
                                              log_index,
                                              network_id,
                                              node,
                                              indexed_key,
                                              key,
                                              timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_text_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        indexed_key,
        key,
        timestamp) 
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

    except Exception as e:
        print(e)
        conn.rollback()


def insert_public_resolver_event_pubkey_changed(block_number,
                                                tx_hash,
                                                log_index,
                                                network_id,
                                                node,
                                                x,
                                                y,
                                                timestamp):
    """
    :return:
    """

    sql = """
    INSERT INTO public_resolver_event_pubkey_changed(
        pk_id,
        block_number,
        tx_hash,
        log_index,
        network_id,
        node,
        x,
        y,
        timestamp) 
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, node, x, y, timestamp)

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
