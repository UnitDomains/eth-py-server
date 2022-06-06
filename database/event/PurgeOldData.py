from database.event.BaseRegistar.Approval import delete_base_registrar_event_approval_after_block
from database.event.BaseRegistar.ApprovalForAll import delete_base_registrar_event_approval_for_all_after_block
from database.event.BaseRegistar.ControllerAdded import delete_base_registrar_event_controller_added_after_block
from database.event.BaseRegistar.ControllerRemoved import delete_base_registrar_event_controller_removed_after_block
from database.event.BaseRegistar.NameMigrated import delete_base_registrar_event_name_migrated_after_block
from database.event.BaseRegistar.NameRegistered import delete_base_registrar_event_name_registered_after_block
from database.event.BaseRegistar.NameRenewed import delete_base_registrar_event_name_renewed_after_block
from database.event.BaseRegistar.NewBaseNode import delete_base_registrar_event_new_basenode_after_block
from database.event.BaseRegistar.OwnershipTransferred import \
    delete_base_registrar_event_ownership_transferred_after_block
from database.event.BaseRegistar.Transfer import delete_base_registrar_event_transfer_after_block
from database.event.EnsRegistry.ApprovalForAll import delete_ens_registry_event_approval_for_all_after_block
from database.event.EnsRegistry.NewOwner import delete_ens_registry_event_new_owner_after_block
from database.event.EnsRegistry.NewResolver import delete_ens_registry_event_new_resolver_after_block
from database.event.EnsRegistry.NewTLDOwner import delete_ens_registry_event_new_tld_owner_after_block
from database.event.EnsRegistry.NewTTL import delete_ens_registry_event_new_ttl_after_block
from database.event.EnsRegistry.Transfer import delete_ens_registry_event_transfer_after_block
from database.event.EthRegistrarController.NameRegistered import \
    delete_eth_registrar_controller_event_name_registered_after_block
from database.event.EthRegistrarController.NameRenewed import \
    delete_eth_registrar_controller_event_name_renewed_after_block
from database.event.EthRegistrarController.NewPriceOracle import \
    delete_eth_registrar_controller_event_new_price_oracle_after_block
from database.event.EthRegistrarController.OwnershipTransferred import \
    delete_eth_registrar_controller_event_ownership_transferred_after_block
from database.event.PriceOracle.OracleChanged import delete_price_oracle_event_oracle_changed_after_block
from database.event.PriceOracle.OwnershipTransferred import delete_price_oracle_event_ownership_transferred_after_block
from database.event.PriceOracle.PaymentTypeChanged import delete_price_oracle_event_payment_type_changed_after_block
from database.event.PriceOracle.RegisterPriceChanged import delete_price_oracle_event_register_price_changed_after_block
from database.event.PriceOracle.RentPriceChanged import delete_price_oracle_event_rent_price_changed_after_block
from database.event.PublicResolver.ABIChanged import delete_public_resolver_event_abi_changed_after_block
from database.event.PublicResolver.AddrChanged import delete_public_resolver_event_addr_changed_after_block
from database.event.PublicResolver.AddressChanged import delete_public_resolver_event_address_changed_after_block
from database.event.PublicResolver.ApprovalForAll import delete_public_resolver_event_approval_for_all_after_block
from database.event.PublicResolver.ContenthashChanged import \
    delete_public_resolver_event_content_hash_changed_after_block
from database.event.PublicResolver.DNSRecordChanged import delete_public_resolver_event_DNS_record_changed_after_block
from database.event.PublicResolver.DNSRecordDeleted import delete_public_resolver_event_DNS_record_deleted_after_block
from database.event.PublicResolver.DNSZoneCleared import delete_public_resolver_event_DNS_zone_cleared_after_block
from database.event.PublicResolver.DNSZonehashChanged import \
    delete_public_resolver_event_DNS_zone_hash_changed_after_block
from database.event.PublicResolver.InterfaceChanged import delete_public_resolver_event_interface_changed_after_block
from database.event.PublicResolver.NameChanged import delete_public_resolver_event_name_changed_after_block
from database.event.PublicResolver.PubkeyChanged import delete_public_resolver_event_pubkey_changed_after_block
from database.event.PublicResolver.TextChanged import delete_public_resolver_event_text_changed_after_block
from database.event.ReverseRegistrar.ControllerChanged import \
    delete_reverse_registrar_event_controller_changed_after_block
from database.event.ReverseRegistrar.OwnershipTransferred import \
    delete_reverse_registrar_event_ownership_transferred_after_block
from database.event.ReverseRegistrar.ReverseClaimed import delete_reverse_registrar_event_reverse_claimed_after_block
from database.event.SubdomainRegistrar.DeleteSubdomain import \
    delete_subdomain_registrar_event_delete_subdomain_after_block
from database.event.SubdomainRegistrar.NewSubdomainRegistration import \
    delete_subdomain_registrar_event_new_subdomain_registration_after_block


def PurgeOldData(network_id,
                 block_number):
    # base_registrar_event
    delete_base_registrar_event_approval_after_block(network_id,
                                                     block_number)
    delete_base_registrar_event_approval_for_all_after_block(network_id,
                                                             block_number)
    delete_base_registrar_event_controller_added_after_block(network_id,
                                                             block_number)
    delete_base_registrar_event_controller_removed_after_block(network_id,
                                                               block_number)
    delete_base_registrar_event_name_migrated_after_block(network_id,
                                                          block_number)
    delete_base_registrar_event_name_registered_after_block(network_id,
                                                            block_number)
    delete_base_registrar_event_name_renewed_after_block(network_id,
                                                         block_number)
    delete_base_registrar_event_new_basenode_after_block(network_id,
                                                         block_number)
    delete_base_registrar_event_ownership_transferred_after_block(network_id,
                                                                  block_number)
    delete_base_registrar_event_transfer_after_block(network_id,
                                                     block_number)

    # ens_registry_event
    delete_ens_registry_event_approval_for_all_after_block(network_id,
                                                           block_number)
    delete_ens_registry_event_new_owner_after_block(network_id,
                                                    block_number)
    delete_ens_registry_event_new_resolver_after_block(network_id,
                                                       block_number)
    delete_ens_registry_event_new_tld_owner_after_block(network_id,
                                                        block_number)
    delete_ens_registry_event_new_ttl_after_block(network_id,
                                                  block_number)
    delete_ens_registry_event_transfer_after_block(network_id,
                                                   block_number)

    # eth_registrar_controller_event
    delete_eth_registrar_controller_event_name_registered_after_block(network_id,
                                                                      block_number)
    delete_eth_registrar_controller_event_name_renewed_after_block(network_id,
                                                                   block_number)
    delete_eth_registrar_controller_event_new_price_oracle_after_block(network_id,
                                                                       block_number)
    delete_eth_registrar_controller_event_ownership_transferred_after_block(network_id,
                                                                            block_number)

    # price_oracle_event
    delete_price_oracle_event_oracle_changed_after_block(network_id,
                                                         block_number)
    delete_price_oracle_event_ownership_transferred_after_block(network_id,
                                                                block_number)
    delete_price_oracle_event_payment_type_changed_after_block(network_id,
                                                               block_number)
    delete_price_oracle_event_register_price_changed_after_block(network_id,
                                                                 block_number)
    delete_price_oracle_event_rent_price_changed_after_block(network_id,
                                                             block_number)

    # public_resolver_event
    delete_public_resolver_event_abi_changed_after_block(network_id,
                                                         block_number)
    delete_public_resolver_event_addr_changed_after_block(network_id,
                                                          block_number)
    delete_public_resolver_event_address_changed_after_block(network_id,
                                                             block_number)
    delete_public_resolver_event_approval_for_all_after_block(network_id,
                                                              block_number)
    delete_public_resolver_event_content_hash_changed_after_block(network_id,
                                                                  block_number)
    delete_public_resolver_event_DNS_record_changed_after_block(network_id,
                                                                block_number)
    delete_public_resolver_event_DNS_record_deleted_after_block(network_id,
                                                                block_number)
    delete_public_resolver_event_DNS_zone_cleared_after_block(network_id,
                                                              block_number)
    delete_public_resolver_event_DNS_zone_hash_changed_after_block(network_id,
                                                                   block_number)
    delete_public_resolver_event_interface_changed_after_block(network_id,
                                                               block_number)
    delete_public_resolver_event_name_changed_after_block(network_id,
                                                          block_number)
    delete_public_resolver_event_pubkey_changed_after_block(network_id,
                                                            block_number)
    delete_public_resolver_event_text_changed_after_block(network_id,
                                                          block_number)

    # reverse_registrar_event
    delete_reverse_registrar_event_controller_changed_after_block(network_id,
                                                                  block_number)
    delete_reverse_registrar_event_ownership_transferred_after_block(network_id,
                                                                     block_number)
    delete_reverse_registrar_event_reverse_claimed_after_block(network_id,
                                                               block_number)

    # subdomain_registrar_event
    delete_subdomain_registrar_event_delete_subdomain_after_block(network_id,
                                                                  block_number)
    delete_subdomain_registrar_event_new_subdomain_registration_after_block(network_id,
                                                                            block_number)
