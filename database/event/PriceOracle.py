from database.database import conn, cur
from database.info.PriceInfo import update_price_info_payment_type, update_price_info_register_price, \
    update_price_info_rent_price
from database.utils import get_uuid


def insert_price_oracle_event_ownership_transferred(block_number,
                                                    tx_hash,
                                                    log_index,
                                                    network_id,
                                                    previous_owner,
                                                    new_owner,
                                                    timestamp):
    """

    :return:
    """

    sql = """
        INSERT INTO price_oracle_event_oracle_changed(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            previous_owner,
            new_owner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
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


def insert_price_oracle_event_oracle_changed(block_number,
                                             tx_hash,
                                             log_index,
                                             network_id,
                                             oracle,
                                             timestamp):
    """

    :return:
    """

    sql = """
        INSERT INTO price_oracle_event_oracle_changed(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            oracle
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, oracle, timestamp)

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


def insert_price_oracle_event_payment_type_changed(block_number,
                                                   tx_hash,
                                                   log_index,
                                                   network_id,
                                                   payment_types,
                                                   timestamp):
    """

    :return:
    """

    sql = """
            INSERT INTO price_oracle_event_payment_type_changed(
                pk_id,
                block_number,
                tx_hash,
                log_index,
                network_id,
                payment_types,
                timestamp) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, payment_types, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_price_info_payment_type(network_id,
                                           payment_types)

    except Exception as e:
        print(e)
        conn.rollback()


def insert_price_oracle_event_register_price_changed(block_number,
                                                     tx_hash,
                                                     log_index,
                                                     network_id,
                                                     prices,
                                                     timestamp):
    sql = """
        INSERT INTO price_oracle_event_register_price_changed(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            prices,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, prices, new_owner, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_price_info_register_price(network_id,
                                             prices)




    except Exception as e:
        print(e)
        conn.rollback()


def insert_price_oracle_event_rent_price_changed(block_number,
                                                 tx_hash,
                                                 log_index,
                                                 network_id,
                                                 prices,
                                                 timestamp):
    sql = """
        INSERT INTO price_oracle_event_rent_price_changed(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            prices,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, prices, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_price_info_rent_price(network_id,
                                         prices)




    except Exception as e:
        print(e)
        conn.rollback()
