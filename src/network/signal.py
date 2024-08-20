import subprocess
import logging


logger = logging.getLogger(__name__)

def signal_mon(iface):
  bin = subprocess.check_output(['iw' ,'dev', iface, 'station', 'dump'])
  string = bin.decode('utf-8')
  lines = string.split('\n')
  devs = []
  for line in lines:
    if 'Station' in line:
      devs.append([line.split(' ')[1]])
    elif 'signal' in line:
      devs[-1] = devs[-1] + [line[-7:]]
  for dev in devs:
    logger.info(dev)