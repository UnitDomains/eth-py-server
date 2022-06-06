import datetime

from web3.datastructures import AttributeDict

from processEvent.ProcessEvent import ProcessEvent


class ProcessEventImpl(ProcessEvent):

    def __init__(self,
                 network_id):
        self.network_id = network_id

    """Store the state of scanned blocks and all events.

    All state is an in-memory dict.
    Simple load/store massive JSON on start up.
    """

    def delete_data(self,
                    since_block):
        """Remove potentially reorganised blocks from the scan data."""
        for block_num in range(since_block,
                               self.get_last_scanned_block()):
            if block_num in self.state["blocks"]:
                del self.state["blocks"][block_num]

    def save_data(
            self,
            block_number,
            tx_hash,
            log_index,
            process_event_data: dict,
            event: AttributeDict) -> int:
        """Delete any data since this block was scanned.

        Purges any potential minor reorg data.
        """

    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        return {}

    def process_event(
            self,
            block_when: datetime.datetime,
            event: AttributeDict,
            ens_contract_event,
            event_type) -> str:
        """Record a ERC-20 transfer in our database."""
        # Events are keyed by their transaction hash and log index
        # One transaction may contain multiple events
        # and each one of those gets their own log index

        # event_name = event.event # "Transfer"
        log_index = event.logIndex  # Log index within the block
        # transaction_index = event.transactionIndex  # Transaction index
        # within the block
        txhash = event.transactionHash.hex()  # Transaction hash
        block_number = event.blockNumber

        process_event_data = self.get_process_event_data(block_when,
                                                         event)

        print("%d\t%d\t%-20s-->%s" % (block_number, log_index, event.event, self.__repr__()))

        self.save_data(
                block_number,
                txhash,
                log_index,
                process_event_data,
                event)

        '''

        # Create empty dict as the block that contains all transactions by txhash
        if block_number not in self.state["blocks"]:
            self.state["blocks"][block_number] = {}

        block = self.state["blocks"][block_number]
        if txhash not in block:
            # We have not yet recorded any transfers in this transaction
            # (One transaction may contain multiple events if executed by a smart contract).
            # Create a tx entry that contains all events by a log index
            self.state["blocks"][block_number][txhash] = {}

        # Record ERC-20 transfer in our database
        self.state["blocks"][block_number][txhash][log_index] = process_event_data

        '''

        # Return a pointer that allows us to look up this event later if needed
        return f"{block_number}-{txhash}-{log_index}"
