import datetime
from abc import ABC, abstractmethod

from web3.datastructures import AttributeDict


# Currently this method is not exposed over official web3 API,
# but we need it to construct eth_getLogs parameters


class ProcessEvent(ABC):
    """Application state that remembers what blocks we have scanned in the case of crash.
    """

    @abstractmethod
    def process_event(
            self,
            block_when: datetime.datetime,
            event: AttributeDict,
            ens_contract_event,
            event_type) -> object:
        """Process incoming events.

        This function takes raw events from Web3, transforms them to your application internal
        format, then saves them in a database or some other state.

        :param block_when: When this block was mined

        :param event: Symbolic dictionary of the event data

        :return: Internal state structure that is the result of event tranformation.
        """

    @abstractmethod
    def delete_data(self, since_block: int) -> int:
        """Delete any data since this block was scanned.

        Purges any potential minor reorg data.
        """

    @abstractmethod
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
