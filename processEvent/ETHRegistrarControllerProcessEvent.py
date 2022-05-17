import datetime

from web3.datastructures import AttributeDict

from database.EthRegistrarController import insert_eth_registrar_controller_event_ownership_transferred, \
    insert_eth_registrar_controller_event_name_renewed, \
    insert_eth_registrar_controller_event_name_registered
from processEvent.ProcessEventImpl import ProcessEventImpl


def NameRegistered(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "name": args["name"],
        "label": args["label"],
        "owner": args["owner"],
        "cost": args["cost"],
        "expires": args["expires"],
        "baseNodeIndex": args["baseNodeIndex"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NameRenewed(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "name": args["name"],
        "label": args["label"],
        "cost": args["cost"],
        "expires": args["expires"],
        "baseNodeIndex": args["baseNodeIndex"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NewPriceOracle(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "oracle": args["oracle"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def OwnershipTransferred(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "previousOwner": args["previousOwner"],
        "newOwner": args["newOwner"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def process_event_helper(block_when: datetime.datetime, event: AttributeDict):
    event_dict = {
        'NameRegistered': NameRegistered,
        'NameRenewed': NameRenewed,
        'NewPriceOracle': NewPriceOracle,
        'OwnershipTransferred': OwnershipTransferred,
    }
    method = event_dict.get(event.event)
    if method:
        return method(block_when, event)


class ETHRegistrarControllerProcessEvent(ProcessEventImpl):



    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'NameRegistered': NameRegistered,
            'NameRenewed': NameRenewed,
            'NewPriceOracle': NewPriceOracle,
            'OwnershipTransferred': OwnershipTransferred,
        }
        method = event_dict.get(event.event)
        if method:
            return method(block_when, event)

    def save_data(
            self,
            block_number,
            tx_hash,
            log_index,
            process_event_data: dict,
            event: AttributeDict) -> int:
        """Delete any data since this block was scanned.

        Purges any potential minor reorg data.
        """

        if event.event == 'NameRegistered':
            insert_eth_registrar_controller_event_name_registered(
                block_number,
                tx_hash,
                log_index,
                self.network_id,
                process_event_data['name'],
                '0x' + process_event_data['label'].hex(),
                process_event_data['owner'],
                process_event_data['cost'],
                process_event_data['expires'],
                process_event_data['baseNodeIndex'],
                process_event_data['timestamp'])
        '''
        elif event.event == 'NameRenewed':
            insert_eth_registrar_controller_event_name_renewed(
            block_number,
                tx_hash,
                log_index,
                                                                self.network_id,
                                                                process_event_data['name'],
                                                               '0x' + process_event_data['label'].hex(),
                                                               process_event_data['cost'],
                                                               process_event_data['expires'],
                                                               process_event_data['baseNodeIndex'],
                                                               process_event_data['timestamp'])


        elif event.event == 'OwnershipTransferred':
            insert_eth_registrar_controller_event_ownership_transferred(
            block_number,
                tx_hash,
                log_index,
            self.network_id,
            process_event_data['previousOwner'],
                                                                 process_event_data['newOwner'],
                                                                 process_event_data['timestamp'])
                                                                 '''
