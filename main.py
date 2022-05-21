"""
The following example code is divided into a reusable EventScanner class and then a demo script that:

*fetches all transfer events for RCC token,
*can incrementally run again to check if there are new events,
*handles interruptions (e.g., CTRL+C abort) gracefully,
*writes all Transfer events in a single file JSON database, so that other process can consume them,
*uses the tqdm library for progress bar output in a console,
*only supports HTTPS providers, because JSON-RPC retry logic depends on the implementation details of the underlying protocol,
*disables the standard http_retry_request_middleware because it does not know how to handle the shrinking block range window for eth_getLogs, and
*consumes around 20k JSON-RPC API calls.

The script can be run with: python ./eventscanner.py <your JSON-RPC API URL>.


"""
import logging
import time

from apscheduler.schedulers.blocking import BlockingScheduler
from web3 import Web3
from web3.middleware import geth_poa_middleware

from EventScanner import EventScanner
from database.database import close_database
from ensContractEvent.BaseRegistarContractEvent import BaseRegistarContractEvent
from ensContractEvent.ETHRegistrarControllerContractEvent import ETHRegistrarControllerContractEvent
from ensContractEvent.EnsRegistryContractEvent import EnsRegistryContractEvent
from ensContractEvent.LinearPremiumPriceOracleContractEvent import LinearPremiumPriceOracleContractEvent
from ensContractEvent.PublicResolverContractEvent import PublicResolverContractEvent
from ensContractEvent.ReverseRegistrarContractEvent import ReverseRegistrarContractEvent
from ensContractEvent.SubdomainRegistrarContractEvent import SubdomainRegistrarContractEvent
from eventState.JSONifiedState import JSONifiedState

"""A stateful event scanner for Ethereum-based blockchains using Web3.py.

With the stateful mechanism, you can do one batch scan or incremental scans,
where events are added wherever the scanner left off.
"""

# 当使用web3.py接入采用POA共识的以太坊节点时，可能会出现错误The field extraData is 97 bytes, but should be 32...
# 当使用Ropston网络时没有问题，但是Rinkeby则会出现问题

if __name__ == "__main__":

    # Simple demo that scans all the token transfers of RCC token (11k).
    # The demo supports persistant state by using a JSON file.
    # You will need an Ethereum node for this.
    # Running this script will consume around 20k JSON-RPC calls.
    # With locally running Geth, the script takes 10 minutes.
    # The resulting JSON state file is 2.9 MB.
    from web3.providers.rpc import HTTPProvider

    # We use tqdm library to render a nice progress bar in the console
    # https://pypi.org/project/tqdm/
    from tqdm import tqdm

    # mainnet
    api_url_mainnet = "https://ropsten.infura.io/v3/ec2d05b145c1443c9cca09393955e37c"
    api_url_mainnet_alchemy = "https://eth-mainnet.alchemyapi.io/v2/CD0O0kdHXToHSvaQrPvN5xRAUTRg0e6_"

    # rospten
    api_url_ropsten_infura = "https://ropsten.infura.io/v3/ec2d05b145c1443c9cca09393955e37c"
    api_url_ropsten_alchemy = "https://eth-ropsten.alchemyapi.io/v2/V8EwUsUS0SCE9FtPYCVPRfC3SnRUy5Vz"

    # rinkeby
    api_url_rinkeby_infura = "https://rinkeby.infura.io/v3/ec2d05b145c1443c9cca09393955e37c"
    api_url_rinkeby_alchemy = "https://eth-rinkeby.alchemyapi.io/v2/9IzDixNqpQGzIGQBb-YsQYdcLvhnlCB1"

    # Goerli
    api_url_goerli_infura = "https://eth-goerli.alchemyapi.io/v2/ec2d05b145c1443c9cca09393955e37c"
    api_url_goerli_alchemy = "https://eth-goerli.alchemyapi.io/v2/ot41xp6WbmRmqtDREro6ERragj2X7AGb"


    def run(api_url):
        network_id = 0
        if api_url.find('mainnet') >= 0:
            network_id = 1
        elif api_url.find('ropsten') >= 0:
            network_id = 3
        elif api_url.find('rinkeby') >= 0:
            network_id = 4
        elif api_url.find('rinkeby') >= 0:
            network_id = 4

        # Enable logs to the stdout.
        # DEBUG is very verbose level
        logging.basicConfig(level=logging.INFO)

        provider = HTTPProvider(api_url)

        # Remove the default JSON-RPC retry middleware
        # as it correctly cannot handle eth_getLogs block range
        # throttle down.
        provider.middlewares.clear()

        web3 = Web3(provider)
        if api_url.find('rinkeby') > 0:
            web3.middleware_onion.inject(
                    geth_poa_middleware,
                    layer=0)  # 注入poa中间件

        # Restore/create our persistent state
        state = JSONifiedState()
        state.restore()

        # chain_id: int, web3: Web3, abi: dict, state: EventScannerState,
        # events: List, filters: {}, max_chunk_scan_size: int=10000
        scanner = EventScanner(
                web3=web3,
                state=state,
                ens_contract_events=[EnsRegistryContractEvent(web3,
                                                              network_id),
                                     BaseRegistarContractEvent(web3,
                                                               network_id),
                                     ETHRegistrarControllerContractEvent(web3,
                                                                         network_id),
                                     LinearPremiumPriceOracleContractEvent(web3,
                                                                           network_id),
                                     PublicResolverContractEvent(web3,
                                                                 network_id),
                                     ReverseRegistrarContractEvent(web3,
                                                                   network_id),
                                     SubdomainRegistrarContractEvent(web3,
                                                                     network_id)
                                     ],
                # How many maximum blocks at the time we request from JSON-RPC
                # and we are unlikely to exceed the response size limit of the
                # JSON-RPC server
                max_chunk_scan_size=10000
        )

        # Assume we might have scanned the blocks all the way to the last Ethereum block
        # that mined a few seconds before the previous scan run ended.
        # Because there might have been a minor Etherueum chain reorganisations
        # since the last scan ended, we need to discard
        # the last few blocks from the previous scan results.
        chain_reorg_safety_blocks = 10
        scanner.delete_potentially_forked_block_data(
                state.get_last_scanned_block() - chain_reorg_safety_blocks)

        # Scan from [last block scanned] - [latest ethereum block]
        # Note that our chain reorg safety blocks cannot go negative
        start_block = max(
                state.get_last_scanned_block() -
                chain_reorg_safety_blocks,
                10464000)
        end_block = scanner.get_suggested_scan_end_block()
        blocks_to_scan = end_block - start_block

        print(f"Scanning events from blocks {start_block} - {end_block}")

        if start_block > end_block:
            return

        # Render a progress bar in the console
        start = time.time()
        with tqdm(total=blocks_to_scan) as progress_bar:
            def _update_progress(
                    start,
                    end,
                    current,
                    current_block_timestamp,
                    chunk_size,
                    events_count):
                if current_block_timestamp:
                    formatted_time = current_block_timestamp.strftime(
                            "%d-%m-%Y")
                else:
                    formatted_time = "no block time available"
                progress_bar.set_description(
                        f"Current block: {current} ({formatted_time}), blocks in a scan batch: {chunk_size}, events processed in a batch {events_count}")
                progress_bar.update(chunk_size)

            # Run the scan
            result, total_chunks_scanned = scanner.scan(
                    start_block,
                    end_block,
                    progress_callback=_update_progress)

        state.save()
        duration = time.time() - start
        print(
                f"Scanned total {len(result)} Transfer events, in {duration} seconds, total {total_chunks_scanned} chunk scans performed")


    run(api_url_rinkeby_alchemy)


    def APschedulerMonitor():
        # 创建调度器：BlockingScheduler
        scheduler = BlockingScheduler()

        # 添加任务,时间间隔60S
        scheduler.add_job(run,
                          'interval',
                          seconds=120,
                          id='scan',
                          args=[api_url_rinkeby_alchemy])
        scheduler.start()


    APschedulerMonitor()

    close_database()
