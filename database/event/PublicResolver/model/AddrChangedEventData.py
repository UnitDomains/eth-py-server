from database.event.EventDataBase import EventDataBase


class AddrChangedEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 node,
                 addr,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(AddrChangedEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)
        self._node = node
        self._addr = addr

    @property
    def node(self):
        return self._node

    @property
    def addr(self):
        return self._addr
