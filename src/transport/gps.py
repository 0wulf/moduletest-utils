import socket
import logging
import time

from pynmeagps.nmeareader import NMEAReader

from src.config import GPSConfig as GC

logger = logging.getLogger(__name__)

class GPSClient:
  def __init__(self):
    self.ipv4 = GC.HOST
    self.port = GC.PORT

  def get_coords(self): # refactor
    try:
      logger.info(f'Connecting to GPS server at {self.ipv4}:{self.port}...')
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
        stream.connect((self.ipv4, self.port))
        nmr = NMEAReader(stream, nmeaonly=True) 
        for _, parsed_data in nmr:
          if parsed_data.msgID == 'RMC':
            logger.info([parsed_data.lat, parsed_data.lon])
    except ConnectionRefusedError as e:
      logger.error(f'Connection refused: {e}')