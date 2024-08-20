import argparse
import threading
import logging


from src.network.signal import signal_mon
from src.network.ap import AP
from src.network.recon import recon
from src.transport import connect_loop
from src.config import NetworkConfig as NC

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
        prog='moduletest-utils',
        description='Tools for analysis of IoT devices probing for 802.11 AP with SSID "moduletest"'
    )
    parser.add_argument('-a', '--access-point', type=str, help='nmcli interface for create, up, down, delete, or show the access point')
    parser.add_argument('-c', '--connect', action='store_true', help='Connect to the devices through port 6668 and send payload')
    parser.add_argument('-i', '--interface', type=str, help='Interface to use')
    parser.add_argument('-r', '--recon', action='store_true', help='Recon the network for IPv4s')
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

    ipv4s = []
    if args.recon == True:
        ipv4s = recon(interface)
    else:
        ipv4s = NC.IPv4s

    threads = []
    if args.connect == True:
        for ipv4 in ipv4s:
            t = threading.Thread(target=connect_loop, args=(ipv4,))
            threads.append(t)

        
    threads.append(threading.Thread(target=signal_mon, args=(interface,)))
    for t in threads:
        t.start()




if __name__ == '__main__':
    main()