import logging
import subprocess


logger = logging.getLogger(__name__)


def scan(iface):
  ipv4s = []
  macs = []
  bin = subprocess.check_output(['arp-scan', '-I', iface, '-l'])
  string = bin.decode('utf-8')
  lines = string.split('\n')[2:-4]
  for line in lines:
    ipv4 = line.split('\t')[0]
    ipv4s.append(ipv4)
    mac = line.split('\t')[1]
    macs.append(mac)
  logger.debug(ipv4s)
  logger.debug(macs)

  return ipv4s