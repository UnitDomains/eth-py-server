from database.event.EventDataBase import EventDataBase


class NewBaseNodeEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 basenode,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(NewBaseNodeEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._basenode = basenode

    @property
    def basenode(self):
        return self._basenode
 