class EventDataBase:

    def __init__(self,
                 pk_id,
                 network_id,
                 block_number,
                 tx_hash,
                 log_index,
                 timestamp,
                 op_time):
        self._pk_id = pk_id
        self._network_id = network_id
        self._block_number = block_number
        self._tx_hash = tx_hash
        self._log_index = log_index
        self._timestamp = timestamp
        self._op_time = op_time

    @property
    def pk_id(self):
        return self._pk_id

    @property
    def network_id(self):
        return self._network_id

    @property
    def block_number(self):
        return self._block_number

    @property
    def tx_hash(self):
        return self._tx_hash

    @property
    def log_index(self):
        return self._log_index

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def op_time(self):
        return self._op_time
