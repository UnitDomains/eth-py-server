import json
import time

from database.database import conn, cur
from database.utils import get_uuid


def insert_domain_info(network_id,
                       name,
                       label,
                       owner,
                       cost,
                       expires,
                       base_node_index):
    """

    :return:
    """

    delete_domain_info(network_id,
                       label)

    sql = """
        INSERT INTO domain_info(
            pk_id,
            network_id,
            label,
            name,
            base_node_index,
            owner,
            expires
            ) 
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
    param = (get_uuid(), network_id, label, name, base_node_index, owner, expires)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

            from database.event.PublicResolver.AddrChanged import get_public_resolver_event_addr_changed
            addrChangedEventData = get_public_resolver_event_addr_changed(network_id,
                                                                          label)

            update_domain_info_eth_address(network_id,
                                           label,
                                           addrChangedEventData.addr)

            # update resolver
            from database.event.EnsRegistry.NewResolver import get_ens_registry_event_new_resolver
            newResolverEventData = get_ens_registry_event_new_resolver(network_id,
                                                                       label)

            update_domain_info_resolver(network_id,
                                        label,
                                        newResolverEventData.resolver)

            # controller
            from database.event.EnsRegistry.NewTLDOwner import get_ens_registry_event_new_tld_owner
            newTLDOwnerEventData = get_ens_registry_event_new_tld_owner(network_id,
                                                                        label)

            update_domain_info_controller(network_id,
                                          label,
                                          newTLDOwnerEventData.owner)
            # owner
            from database.event.BaseRegistar.Transfer import get_base_registrar_event_transfer
            transferEventData = get_base_registrar_event_transfer(network_id,
                                                                  label)

            update_domain_info_owner(network_id,
                                     label,
                                     transferEventData.to_addr)



    except Exception as e:
        print("insert_domain_info")
        print(e)
        conn.rollback()


def update_domain_info_transfer(network_id,
                                token_id,
                                from_addr,
                                to_addr):
    sql = """
        UPDATE domain_info 
        SET owner =%s
        WHERE network_id=%s AND  label=%s AND owner=%s
        """
    param = (to_addr, network_id, token_id, from_addr)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_owner")
        print(e)
        conn.rollback()


def update_domain_info_base_node_index(network_id,
                                       label,
                                       base_node_index
                                       ):
    """

    :return:
    """

    sql = """
    UPDATE domain_info 
    SET base_node_index =%s
    WHERE network_id=%s AND  label=%s
    """
    param = (base_node_index, network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_owner")
        print(e)
        conn.rollback()


def update_domain_info_owner(network_id,
                             label,
                             owner):
    """

    :return:
    """

    sql = "UPDATE domain_info SET owner =%s WHERE network_id=%s AND  label=%s"
    param = (owner, network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_owner")
        print(e)
        conn.rollback()


def update_domain_info_controller(network_id,
                                  label,
                                  controller):
    """

    :return:
    """

    sql = "UPDATE domain_info SET controller =%s WHERE network_id=%s AND  label=%s"
    param = (controller, network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_controller")
        print(e)
        conn.rollback()


def update_domain_info_resolver(network_id,
                                label,
                                resolver):
    """

    :return:
    """

    sql = "UPDATE domain_info SET resolver =%s WHERE network_id=%s AND  label=%s"
    param = (resolver, network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_resolver")
        print(e)
        conn.rollback()


def update_domain_info_expires(network_id,
                               label,
                               expires):
    """

    :return:
    """

    sql = "UPDATE domain_info SET expires =%s WHERE network_id=%s AND  label=%s"
    param = (expires, network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_expires")
        print(e)
        conn.rollback()


def update_domain_info_eth_address(network_id,
                                   label,
                                   eth_address):
    """

    :return:
    """

    sql = "UPDATE domain_info SET eth_address =%s WHERE network_id=%s AND  label=%s"
    param = (eth_address, network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_eth_address")
        print(e)
        conn.rollback()


def update_domain_info_record(network_id,
                              label,
                              key,
                              value):
    """

    :return:
    """

    oldRecord = get_domain_info_record(network_id,
                                       label)

    record = {}
    if oldRecord is not None:
        record = json.loads(oldRecord)

    record[key] = value

    jsonData = json.dumps(record)

    sql = "UPDATE domain_info SET record =%s WHERE network_id=%s AND  label=%s"
    param = (jsonData, network_id, label,)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)  # 执行,如果成功,result的值为1
            conn.commit()

    except Exception as e:
        print("update_domain_info_record")
        print(e)
        conn.rollback()


def delete_domain_info(network_id,
                       label):
    sql = """
        DELETE FROM domain_info 
        WHERE network_id=%s AND label=%s
        """
    param = (network_id, label)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("delete_domain_info")
        print(e)
        conn.rollback()


def is_exist_label(network_id,
                   label):
    sql = """
                SELECT count(*) 
                FROM domain_info 
                WHERE network_id=%s AND label=%s
                """
    param = (network_id, label)

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


    except Exception as e:

        print("is_exist_label")

        print(e)
        return False


def get_domain_info_record(network_id,
                           label
                           ):
    """
    """

    sql = """
            SELECT record 
            FROM domain_info 
            WHERE network_id=%s AND label=%s
            """
    param = (network_id, label)

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

        print("is_exist_label")

        print(e)
        return None


def removeExpiredDomain(network_id):
    GRACE_PERIOD = 86400 * 90
    time_stamp = time.time() - GRACE_PERIOD

    sql = """
            DELETE FROM domain_info 
            WHERE network_id=%s AND expires<=%s
            """
    param = (network_id, time_stamp)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("delete_domain_info")
        print(e)
        conn.rollback()
