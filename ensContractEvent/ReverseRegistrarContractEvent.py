import json

from ensContractEvent.EnsContractEvent import EnsContractEvent
from eventState.AddressConfigure import AddressConfigure
from processEvent.ReverseRegistrarProcessEvent import ReverseRegistrarProcessEvent


class ReverseRegistrarContractEvent(EnsContractEvent):

    def __init__(self, web3, network_id):
        EnsContractEvent.__init__(self, web3, network_id)
        ABI = self.loadFile('./abis/ReverseRegistrar.json')
        abi = json.loads(ABI)
        self.ERC20 = self.web3.eth.contract(abi=abi)

    def get_contract(self):

        return self.ERC20

    def get_events(self):
        return [self.ERC20.events.ControllerChanged,
                self.ERC20.events.OwnershipTransferred,
                self.ERC20.events.ReverseClaimed
                ]

    def get_state(self):
        return ReverseRegistrarProcessEvent(self.network_id)

    def get_filters(self):
        address = AddressConfigure(self.network_id)
        return {"address": address.get_reverse_registar_contract_address()}
