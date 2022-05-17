import datetime
from abc import ABC, abstractmethod

from web3.datastructures import AttributeDict


# Currently this method is not exposed over official web3 API,
# but we need it to construct eth_getLogs parameters


class EventScannerState(ABC):
    """Application state that remembers what blocks we have scanned in the case of crash.
    """

    @abstractmethod
    def get_last_scanned_block(self) -> int:
        """Number of the last block we have scanned on the previous cycle.

        :return: 0 if no blocks scanned yet
        """

    @abstractmethod
    def start_chunk(self,
                    block_number: int):
        """Scanner is about to ask data of multiple blocks over JSON-RPC.

        Start a database session if needed.
        """

    @abstractmethod
    def end_chunk(self,
                  block_number: int):
        """Scanner finished a number of blocks.

        Persistent any data in your state now.
        """
