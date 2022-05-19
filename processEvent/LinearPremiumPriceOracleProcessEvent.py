import datetime

from web3.datastructures import AttributeDict

from database.event.PriceOracle import insert_price_oracle_event_oracle_changed, \
    insert_price_oracle_event_ownership_transferred, insert_price_oracle_event_payment_type_changed, \
    insert_price_oracle_event_register_price_changed, insert_price_oracle_event_rent_price_changed
from processEvent.ProcessEventImpl import ProcessEventImpl


def OracleChanged(block_when: datetime.datetime,
                  event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "oracle":    args["oracle"],
        "timestamp": block_when.isoformat(),
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


def PaymentTypeChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "_paymentType": args["_paymentType"],
        "timestamp":    block_when.isoformat(),
    }
    return event_data


def RegisterPriceChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "prices":    args["prices"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def RentPriceChanged(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "prices":    args["prices"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class LinearPremiumPriceOracleProcessEvent(ProcessEventImpl):

    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'OracleChanged':        OracleChanged,
            'OwnershipTransferred': OwnershipTransferred,
            'PaymentTypeChanged':   PaymentTypeChanged,
            'RegisterPriceChanged': RegisterPriceChanged,
            'RentPriceChanged':     RentPriceChanged
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
        if event.event == 'OracleChanged':
            # event OracleChanged(address oracle);
            insert_price_oracle_event_oracle_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['oracle'],
                    process_event_data['timestamp'])

        elif event.event == 'OwnershipTransferred':
            insert_price_oracle_event_ownership_transferred(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['previousOwner'],
                    process_event_data['newOwner'],
                    process_event_data['timestamp'])
        elif event.event == 'PaymentTypeChanged':
            insert_price_oracle_event_payment_type_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['_paymentType'],
                    process_event_data['timestamp'])
        elif event.event == 'RegisterPriceChanged':
            insert_price_oracle_event_register_price_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['prices'],
                    process_event_data['timestamp'])
        elif event.event == 'RentPriceChanged':
            insert_price_oracle_event_rent_price_changed(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    process_event_data['prices'],
                    process_event_data['timestamp'])
