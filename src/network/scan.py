import logging
import subprocess


logger = logging.getLogger(__name__)


def scan(iface):
  ipv4s = []
  bin = subprocess.check_output(['arp-scan', '-I', iface, '-l'])
  string = bin.decode('utf-8')
  lines = string.split('\n')[2:-4]
  for line in lines:
    ipv4 = line.split('\t')[0]
    ipv4s.append(ipv4)
  logger.info(ipv4s)

  return ipv4s