import tinytuya
import logging
import asyncio

from src.config import MessageConfig as MC

logger = logging.getLogger(__name__)


class ConnectionManager:
    def __init__(self):
        self.ipv4s = []

    def _get_message(self):
        msg = tinytuya.TuyaMessage(0, 0x0a, 0, MC.DUMMY_PAYLOAD, 0, True, tinytuya.PREFIX_55AA_VALUE, False) # commands 0x09 0x0a 0x0b generate responses
        msg = tinytuya.pack_message(msg, hmac_key=None)
        return msg

    async def _single_connect(self, ipv4):
        logger.debug(f'Starting connection for {ipv4}')
        message = self._get_message()
        try:
            reader, writer = await asyncio.open_connection(ipv4, 6668)
            writer.write(message)
            logger.debug(f'Sent message to {ipv4}: {message}')
            await writer.drain()
            rcv = await reader.read(1024)
            msg = tinytuya.unpack_message(rcv, hmac_key=None)
            logger.debug(f'Received message from {ipv4}: {msg}')
        except Exception as e:
            logger.debug(f'Failed to send message to {ipv4}: {e}')


    async def connect(self):
        await asyncio.gather(*[self._single_connect(ipv4) for ipv4 in self.ipv4s])

    def update_ipv4s(self, ipv4s):
        self.ipv4s = ipv4s