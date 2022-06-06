import datetime

from web3.datastructures import AttributeDict

from database.event.PublicResolver.ABIChanged import insert_public_resolver_event_abi_changed
from database.event.PublicResolver.AddrChanged import insert_public_resolver_event_addr_changed
from database.event.PublicResolver.AddressChanged import insert_public_resolver_event_address_changed
from database.event.PublicResolver.ApprovalForAll import insert_public_resolver_event_approval_for_all
from database.event.PublicResolver.ContenthashChanged import insert_public_resolver_event_content_hash_changed
from database.event.PublicResolver.DNSRecordChanged import insert_public_resolver_event_DNS_record_changed
from database.event.PublicResolver.DNSRecordDeleted import insert_public_resolver_event_DNS_record_deleted
from database.event.PublicResolver.DNSZoneCleared import insert_public_resolver_event_DNS_zone_cleared
from database.event.PublicResolver.DNSZonehashChanged import insert_public_resolver_event_DNS_zone_hash_changed
from database.event.PublicResolver.InterfaceChanged import insert_public_resolver_event_interface_changed
from database.event.PublicResolver.NameChanged import insert_public_resolver_event_name_changed
from database.event.PublicResolver.PubkeyChanged import insert_public_resolver_event_pubkey_changed
from database.event.PublicResolver.TextChanged import insert_public_resolver_event_text_changed
from processEvent.ProcessEventImpl import ProcessEventImpl


def ABIChanged(block_when: datetime.datetime,
               event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":        args["node"],
        "contentType": args["contentType"],
        "timestamp":   block_when.isoformat(),
    }
    return event_data


def AddrChanged(block_when: datetime.datetime,
                event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "addr":      args["addr"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def AddressChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":       args["node"],
        "coinType":   args["coinType"],
        "newAddress": args["newAddress"],
        "timestamp":  block_when.isoformat(),
    }
    return event_data


def ApprovalForAll(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "owner":     args["owner"],
        "operator":  args["operator"],
        "approved":  args["approved"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def ContenthashChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "hash":      args["hash"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSRecordChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "name":      args["name"],
        "resource":  args["resource"],
        "record":    args["record"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSRecordDeleted(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "name":      args["name"],
        "resource":  args["resource"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSZoneCleared(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def DNSZonehashChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":         args["node"],
        "lastzonehash": args["lastzonehash"],
        "zonehash":     args["zonehash"],
        "timestamp":    block_when.isoformat(),
    }
    return event_data


def InterfaceChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":        args["node"],
        "interfaceID": args["interfaceID"],
        "implementer": args["implementer"],
        "timestamp":   block_when.isoformat(),
    }
    return event_data


def NameChanged(block_when: datetime.datetime,
                event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "name":      args["name"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def PubkeyChanged(block_when: datetime.datetime,
                  event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "x":         args["x"],
        "y":         args["y"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def TextChanged(block_when: datetime.datetime,
                event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":       args["node"],
        "indexedKey": args["indexedKey"],
        "key":        args["key"],
        "value":      args["value"],
        "timestamp":  block_when.isoformat(),
    }
    return event_data


class PublicResolverProcessEvent(ProcessEventImpl):

    def __repr__(self):
        return "PublicResolverProcessEvent"

    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'ABIChanged':         ABIChanged,
            'AddrChanged':        AddrChanged,
            'AddressChanged':     AddressChanged,
            'ApprovalForAll':     ApprovalForAll,
            'ContenthashChanged': ContenthashChanged,
            'DNSRecordChanged':   DNSRecordChanged,
            'DNSRecordDeleted':   DNSRecordDeleted,
            'DNSZoneCleared':     DNSZoneCleared,
            'DNSZonehashChanged': DNSZonehashChanged,
            'InterfaceChanged':   InterfaceChanged,
            'NameChanged':        NameChanged,
            'PubkeyChanged':      PubkeyChanged,
            'TextChanged':        TextChanged
        }
        method = event_dict.get(event.event)
        if method:
            return method(block_when,
                          event)

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
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['addr'],
                    process_event_data['timestamp'])

        elif event.event == 'NameChanged':
            # event NameChanged(bytes32 indexed node, string name);
            insert_public_resolver_event_name_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['name'],
                    process_event_data['timestamp'])
        elif event.event == 'ABIChanged':
            insert_public_resolver_event_abi_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['contentType'],
                    process_event_data['timestamp'])
        elif event.event == 'AddressChanged':
            insert_public_resolver_event_address_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['newAddress'],
                    process_event_data['coinType'],
                    process_event_data['timestamp'])
        elif event.event == 'ApprovalForAll':
            insert_public_resolver_event_approval_for_all(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['owner'],
                    process_event_data['operator'],
                    process_event_data['approved'],
                    process_event_data['timestamp'])
        elif event.event == 'ContenthashChanged':
            insert_public_resolver_event_content_hash_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['hash'],
                    process_event_data['timestamp'])
        elif event.event == 'DNSRecordChanged':
            insert_public_resolver_event_DNS_record_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['name'],
                    process_event_data['resource'],
                    process_event_data['record'],
                    process_event_data['timestamp'])
        elif event.event == 'DNSRecordDeleted':
            insert_public_resolver_event_DNS_record_deleted(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['name'],
                    process_event_data['resource'],
                    process_event_data['timestamp'])
        elif event.event == 'DNSZoneCleared':
            insert_public_resolver_event_DNS_zone_cleared(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['timestamp'])
        elif event.event == 'DNSZonehashChanged':
            insert_public_resolver_event_DNS_zone_hash_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['last_zone_hash'],
                    process_event_data['zone_hash'],
                    process_event_data['timestamp'])
        elif event.event == 'InterfaceChanged':
            insert_public_resolver_event_interface_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['interfaceID'],
                    process_event_data['implementer'],
                    process_event_data['timestamp'])
        elif event.event == 'TextChanged':
            insert_public_resolver_event_text_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['indexedKey'],
                    process_event_data['key'],
                    process_event_data['value'],
                    process_event_data['timestamp'])
        elif event.event == 'PubkeyChanged':
            insert_public_resolver_event_pubkey_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['x'],
                    process_event_data['y'],
                    process_event_data['timestamp'])
