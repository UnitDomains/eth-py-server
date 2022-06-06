import json

from web3 import Web3

from database.database import conn, cur
from database.event.EnsRegistry.NewResolver import get_ens_registry_event_new_resolver
from database.event.EnsRegistry.Transfer import get_ens_registry_event_transfer
from database.event.PublicResolver.AddrChanged import get_public_resolver_event_addr_changed
from database.utils import get_uuid


def insert_subdomain_info(network_id,
                          label,
                          sub_domain,
                          owner):
    """

    :return:
    """

    subLabel = (Web3.keccak(text=sub_domain).hex())
    node = Web3.solidityKeccak(['bytes32', 'bytes32'],
                               [label,
                                subLabel])

    node = node.hex()

    delete_subdomain_info(network_id,
                          label,
                          node
                          )

    sql = """
        INSERT INTO subdomain_info(
            pk_id,
            network_id,
            label,
            sub_node_label,            
            sub_domain,
            owner,
            controller,
            eth_address
            ) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, label, node, sub_domain, owner, owner, owner)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            # update owner
            '''
            newOwner = get_ens_registry_event_new_owner(network_id,
                                                        label,
                                                        subLabel)

            update_subdomain_info_controller(network_id,
                                             label,
                                             sub_domain,
                                             newOwner)
            '''

            # update eth address
            addrChangedEventData = get_public_resolver_event_addr_changed(network_id,
                                                                          node)

            update_subdomain_info_eth_address(network_id,
                                              node,
                                              addrChangedEventData.addr)

            # update resolver
            newResolverEventData = get_ens_registry_event_new_resolver(network_id,
                                                                       node)

            update_subdomain_info_resolver(network_id,
                                           node,
                                           newResolverEventData.resolver)

            transferEventData = get_ens_registry_event_transfer(network_id,
                                                                node)
            update_subdomain_info_owner(network_id,
                                        node,
                                        transferEventData.owner)




    except Exception as e:
        print("insert_subdomain_info")
        print(e)
        conn.rollback()


def delete_subdomain_info(network_id,
                          label,
                          sub_node_label):
    sql = """
        DELETE FROM subdomain_info 
        WHERE network_id=%s AND label=%s AND sub_node_label=%s
        """
    param = (network_id, label, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("delete_subdomain_info")
        print(e)
        conn.rollback()


def update_subdomain_info_owner(network_id,
                                sub_node_label,
                                owner):
    sql = "UPDATE subdomain_info SET owner =%s WHERE network_id=%s AND sub_node_label=%s"
    param = (owner, network_id, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("update_subdomain_info_owner")
        print(e)
        conn.rollback()


def update_subdomain_info_controller(network_id,
                                     sub_node_label,
                                     controller):
    sql = "UPDATE subdomain_info SET controller =%s WHERE network_id=%s AND sub_node_label=%s"
    param = (controller, network_id, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("update_subdomain_info_controller")
        print(e)
        conn.rollback()


def update_subdomain_info_resolver(network_id,
                                   sub_node_label,
                                   resolver):
    sql = "UPDATE subdomain_info SET resolver =%s WHERE network_id=%s AND sub_node_label=%s"
    param = (resolver, network_id, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("update_subdomain_info_resolver")
        print(e)
        conn.rollback()


def update_subdomain_info_eth_address(network_id,
                                      sub_node_label,
                                      eth_address):
    sql = "UPDATE subdomain_info SET eth_address =%s WHERE network_id=%s AND sub_node_label=%s"
    param = (eth_address, network_id, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("update_subdomain_info_eth_address")
        print(e)
        conn.rollback()


def update_subdomain_info_content_hash(network_id,
                                       sub_node_label,
                                       content_hash):
    sql = "UPDATE subdomain_info SET content_hash =%s WHERE network_id=%s AND sub_node_label=%s"
    param = (content_hash, network_id, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("update_subdomain_info_content_hash")
        print(e)
        conn.rollback()


def update_subdomain_info_record(network_id,
                                 sub_node_label,
                                 key,
                                 value):
    """

    :return:
    """

    oldRecord = get_subdomain_info_record_by_sub_node_label(network_id,
                                                            sub_node_label)

    record = {}
    if oldRecord is not None:
        record = json.loads(oldRecord)

    record[key] = value

    jsonData = json.dumps(record)

    sql = "UPDATE subdomain_info SET record =%s WHERE network_id=%s AND  sub_node_label=%s"
    param = (jsonData, network_id, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_subdomain_info_record")
        print(e)
        conn.rollback()


def get_subdomain_info_record(network_id,
                              label,
                              sub_domain,
                              ):
    """
    """

    sql = """
            SELECT record 
            FROM subdomain_info 
            WHERE network_id=%s AND label=%s AND sub_domain=%s
            """
    param = (network_id, label, sub_domain)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            return row[0]

        return None


    except Exception as e:

        print("get_subdomain_info_record")

        print(e)
        return None


def get_subdomain_info_record_by_sub_node_label(network_id,
                                                sub_node_label
                                                ):
    """
    """

    sql = """
            SELECT record 
            FROM subdomain_info 
            WHERE network_id=%s AND sub_node_label=%s
            """
    param = (network_id, sub_node_label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            return row[0]

        return None


    except Exception as e:

        print("get_subdomain_info_record_by_sub_node_label")

        print(e)
        return None
