from database.event.EventDataBase import EventDataBase


class TransferEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 from_addr,
                 to_addr,
                 token_id,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(TransferEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._from_addr = from_addr
        self._to_addr = to_addr
        self._token_id = token_id

    @property
    def from_addr(self):
        return self._from_addr

    @property
    def to_addr(self):
        return self._to_addr

    @property
    def token_id(self):
        return self._token_id
