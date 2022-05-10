import configparser


class AddressConfigure:
    def __init__(self, network_id):
        self.fname = "addressConfig.ini"
        con = configparser.ConfigParser()
        con.read(self.fname, encoding='utf-8')
        if network_id == 1:
            items = con.items('address_mainnet')
        elif network_id == 3:
            items = con.items('address_ropsten')
        elif network_id == 4:
            items = con.items('address_rinkeby')

        self.items = dict(items)

    def get_ens_contract_address(self):
        return self.items["ens_registar"]

    def get_base_registar_contract_address(self):
        """The number of the last block we have stored."""
        return self.items["base_registar"]

    def get_eth_registar_contract_address(self):
        """The number of the last block we have stored."""
        return self.items["eth_controller"]

    def get_public_resolver_contract_address(self):
        """The number of the last block we have stored."""
        return self.items["public_resolver"]

    def get_reverse_registar_contract_address(self):
        """The number of the last block we have stored."""
        return self.items["reverse_registar"]

    def get_liner_preminum_price_oracle_contract_address(self):
        """The number of the last block we have stored."""
        return self.items["price_oracle"]

    def get_subdomain_registrar_contract_address(self):
        """The number of the last block we have stored."""
        return self.items["subdomain_registrar"]
