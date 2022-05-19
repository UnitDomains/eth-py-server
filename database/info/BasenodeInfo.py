from database.database import conn, cur
from database.utils import get_uuid


def insert_basenode_info_basenode(network_id,
                                  node,
                                  name):
    reverse = 0

    sql = """
        INSERT INTO basenode_info(
            pk_id,
            network_id,
            node,
            name) 
        VALUES (%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, node, name)

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
