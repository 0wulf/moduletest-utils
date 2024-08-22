import subprocess
import logging


logger = logging.getLogger(__name__)

class Monitor:
  def __init__(self, iface):
    self.iface = iface

  def get_signal(self):
    lines = subprocess.check_output(['iw' ,'dev', self.iface, 'station', 'dump']).decode('utf-8').split('\n')
    devs = []
    for line in lines:
      if 'Station' in line:
        devs.append([line.split(' ')[1]])
      elif 'signal' in line:
        devs[-1] = devs[-1] + [line[-7:]]
    for dev in devs:
      logger.info(dev)

    return devs

  '''
  Scan via arp-scan for dynamic IP addresses. Noisy
  '''
  def scan(self):
    ipv4s, macs = [], []
    lines = subprocess.check_output(['arp-scan', '-I', self.iface, '-l']).decode('utf-8').split('\n')[2:-4]
    for line in lines:
      ipv4, mac = line.split('\t')[0], line.split('\t')[1]
      ipv4s.append(ipv4)
      macs.append(mac)
    logger.debug([ipv4s, macs])

    return ipv4s