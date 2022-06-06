import datetime

from web3.datastructures import AttributeDict

from database.event.SubdomainRegistrar.DeleteSubdomain import insert_subdomain_registrar_event_delete_subdomain
from database.event.SubdomainRegistrar.NewSubdomainRegistration import \
    insert_subdomain_registrar_event_new_subdomain_registration
from processEvent.ProcessEventImpl import ProcessEventImpl


def DeleteSubdomain(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "node":      args["node"],
        "label":     args["label"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


def NewSubdomainRegistration(
        block_when: datetime.datetime,
        event: AttributeDict) -> dict:
    args = event["args"]
    event_data = {
        "label":     args["label"],
        "subdomain": args["subdomain"],
        "owner":     args["owner"],
        "timestamp": block_when.isoformat(),
    }
    return event_data


class SubdomainRegistrarProcessEvent(ProcessEventImpl):

    def __repr__(self):
        return "SubdomainRegistrarProcessEvent"

    def get_process_event_data(self,
                               block_when: datetime.datetime,
                               event: AttributeDict) -> dict:
        event_dict = {
            'DeleteSubdomain':          DeleteSubdomain,
            'NewSubdomainRegistration': NewSubdomainRegistration
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

        if event.event == 'DeleteSubdomain':
            #  event DeleteSubdomain(bytes32 indexed node, bytes32 indexed label);
            insert_subdomain_registrar_event_delete_subdomain(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['node'].hex(),
                    '0x' + process_event_data['label'].hex(),
                    process_event_data['timestamp'])

        elif event.event == 'NewSubdomainRegistration':
            '''
            event NewSubdomainRegistration(
                bytes32 indexed label,
                string subdomain,
                address indexed owner
            );
            '''

            insert_subdomain_registrar_event_new_subdomain_registration(
                    block_number,
                    tx_hash,
                    log_index,
                    self.network_id,
                    '0x' + process_event_data['label'].hex(),
                    process_event_data['subdomain'],
                    process_event_data['owner'],
                    process_event_data['timestamp'])
