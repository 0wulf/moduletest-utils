#!/usr/bin/env python3
import argparse
import logging
import asyncio


from src.mtsniff import mtsniff


logger = logging.getLogger(__name__)


def mtsniff_args(subparsers):
    subparser = subparsers.add_parser('mtsniff', help='Monitor for devices probing for 802.11 AP with SSID "moduletest"')
    subparser.add_argument('-c', '--connect', action='store_true', help='Connect to the devices through port 6668/tcp and send dummy payload')
    subparser.add_argument('-g', '--gps', action='store_true', help='Connect to tcp gps server')
    subparser.add_argument('-i', '--interface', type=str, help='Interface to use')
    subparser.add_argument('-v', '--verbose', action='store_true', help='Debug level logging')
    subparser.add_argument('-o', '--output', type=str, help='Append to csv file. -g must be set')

async def main():
    parser = argparse.ArgumentParser(
        prog='moduletest-utils',
        description='Tools for analysis of IoT devices probing for 802.11 AP with SSID "moduletest"'
    )
    subparsers = parser.add_subparsers(dest='tool', required=True, help='Tool to run from: mtsniff')

    mtsniff_args(subparsers)

    args = parser.parse_args()

    if args.tool == 'mtsniff':
        await mtsniff.main(args)
            

if __name__ == '__main__':
    asyncio.run(main())