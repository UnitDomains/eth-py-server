from database.event.EventDataBase import EventDataBase


class NewResolverEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 node,
                 resolver,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(NewResolverEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._node = node
        self._resolver = resolver

    @property
    def node(self):
        return self._node

    @property
    def resolver(self):
        return self._resolver
