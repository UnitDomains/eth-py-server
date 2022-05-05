import configparser


class AddressConfigure:
    def __init__(self):
        self.fname = "config.ini"
        con = configparser.ConfigParser()
        con.read(self.fname, encoding='utf-8')
        items = con.items('address')
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
