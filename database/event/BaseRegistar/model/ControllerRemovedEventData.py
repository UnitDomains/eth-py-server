from database.event.EventDataBase import EventDataBase


class ControllerRemovedEventData(EventDataBase):

    def __init__(self,
                 pk_id,
                 controller,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        super(ControllerRemovedEventData,
              self).__init__(pk_id,
                             network_id,
                             block_number,
                             tx_hash,
                             log_index,
                             timestamp,
                             op_time)

        self._controller = controller

    @property
    def controller(self):
        return self._controller
