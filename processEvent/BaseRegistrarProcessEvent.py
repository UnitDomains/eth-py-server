import datetime

from web3.datastructures import AttributeDict

from database.BaseRegistar import insert_base_registrar_event_transfer, insert_base_registrar_event_name_registered, \
    update_base_registrar_event_name_renewed
from database.utils import adjust_hex_2_fix_length
from processEvent.ProcessEventImpl import ProcessEventImpl


def Approval(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "owner": args["owner"],
        "approved": args["approved"],
        "tokenId": args["tokenId"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def ApprovalForAll(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "owner": args["owner"],
        "operator": args["operator"],
        "approved": args["approved"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def ControllerAdded(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "controller": args["controller"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def ControllerRemoved(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "controller": args["controller"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NameMigrated(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "id": args["id"],
        "owner": args["owner"],
        "expires": args["expires"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NameRegistered(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "id": args["id"],
        "owner": args["owner"],
        "expires": args["expires"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NameRenewed(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "id": args["id"],
        "expires": args["expires"],
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


def Transfer(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "from": args["from"],
        "to": args["to"],
        "tokenId": args["tokenId"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class BaseRegistarProcessEvent(ProcessEventImpl):
    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'Approval': Approval,
            'ApprovalForAll': ApprovalForAll,
            'ControllerAdded': ControllerAdded,
            'ControllerRemoved': ControllerRemoved,
            'NameMigrated': NameMigrated,
            'NameRegistered': NameRegistered,
            'NameRenewed': NameRenewed,
            'OwnershipTransferred': OwnershipTransferred,
            'Transfer': Transfer
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

        if event.event == 'Transfer':
            insert_base_registrar_event_transfer(
                process_event_data['from'],
                process_event_data['to'],
                adjust_hex_2_fix_length(
                    hex(
                        process_event_data['tokenId'])),
                process_event_data['timestamp'])

        elif event.event == 'NameRenewed':
            update_base_registrar_event_name_renewed(adjust_hex_2_fix_length(hex(
                process_event_data['id'])), process_event_data['expires'], process_event_data['timestamp'])

        elif event.event == 'NameRegistered':
            insert_base_registrar_event_name_registered(
                adjust_hex_2_fix_length(
                    hex(
                        process_event_data['id'])),
                process_event_data['owner'],
                process_event_data['expires'],
                process_event_data['timestamp'])

        elif event.event == 'OwnershipTransferred':
            print(process_event_data['newOwner'])
            '''
            insert_base_registrar_event_name_registered(              
                process_event_data['previousOwner'],
                process_event_data['newOwner'],
                process_event_data['timestamp'])
            '''
