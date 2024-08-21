import argparse
import threading
import logging

from time import sleep


from src.network.signal import signal_mon
from src.network.ap import AP
from src.network.scan import scan
from src.transport import connect
from src.config import NetworkConfig as NC
from src.config import SLEEP_TIME

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
        prog='moduletest-utils',
        description='Tools for analysis of IoT devices probing for 802.11 AP with SSID "moduletest"'
    )
    parser.add_argument('-a', '--access-point', type=str, help='nmcli interface for create, up, down, delete, or show the access point')
    parser.add_argument('-c', '--connect', action='store_true', help='Connect to the devices through port 6668/tcp and send payload')
    parser.add_argument('-i', '--interface', type=str, help='Interface to use')
    parser.add_argument('-v', '--verbose', action='store_true', help='Debug level logging')
    parser.add_argument('-m', '--monitor', action='store_true', help='Monitor the signal of the devices')
    parser.add_argument('-g', '--gps', action='store_true', help='Connect to tcp gps server - WIP')
    parser.add_argument('-d', '--detect-cleartext', action='store_true', help='Detect cleartext communication - WIP')
    args = parser.parse_args()

    level =  logging.INFO
    if args.verbose:
        level = logging.DEBUG
    logging.basicConfig(level=level)

    interface = NC.INTERFACE
    if args.interface:
        interface = args.interface
    logger.info(f'Using interface: {interface}')

    if args.access_point == 'create':
        AP.create(interface)
        exit()
    elif args.access_point == 'up':
        AP.up()
        exit()
    elif args.access_point == 'down':
        AP.down()
        exit()
    elif args.access_point == 'delete':
        AP.delete()
        exit()
    elif args.access_point == 'show':
        AP.show()
        exit()

    # Loop for avoiding shared data and locks
    while True:
        ipv4s = scan(interface)

        threads = []
        if args.connect == True:
            for ipv4 in ipv4s:
                t = threading.Thread(target=connect, args=(ipv4,))
                threads.append(t)
        if args.monitor == True:         
            threads.append(threading.Thread(target=signal_mon, args=(interface,)))
        for t in threads:
            t.start()
        sleep(SLEEP_TIME)
        for t in threads:
            t.join()


if __name__ == '__main__':
    main()