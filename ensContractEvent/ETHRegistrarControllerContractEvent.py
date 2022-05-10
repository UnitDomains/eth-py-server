import json

from ensContractEvent.EnsContractEvent import EnsContractEvent
from eventState.AddressConfigure import AddressConfigure
from processEvent.ETHRegistrarControllerProcessEvent import ETHRegistrarControllerProcessEvent


class ETHRegistrarControllerContractEvent(EnsContractEvent):
    def __init__(self, web3):
        self.web3 = web3
        ABI = self.loadFile('./abis/ETHRegistrarController.json')
        abi = json.loads(ABI)
        self.ERC20 = self.web3.eth.contract(abi=abi)

    def get_contract(self):

        return self.ERC20

    def get_events(self):
        return [self.ERC20.events.NameRegistered,
                self.ERC20.events.NameRenewed,
                self.ERC20.events.NewPriceOracle,
                self.ERC20.events.OwnershipTransferred]

    def get_state(self):
        return ETHRegistrarControllerProcessEvent(self.network_id)

    def get_filters(self):
        address = AddressConfigure(self.network_id)
        return {"address": address.get_eth_registar_contract_address()}
