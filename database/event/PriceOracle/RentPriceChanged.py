from database.database import conn, cur
from database.info.PriceInfo import update_price_info_rent_price
from database.utils import get_uuid


def insert_price_oracle_event_rent_price_changed(block_number,
                                                 tx_hash,
                                                 log_index,
                                                 network_id,
                                                 prices,
                                                 timestamp):
    delete_price_oracle_event_rent_price_changed(network_id,
                                                 block_number,
                                                 tx_hash,
                                                 log_index
                                                 )

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
    param = (get_uuid(), block_number, tx_hash, log_index, network_id, str(prices), timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            update_price_info_rent_price(network_id,
                                         str(prices))




    except Exception as e:
        print("insert_price_oracle_event_rent_price_changed")
        print(e)
        conn.rollback()


def delete_price_oracle_event_rent_price_changed(network_id,
                                                 block_number,
                                                 tx_hash,
                                                 log_index
                                                 ):
    sql = """
        DELETE FROM price_oracle_event_rent_price_changed 
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
        print("delete_price_oracle_event_rent_price_changed")
        print(e)
        conn.rollback()


def delete_price_oracle_event_rent_price_changed_after_block(network_id,
                                                             block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM price_oracle_event_rent_price_changed 
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
        print("delete_price_oracle_event_rent_price_changed_after_block")
        print(e)
        conn.rollback()
