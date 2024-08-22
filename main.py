#!/usr/bin/env python3
import argparse
import logging
import asyncio


from src.network.monitor import Monitor
from src.network.ap import AP
from src.transport.tcp import ConnectionManager
from src.transport.gps import GPSClient
from src.config import NetworkConfig as NC
from src.config import SLEEP_TIME

logger = logging.getLogger(__name__)


async def main():
    parser = argparse.ArgumentParser(
        prog='moduletest-utils',
        description='Tools for analysis of IoT devices probing for 802.11 AP with SSID "moduletest"'
    )
    parser.add_argument('-c', '--connect', action='store_true', help='Connect to the devices through port 6668/tcp and send dummy payload')
    parser.add_argument('-g', '--gps', action='store_true', help='Connect to tcp gps server')
    parser.add_argument('-i', '--interface', type=str, help='Interface to use')
    parser.add_argument('-v', '--verbose', action='store_true', help='Debug level logging')
    args = parser.parse_args()

    level =  logging.INFO
    if args.verbose:
        level = logging.DEBUG
    logging.basicConfig(level=level)

    interface = NC.INTERFACE
    if args.interface:
        interface = args.interface
    logger.info(f'Using interface: {interface}')

    AP(interface)
    mon = Monitor(interface)
    conman = ConnectionManager()
    gps_client = GPSClient()
    
    while True:
        min_time = asyncio.sleep(SLEEP_TIME)

        if args.gps:
            gps_client.get_coords()
        mon.get_signal()

        if args.connect:
            ipv4s = mon.scan()
            conman.update_ipv4s(ipv4s)
            await conman.connect()

        await min_time
        

if __name__ == '__main__':
    asyncio.run(main())