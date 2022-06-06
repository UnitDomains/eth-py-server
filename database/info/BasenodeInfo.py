from database.database import conn, cur
from database.utils import get_uuid


def insert_basenode_info_basenode(network_id,
                                  basenode,
                                  name):
    basenode_index = get_basenode_count(network_id)

    sql = """
        INSERT INTO basenode_info(
            pk_id,
            network_id,
            basenode,
            basenode_index,
            name) 
        VALUES (%s,%s,%s,%s,%s)
    """
    param = (get_uuid(), network_id, basenode, basenode_index, name)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        if cur:
            result = cur.execute(sql,
                                 param)
            conn.commit()

    except Exception as e:
        print("insert_basenode_info_basenode")
        print(e)
        conn.rollback()


def get_basenode_count(network_id):
    """
    """

    sql = """
        SELECT count(*) 
        FROM basenode_info 
        WHERE network_id=%s
    """
    param = (network_id)

    try:

        # Check whether the connection is disconnected. If it is disconnected, reconnect the database
        conn.ping(reconnect=True)

        cur.execute(sql,
                    param)

        if cur.rowcount > 0:
            row = cur.fetchone()

            return row[0]

        return 0


    except Exception as e:
        print("get_basenode_count")
        print(e)
        return 0
