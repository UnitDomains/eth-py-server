import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_price_info_default(network_id):
    """

    :return:
    """

    sql = """
        INSERT INTO price_info(
            pk_id,
            network_id,
            register_price,
            rent_price,
            payment_type) 
        VALUES (%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, "", "", 0)

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


def update_price_info_register_price(network_id,
                                     register_price):
    """

    :return:
    """

    if not is_exist_price(network_id):
        insert_price_info_default(network_id)

    sql = "UPDATE price_info SET register_price =%s WHERE network_id=%s"
    param = (register_price, network_id)

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


def update_price_info_rent_price(network_id,
                                 rent_price):
    """
    60:ETH,See the documentation for more details on coin types
    :return:
    """

    if not is_exist_price(network_id):
        insert_price_info_default(network_id)

    sql = "UPDATE price_info SET rent_price =%s WHERE network_id=%s"
    param = (rent_price, network_id)

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


def update_price_info_payment_type(network_id,
                                   payment_type):
    """
    60:ETH,See the documentation for more details on coin types
    :return:
    """

    if not is_exist_price(network_id):
        insert_price_info_default(network_id)

    sql = "UPDATE price_info SET payment_type =%s WHERE network_id=%s"
    param = (payment_type, network_id)

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


def is_exist_price(network_id):
    """
    """

    sql = "select count(*) from price_info where network_id= %s"
    param = (network_id)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            if row[0] == 1:
                return True

        return False

    except pymysql.ProgrammingError as e:
        return False
