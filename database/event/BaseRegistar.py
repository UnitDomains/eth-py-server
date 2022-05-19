from database.database import conn, cur
from database.info.BasenodeInfo import insert_basenode_info_basenode
from database.info.DomainInfo import update_domain_info_transfer
from database.utils import get_uuid


def insert_base_registrar_event_name_registered(block_number,
                                                tx_hash,
                                                log_index,
                                                network_id,
                                                id,
                                                owner,
                                                expires,
                                                timestamp):
    """

    :return:
    """

    sql = """
        INSERT INTO base_registrar_event_name_registered(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            id,
            owner,
            expires,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, id, owner, expires, timestamp)

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


def insert_base_registrar_event_name_renewed(block_number,
                                             tx_hash,
                                             log_index,
                                             network_id,
                                             id,
                                             expires,
                                             timestamp):
    """

    :return:
    """

    sql = """
            INSERT INTO base_registrar_event_name_renewed(
                pk_id,
                block_number,
                tx_hash,
                log_index,
                network_id,
                id,
                expires,
                timestamp) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, id, expires, timestamp)

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


def insert_base_registrar_event_transfer(block_number,
                                         tx_hash,
                                         log_index,
                                         network_id,
                                         from_addr,
                                         to_addr,
                                         token_id,
                                         timestamp):
    sql = """
        INSERT INTO base_registrar_event_transfer(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            from_addr,
            to_addr,
            token_id,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, from_addr, to_addr, token_id, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_domain_info_transfer(network_id,
                                        token_id,
                                        from_addr,
                                        to_addr)


    except Exception as e:
        print(e)
        conn.rollback()


def insert_base_registrar_event_approval(block_number,
                                         tx_hash,
                                         log_index,
                                         network_id,
                                         owner,
                                         approved,
                                         token_id,
                                         timestamp):
    sql = """
        INSERT INTO base_registrar_event_approval(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            owner,
            approved,
            token_id,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, owner, approved, token_id, timestamp)

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


def insert_base_registrar_event_approval_for_all(block_number,
                                                 tx_hash,
                                                 log_index,
                                                 network_id,
                                                 owner,
                                                 operator,
                                                 approved,
                                                 timestamp):
    sql = """
        INSERT INTO base_registrar_event_approval_for_all(
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


def insert_base_registrar_event_controller_added(block_number,
                                                 tx_hash,
                                                 log_index,
                                                 network_id,
                                                 controller,
                                                 timestamp):
    sql = """
        INSERT INTO base_registrar_event_controller_added(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            controller,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, controller, timestamp)

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


def insert_base_registrar_event_controller_removed(block_number,
                                                   tx_hash,
                                                   log_index,
                                                   network_id,
                                                   controller,
                                                   timestamp):
    sql = """
        INSERT INTO base_registrar_event_controller_removed(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            controller,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, controller, timestamp)

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


def insert_base_registrar_event_name_migrated(block_number,
                                              tx_hash,
                                              log_index,
                                              network_id,
                                              id,
                                              owner,
                                              expires,
                                              timestamp):
    sql = """
        INSERT INTO base_registrar_event_name_migrated(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            id,
            owner,
            expires,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, id, owner, expires, timestamp)

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


def insert_base_registrar_event_new_basenode(block_number,
                                             tx_hash,
                                             log_index,
                                             network_id,
                                             basenode,
                                             timestamp):
    sql = """
        INSERT INTO base_registrar_event_new_basenode(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            basenode,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, basenode, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            insert_basenode_info_basenode(network_id,
                                          basenode,
                                          "")




    except Exception as e:
        print(e)
        conn.rollback()


def insert_base_registrar_event_ownership_transferred(block_number,
                                                      tx_hash,
                                                      log_index,
                                                      network_id,
                                                      previous_owner,
                                                      new_owner,
                                                      timestamp):
    sql = """
        INSERT INTO base_registrar_event_ownership_transferred(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            previous_owner,
            new_owner,            
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, previous_owner, new_owner, timestamp)

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
