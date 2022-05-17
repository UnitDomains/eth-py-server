import json

from ensContractEvent.EnsContractEvent import EnsContractEvent
from eventState.AddressConfigure import AddressConfigure
from processEvent.BaseRegistrarProcessEvent import BaseRegistarProcessEvent


class BaseRegistarContractEvent(EnsContractEvent):

    def __init__(self,
                 web3,
                 network_id):
        EnsContractEvent.__init__(self,
                                  web3,
                                  network_id)
        ABI = self.loadFile('./abis/BaseRegistrarImplementation.json')
        abi = json.loads(ABI)
        self.ERC20 = self.web3.eth.contract(abi=abi)

    def get_contract(self):
        return self.ERC20

    def get_events(self):
        return [
            self.ERC20.events.Approval,
            self.ERC20.events.ApprovalForAll,
            self.ERC20.events.ControllerAdded,
            self.ERC20.events.ControllerRemoved,
            self.ERC20.events.NameMigrated,
            self.ERC20.events.NameRegistered,
            self.ERC20.events.NameRenewed,
            self.ERC20.events.OwnershipTransferred,
            self.ERC20.events.Transfer
        ]

    def get_state(self):
        return BaseRegistarProcessEvent(self.network_id)

    def get_filters(self):
        address = AddressConfigure(self.network_id)
        return {"address": address.get_base_registar_contract_address()}
