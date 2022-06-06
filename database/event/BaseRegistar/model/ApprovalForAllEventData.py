from database.event.EventDataBase import EventDataBase


class ApprovalForAllEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 owner,
                 operator,
                 approved,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(ApprovalForAllEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._operator = operator
        self._approved = approved
        self._owner = owner

    @property
    def operator(self):
        return self._operator

    @property
    def approved(self):
        return self._approved

    @property
    def owner(self):
        return self._owner
