import logging

from web3 import Web3

# Currently this method is not exposed over official web3 API,
# but we need it to construct eth_getLogs parameters

logger = logging.getLogger(__name__)


class EnsContractEvent:
    def __init__(self, web3: Web3):
        self.logger = logger
        self.web3 = web3

    def get_contract(self):
        return

    def get_events(self):
        return []

    def get_state(self):
        return

    def loadFile(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
            return data

    def get_filters(self):
        return {}
