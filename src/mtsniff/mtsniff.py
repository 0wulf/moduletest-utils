#!/usr/bin/env python3
import logging
import asyncio
import datetime
import subprocess


from src.mtsniff.network.monitor import Monitor
from src.mtsniff.network.ap import AP
from src.mtsniff.transport.tcp import ConnectionManager
from src.mtsniff.transport.gps import GPSClient
from src.mtsniff.config import NetworkConfig as NC
from src.mtsniff.config import SLEEP_TIME

logger = logging.getLogger(__name__)


async def main(args):
    if args.web:
        logger.info('Starting web server')
        subprocess.run(['python3', 'src/mtsniff/manage.py', 'runserver', '0.0.0.0:8000'])
        return
    
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    interface = NC.INTERFACE
    if args.interface:
        interface = args.interface
    logger.info(f'Using interface: {interface}')

    AP(interface)
    mon = Monitor(interface)
    conman = ConnectionManager()
    gps_client = GPSClient()
    
    while True:
        wg = [asyncio.sleep(SLEEP_TIME)]

        if args.connect:
            ipv4s = mon.scan()
            conman.update_ipv4s(ipv4s)
            wg.append(conman.connect()) # timeout?

        signal = mon.get_signal()
        coords = []
        if args.gps:
            coords = gps_client.get_coords()
            if args.output:
              with open(args.output, 'a') as f:
                  for dev in signal:
                      now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                      f.write(f'{now},{dev[0]},{dev[1]},{dev[2]},{coords[0]},{coords[1]}\n')

        logger.info(f'Signal: {signal} dBm, Coords: {coords}')

        await asyncio.gather(*wg)