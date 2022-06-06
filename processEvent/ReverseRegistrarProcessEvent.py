import datetime

from web3.datastructures import AttributeDict

from database.event.ReverseRegistrar.ControllerChanged import insert_reverse_registrar_event_controller_changed
from database.event.ReverseRegistrar.OwnershipTransferred import insert_reverse_registrar_event_ownership_transferred
from database.event.ReverseRegistrar.ReverseClaimed import insert_reverse_registrar_event_reverse_claimed
from processEvent.ProcessEventImpl import ProcessEventImpl


def ControllerChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "controller": args["controller"],
        "enabled":    args["enabled"],
        "timestamp":  block_when.isoformat(),
    }
    return event_data


def OwnershipTransferred(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "previousOwner": args["previousOwner"],
        "newOwner":      args["newOwner"],
        "timestamp":     block_when.isoformat(),
    }
    return event_data


def ReverseClaimed(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "addr":      args["addr"],
        "node":      args["node"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class ReverseRegistrarProcessEvent(ProcessEventImpl):

    def __repr__(self):
        return "ReverseRegistrarProcessEvent"

    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'ControllerChanged':    ControllerChanged,
            'OwnershipTransferred': OwnershipTransferred,
            'ReverseClaimed':       ReverseClaimed
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

        if event.event == 'ControllerChanged':
            insert_reverse_registrar_event_controller_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['controller'],
                    process_event_data['enabled'],
                    process_event_data['timestamp'])
        elif event.event == 'OwnershipTransferred':
            insert_reverse_registrar_event_ownership_transferred(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['previousOwner'],
                    process_event_data['newOwner'],
                    process_event_data['timestamp'])
        elif event.event == 'ReverseClaimed':
            # event ReverseClaimed(address indexed addr, bytes32 indexed node);
            insert_reverse_registrar_event_reverse_claimed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['addr'],
                    '0x' + process_event_data['node'].hex(),
                    process_event_data['timestamp'])
