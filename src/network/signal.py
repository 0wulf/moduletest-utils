import subprocess
import logging
from time import sleep

logger = logging.getLogger(__name__)

def signal_mon(iface):
  while True:
    bin = subprocess.check_output([f'iw dev {iface} station dump'], shell=True)
    string = bin.decode('utf-8')
    lines = string.split('\n')
    devs = [['MAC', 'Signal', 'Avg Signal']]
    for line in lines:
      if 'Station' in line:
        devs.append([line.split(' ')[1]])
      elif 'signal' in line:
        devs[-1] = devs[-1] + [line[-7:]]
    logger.info(devs)
    sleep(1)