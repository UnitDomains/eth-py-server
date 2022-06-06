from database.event.EventDataBase import EventDataBase


class NameMigratedEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 id,
                 owner,
                 expires,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(NameMigratedEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._id = id
        self._owner = owner
        self._expires = expires

    @property
    def id(self):
        return self._id

    @property
    def expires(self):
        return self._expires

    @property
    def owner(self):
        return self._owner
