import datetime

from web3.datastructures import AttributeDict

from database.event.EnsRegistry.ApprovalForAll import insert_ens_registry_event_approval_for_all
from database.event.EnsRegistry.NewOwner import insert_ens_registry_event_new_owner
from database.event.EnsRegistry.NewResolver import insert_ens_registry_event_new_resolver
from database.event.EnsRegistry.NewTLDOwner import insert_ens_registry_event_new_tld_owner
from database.event.EnsRegistry.NewTTL import insert_ens_registry_event_new_ttl
from database.event.EnsRegistry.Transfer import insert_ens_registry_event_transfer
from processEvent.ProcessEventImpl import ProcessEventImpl


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


def NewOwner(block_when: datetime.datetime,
             event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "label":     args["label"],
        "owner":     args["owner"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NewTLDOwner(block_when: datetime.datetime,
                event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "nodelabel": args["nodelabel"],
        "owner":     args["owner"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NewResolver(block_when: datetime.datetime,
                event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "resolver":  args["resolver"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NewTTL(block_when: datetime.datetime,
           event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "ttl":       args["ttl"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def Transfer(block_when: datetime.datetime,
             event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "owner":     args["owner"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class EnsRegistryProcessEvent(ProcessEventImpl):

    def __repr__(self):
        return "EnsRegistryProcessEvent"

    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'ApprovalForAll': ApprovalForAll,
            'NewOwner':       NewOwner,
            "NewTLDOwner":    NewTLDOwner,
            'NewResolver':    NewResolver,
            'NewTTL':         NewTTL,
            'Transfer':       Transfer
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
        """将数据保存到数据库中
        """

        if event.event == 'NewOwner':
            insert_ens_registry_event_new_owner(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    '0x' + process_event_data['label'].hex(),
                    process_event_data['owner'],
                    process_event_data['timestamp'])
        if event.event == 'NewTLDOwner':
            insert_ens_registry_event_new_tld_owner(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    '0x' + process_event_data['nodelabel'].hex(),
                    process_event_data['owner'],
                    process_event_data['timestamp'])

        elif event.event == 'Transfer':
            insert_ens_registry_event_transfer(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['owner'],
                    process_event_data['timestamp'])
        elif event.event == 'ApprovalForAll':
            insert_ens_registry_event_approval_for_all(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['owner'],
                    process_event_data['operator'],
                    process_event_data['approved'],
                    process_event_data['timestamp'])
        elif event.event == 'NewResolver':
            insert_ens_registry_event_new_resolver(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['resolver'],
                    process_event_data['timestamp'])

        elif event.event == 'NewTTL':
            insert_ens_registry_event_new_ttl(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['ttl'],
                    process_event_data['timestamp'])
