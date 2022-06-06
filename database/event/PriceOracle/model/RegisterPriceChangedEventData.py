from database.event.EventDataBase import EventDataBase


class RegisterPriceChangedEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 node,
                 owner,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(RegisterPriceChangedEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._node = node
        self._owner = owner

    @property
    def node(self):
        return self._node

    @property
    def owner(self):
        return self._owner
