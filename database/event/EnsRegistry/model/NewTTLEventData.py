from database.event.EventDataBase import EventDataBase


class NewTTLEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 node,
                 ttl,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(NewTTLEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._node = node
        self._ttl = ttl

    @property
    def node(self):
        return self._node

    @property
    def ttl(self):
        return self._ttl
