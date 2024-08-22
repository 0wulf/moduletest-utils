#!/usr/bin/env python3
import argparse
import logging
import signal
import sys
import asyncio


from src.network.monitor import Monitor
from src.network.ap import AP
from src.transport.tcp import ConnectionManager
from src.transport.gps import GPSClient
from src.config import NetworkConfig as NC
from src.config import SLEEP_TIME

logger = logging.getLogger(__name__)

def signal_handler(sig, frame):
    logger.info('Exiting...')
    AP.down()
    sys.exit(0)

async def main():
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(
        prog='moduletest-utils',
        description='Tools for analysis of IoT devices probing for 802.11 AP with SSID "moduletest"'
    )
    parser.add_argument('-a', '--access-point', type=str, help='nmcli interface for create the AP, delete the AP or clear the connections', choices=['create', 'delete', 'clear'])
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

    if args.access_point is not None:
        if args.access_point == 'create':
            AP.create(interface)
            AP.down()
        elif args.access_point == 'delete':
            AP.delete()
        elif args.access_point == 'clear':
            AP.clear(interface)
        sys.exit(0)
    AP.up()

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