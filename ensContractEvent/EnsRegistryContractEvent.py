import json

from ensContractEvent.EnsContractEvent import EnsContractEvent
from eventState.AddressConfigure import AddressConfigure
from processEvent.EnsRegistryProcessEvent import EnsRegistryProcessEvent


class EnsRegistryContractEvent(EnsContractEvent):
    def __init__(self,
                 web3,
                 network_id):
        EnsContractEvent.__init__(self,
                                  web3,
                                  network_id)
        ABI = self.loadFile('./abis/ENSRegistry.json')
        abi = json.loads(ABI)
        self.ERC20 = self.web3.eth.contract(abi=abi)

    def get_contract(self):
        return self.ERC20

    def get_events(self):
        return [self.ERC20.events.ApprovalForAll,
                self.ERC20.events.NewOwner,
                self.ERC20.events.NewTLDOwner,
                self.ERC20.events.NewResolver,
                self.ERC20.events.NewTTL,
                self.ERC20.events.Transfer
                ]

    def get_state(self):
        return EnsRegistryProcessEvent(self.network_id)

    def get_filters(self):
        address = AddressConfigure(self.network_id)
        return {"address": address.get_ens_contract_address()}
