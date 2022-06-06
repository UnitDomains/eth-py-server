from database.database import conn, cur
from database.event.BaseRegistar.model.ControllerRemovedEventData import ControllerRemovedEventData
from database.utils import get_uuid

base_registrar_event_controller_removed_table_columns = [
    'pk_id', 'node', 'addr', 'network_id', 'block_number', 'tx_hash', 'log_index', 'timestamp', 'op_time'
]


def insert_base_registrar_event_controller_removed(block_number,
                                                   tx_hash,
                                                   log_index,
                                                   network_id,
                                                   controller,
                                                   timestamp):
    delete_base_registrar_event_controller_removed(network_id,
                                                   block_number,
                                                   tx_hash,
                                                   log_index)

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
        print("insert_base_registrar_event_controller_removed")
        print(e)
        conn.rollback()


def delete_base_registrar_event_controller_removed(network_id,
                                                   block_number,
                                                   tx_hash,
                                                   log_index):
    sql = """
        DELETE FROM base_registrar_event_controller_removed 
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
        print("delete_base_registrar_event_controller_removed")
        print(e)
        conn.rollback()


def delete_base_registrar_event_controller_removed_after_block(network_id,
                                                               block_number):
    '''
    Purge old data in the case of blockchain reorganisation
    :param network_id:
    :param block_number:
    :return:
    '''
    sql = """
        DELETE FROM base_registrar_event_controller_removed 
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
        print("delete_base_registrar_event_controller_removed_after_block")
        print(e)
        conn.rollback()


def convertRow2ControllerRemovedEventData(row):
    '''
    pk_id, node, node_label,owner, network_id, block_number, tx_hash, log_index, timestamp, op_time
    :param row:
    :return:
    '''
    pk_id = row[0]
    controller = row[1]
    network_id = row[2]
    block_number = row[3]
    tx_hash = row[4]
    log_index = row[5]
    timestamp = row[6]
    op_time = row[7]

    return ControllerRemovedEventData(pk_id,
                                      controller,
                                      network_id,
                                      block_number,
                                      tx_hash,
                                      log_index,
                                      timestamp,
                                      op_time)


def get_base_registrar_event_controller_removed(network_id,
                                                node
                                                ):
    """
    """

    sql = """
            SELECT pk_id, controller, network_id, block_number, tx_hash, log_index, timestamp, op_time  
            FROM base_registrar_event_controller_removed 
            WHERE network_id=%s AND node=%s
            ORDER BY block_number DESC ,log_index DESC 
            LIMIT 0,1
            """
    param = (network_id, node)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            return convertRow2ControllerRemovedEventData(row)

        return None


    except Exception as e:

        print("get_base_registrar_event_controller_removed")

        print(e)
        return None
