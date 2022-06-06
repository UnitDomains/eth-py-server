from database.event.EventDataBase import EventDataBase


class OwnershipTransferredEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 previous_owner,
                 new_owner,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(OwnershipTransferredEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._previous_owner = previous_owner
        self._new_owner = new_owner

    @property
    def previous_owner(self):
        return self._previous_owner

    @property
    def new_owner(self):
        return self._new_owner
