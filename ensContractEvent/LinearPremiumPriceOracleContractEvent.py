import json

from ensContractEvent.EnsContractEvent import EnsContractEvent
from eventState.AddressConfigure import AddressConfigure
from processEvent.LinearPremiumPriceOracleProcessEvent import LinearPremiumPriceOracleProcessEvent


class LinearPremiumPriceOracleContractEvent(EnsContractEvent):
    def __init__(self, web3):
        self.web3 = web3
        ABI = self.loadFile('./abis/LinearPremiumPriceOracle.json')
        abi = json.loads(ABI)
        self.ERC20 = self.web3.eth.contract(abi=abi)

    def get_contract(self):

        return self.ERC20

    def get_events(self):
        return [self.ERC20.events.OracleChanged,
                self.ERC20.events.OwnershipTransferred,
                self.ERC20.events.PaymentTypeChanged,
                self.ERC20.events.RegisterPriceChanged,
                self.ERC20.events.RentPriceChanged]

    def get_state(self):
        return LinearPremiumPriceOracleProcessEvent(self.network_id)

    def get_filters(self):
        address = AddressConfigure(self.network_id)
        return {
            "address": address.get_liner_preminum_price_oracle_contract_address()}
