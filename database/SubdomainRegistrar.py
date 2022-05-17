from database.SubdomainInfo import delete_subdomain_info, insert_subdomain_info
from database.database import conn, cur
from database.utils import get_uuid


def insert_subdomain_registrar_event_new_subdomain_registration(block_number,
                                                                tx_hash,
                                                                log_index,
                                                                network_id,
                                                                label,
                                                                sub_domain,
                                                                sub_node_label,
                                                                owner,
                                                                timestamp):
    """
    event NewSubdomainRegistration(
                bytes32 indexed label,
                string subdomain,
                bytes32 indexed subdomainLabel,
                address indexed owner
             );
    :return:
    """

    sql = """
        INSERT INTO subdomain_registrar_event_new_subdomain_registration(
            pk_id,
            block_number,
            tx_hash,
            log_index,
            network_id,
            label,
            sub_domain,
            sub_node_label,
            owner,
            timestamp) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (
        get_uuid(), block_number, tx_hash, log_index, network_id, label, sub_domain, sub_node_label, owner, timestamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            print("insert_subdomain_info")
            insert_subdomain_info(network_id,
                                  label,
                                  sub_node_label,
                                  sub_domain,
                                  owner)

    except Exception as e:
        print(e)
        conn.rollback()


def insert_subdomain_registrar_event_delete_subdomain(block_number,
                                                      tx_hash,
                                                      log_index,
                                                      network_id,
                                                      node,
                                                      label,
                                                      timestamp):
    """
     event DeleteSubdomain(bytes32 indexed node, bytes32 indexed label);
    :return:
    """

    sql = """
            INSERT INTO subdomain_registrar_event_delete_subdomain(
                pk_id,
                block_number,
                tx_hash,
                log_index,
                network_id,
                node,
                label,
                timestamp) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
    param = (
        get_uuid(), block_number, tx_hash, log_index, network_id, node, label, timestamp)
    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            delete_subdomain_info(network_id,
                                  node,
                                  label)

    except Exception as e:
        print(e)
        conn.rollback()
