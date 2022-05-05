import json

from ensContractEvent.EnsContractEvent import EnsContractEvent
from eventState.AddressConfigure import AddressConfigure
from processEvent.PublicResolverProcessEvent import PublicResolverProcessEvent
from processEvent.SubdomainRegistrarProcessEvent import SubdomainRegistrarProcessEvent


class SubdomainRegistrarContractEvent(EnsContractEvent):
    def __init__(self, web3):
        self.web3 = web3
        ABI = self.loadFile('./abis/SubdomainRegistrar.json')
        abi = json.loads(ABI)
        self.ERC20 = self.web3.eth.contract(abi=abi)

    def get_contract(self):

        return self.ERC20

    def get_events(self):
        return [self.ERC20.events.DeleteSubdomain,
                self.ERC20.events.NewSubdomainRegistration
               ]

    def get_state(self):
        return SubdomainRegistrarProcessEvent()

    def get_filters(self):
        address = AddressConfigure()
        return {"address": address.get_subdomain_registrar_contract_address()}
