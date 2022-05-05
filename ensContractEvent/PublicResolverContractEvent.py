import json

from ensContractEvent.EnsContractEvent import EnsContractEvent
from eventState.AddressConfigure import AddressConfigure
from processEvent.PublicResolverProcessEvent import PublicResolverProcessEvent


class PublicResolverContractEvent(EnsContractEvent):
    def __init__(self, web3):
        self.web3 = web3
        ABI = self.loadFile('./abis/PublicResolver.json')
        abi = json.loads(ABI)
        self.ERC20 = self.web3.eth.contract(abi=abi)

    def get_contract(self):

        return self.ERC20

    def get_events(self):
        return [self.ERC20.events.ABIChanged,
                self.ERC20.events.AddrChanged,
                self.ERC20.events.AddressChanged,
                self.ERC20.events.ApprovalForAll,
                self.ERC20.events.ContenthashChanged,
                self.ERC20.events.DNSRecordChanged,
                self.ERC20.events.DNSRecordDeleted,
                self.ERC20.events.DNSZoneCleared,
                self.ERC20.events.DNSZonehashChanged,
                self.ERC20.events.InterfaceChanged,
                self.ERC20.events.NameChanged,
                self.ERC20.events.PubkeyChanged,
                self.ERC20.events.TextChanged]

    def get_state(self):
        return PublicResolverProcessEvent()

    def get_filters(self):
        address = AddressConfigure()
        return {"address": address.get_public_resolver_contract_address()}
