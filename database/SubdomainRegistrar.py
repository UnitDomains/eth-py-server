import pymysql

from database.database import conn, cur
from database.utils import get_uuid


def insert_subdomain_registrar_event_new_subdomain_registration(network_id,label, sub_domain,sub_node_label, owner,timestamp):
    """
    event NewSubdomainRegistration(
                bytes32 indexed label,
                string subdomain,
                bytes32 indexed subdomainLabel,
                address indexed owner
             );
    :return:
    """

    delete_subdomain_registrar_event_new_subdomain_registration(network_id,label,sub_node_label)

    sql = """
        INSERT INTO subdomain_registrar_event_new_subdomain_registration(
            pk_id,
            network_id,
            label,
            sub_domain,
            sub_node_label,
            owner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id,label, sub_domain,sub_node_label, owner,timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def insert_subdomain_registrar_event_delete_subdomain(network_id,label, sub_node_label, timestamp):
    """
     event DeleteSubdomain(bytes32 indexed node, bytes32 indexed label);
    :return:
    """

    sql = """
        DELETE FROM subdomain_registrar_event_new_subdomain_registration 
        WHERE network_id=%s AND label=%s AND sub_node_label=%s
        """
    param = (network_id,label, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()


def delete_subdomain_registrar_event_new_subdomain_registration(network_id,label,sub_node_label):
    """

    :return:
    """

    sql = """
        DELETE FROM subdomain_registrar_event_new_subdomain_registration 
        WHERE network_id=%s AND label=%s AND sub_node_label=%s
        """
    param = (network_id,label,sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql, param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()




def is_exist_phrase(word):
    """

    """

    sql = 'select count(*) from subdomain_registrar_event_new_subdomain_registration where word= "%s"' % word

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql)

        if cur.rowcount > 0:
            row = cur.fetchone()

            if row[0] == 1:
                return True

        return False

    except pymysql.ProgrammingError as e:
        return False
