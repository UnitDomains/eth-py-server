from database.event.EventDataBase import EventDataBase


class ApprovalEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 owner,
                 approved,
                 token_id,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(ApprovalEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._approved = approved
        self._owner = owner
        self._token_id = token_id

    @property
    def approved(self):
        return self._approved

    @property
    def token_id(self):
        return self._token_id

    @property
    def owner(self):
        return self._owner
