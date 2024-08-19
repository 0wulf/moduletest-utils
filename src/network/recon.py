import subprocess
import logging

logger = logging.getLogger(__name__)

def recon(iface):
  bin = subprocess.check_output([f'arp -n -i {iface}'], shell=True)
  string = bin.decode('utf-8')
  lines = string.split('\n')[1:-1]
  ipv4s = []
  for line in lines:
    ipv4s.append(line.split(' ')[0])
  logging.info(f'Recon obtained IPv4s: {ipv4s}')
  return ipv4s