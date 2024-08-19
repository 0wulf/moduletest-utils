import tinytuya
import socket
import logging

from time import sleep

from src.config import MessageConfig as MC

logger = logging.getLogger(__name__)

def get_message(payload: bytes):
    msg = tinytuya.TuyaMessage(0, tinytuya.DP_QUERY, 0, payload, 0, True, tinytuya.PREFIX_55AA_VALUE, False)
    msg = tinytuya.pack_message(msg,hmac_key=None)
    return msg

def send_message(message, ipv4):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout( 4 )
        sock.connect((ipv4, 6668))
        sock.send(message)
        logger.debug(f'Sent message to {ipv4}: {message}')
        rcv = sock.recv(1024)
        logger.debug(f'Received message from {ipv4}: {rcv}')
    except Exception as e:
        logger.error(f'Failed to send message to {ipv4}: {e}')

def connect_loop(ipv4):
    logger.info(f'Starting connect_loop for {ipv4}')
    while True:
        message = get_message(MC.PAYLOAD)
        send_message(message, ipv4)
        sleep(1)