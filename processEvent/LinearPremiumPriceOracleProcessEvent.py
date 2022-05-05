import datetime

from web3.datastructures import AttributeDict

from processEvent.ProcessEventImpl import ProcessEventImpl


def OracleChanged(block_when: datetime.datetime, event: AttributeDict) -> dict:
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


def PaymentTypeChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "_paymentType": args["_paymentType"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def RegisterPriceChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "prices": args["prices"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def RentPriceChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "prices": args["prices"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class LinearPremiumPriceOracleProcessEvent(ProcessEventImpl):
    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'OracleChanged': OracleChanged,
            'OwnershipTransferred': OwnershipTransferred,
            'PaymentTypeChanged': PaymentTypeChanged,
            'RegisterPriceChanged': RegisterPriceChanged,
            'RentPriceChanged': RentPriceChanged
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
