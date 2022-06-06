from database.event.EventDataBase import EventDataBase


class NewTLDOwnerEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 node,
                 node_label,
                 owner,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(NewTLDOwnerEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._node = node
        self._node_label = node_label
        self._owner = owner

    @property
    def node(self):
        return self._node

    @property
    def owner(self):
        return self._owner

    @property
    def node_label(self):
        return self._node_label
