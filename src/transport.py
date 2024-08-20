import tinytuya
import socket
import logging


from src.config import MessageConfig as MC

logger = logging.getLogger(__name__)

def get_message(payload: bytes):
    msg = tinytuya.TuyaMessage(0, 0x0b, 0, payload, 0, True, tinytuya.PREFIX_55AA_VALUE, False) # 0x09 0x0a 0x0b
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
        msg = tinytuya.unpack_message(rcv, hmac_key=None)
        logger.debug(f'Received message from {ipv4}: {msg}')
    except Exception as e:
        logger.error(f'Failed to send message to {ipv4}: {e}')

def connect(ipv4):
    logger.info(f'Starting connection for {ipv4}')
    message = get_message(MC.DUMMY_PAYLOAD)
    send_message(message, ipv4)