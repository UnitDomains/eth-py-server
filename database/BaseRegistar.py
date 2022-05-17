import pymysql

from database.DomainInfo import update_domain_info_transfer
from database.database import conn, cur
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
                                         tokenId,
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
            tokenId,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, from_addr, to_addr, tokenId, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_domain_info_transfer(network_id,
                                        tokenId,
                                        from_addr,
                                        to_addr)


    except Exception as e:
        print(e)
        conn.rollback()
