import datetime

from web3.datastructures import AttributeDict

from database.PublicResolver import insert_public_resolver_event_addr_changed, insert_public_resolver_event_name_changed
from processEvent.ProcessEventImpl import ProcessEventImpl


def ABIChanged(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "contentType": args["contentType"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def AddrChanged(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "addr": args["addr"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def AddressChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "coinType": args["coinType"],
        "newAddress": args["newAddress"],
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


def ContenthashChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "hash": args["hash"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSRecordChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "name": args["name"],
        "resource": args["resource"],
        "record": args["record"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSRecordDeleted(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "name": args["name"],
        "resource": args["resource"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSZoneCleared(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSZonehashChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "lastzonehash": args["lastzonehash"],
        "zonehash": args["zonehash"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def InterfaceChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "interfaceID": args["interfaceID"],
        "implementer": args["implementer"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NameChanged(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "name": args["name"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def PubkeyChanged(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "x": args["x"],
        "y": args["y"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def TextChanged(block_when: datetime.datetime, event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node": args["node"],
        "indexedKey": args["indexedKey"],
        "key": args["key"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class PublicResolverProcessEvent(ProcessEventImpl):
    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'ABIChanged': ABIChanged,
            'AddrChanged': AddrChanged,
            'AddressChanged': AddressChanged,
            'ApprovalForAll': ApprovalForAll,
            'ContenthashChanged': ContenthashChanged,
            'DNSRecordChanged': DNSRecordChanged,
            'DNSRecordDeleted': DNSRecordDeleted,
            'DNSZoneCleared': DNSZoneCleared,
            'DNSZonehashChanged': DNSZonehashChanged,
            'InterfaceChanged': InterfaceChanged,
            'NameChanged': NameChanged,
            'PubkeyChanged': PubkeyChanged,
            'TextChanged': TextChanged
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
        if event.event == 'AddrChanged':
            # event AddrChanged(bytes32 indexed node, address a);
            insert_public_resolver_event_addr_changed(
                '0x' + process_event_data['node'].hex(),
                process_event_data['addr'],
                process_event_data['timestamp'])

        elif event.event == 'NameChanged':
            # event NameChanged(bytes32 indexed node, string name);
            insert_public_resolver_event_name_changed(
                '0x' + process_event_data['node'].hex(),
                process_event_data['name'],
                process_event_data['timestamp'])
