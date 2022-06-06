from database.event.EventDataBase import EventDataBase


class NewSubdomainRegistrationEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 label,
                 sub_domain,
                 owner,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(NewSubdomainRegistrationEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._label = label
        self._sub_domain = sub_domain
        self._owner = owner

    @property
    def label(self):
        return self._label

    @property
    def sub_domain(self):
        return self._sub_domain

    @property
    def owner(self):
        return self._owner
