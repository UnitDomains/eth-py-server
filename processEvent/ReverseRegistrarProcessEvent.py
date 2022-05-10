import datetime

from web3.datastructures import AttributeDict

from processEvent.ProcessEventImpl import ProcessEventImpl


def ControllerChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "controller": args["controller"],
        "enabled": args["enabled"],
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


def ReverseClaimed(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "addr": args["addr"],
        "node": args["node"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class ReverseRegistrarProcessEvent(ProcessEventImpl):
    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'ControllerChanged': ControllerChanged,
            'OwnershipTransferred': OwnershipTransferred,
            'ReverseClaimed': ReverseClaimed
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
        if event.event == 'ReverseClaimed':
            # event ReverseClaimed(address indexed addr, bytes32 indexed node);
            pass


