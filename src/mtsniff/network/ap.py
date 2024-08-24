import subprocess

from src.mtsniff.config import NetworkConfig as NC

class AP:
  def __init__(self, interface=NC.INTERFACE):
    self.ssid = NC.SSID
    self.password = NC.PSK
    self.channel = NC.CHANNEL
    self.interface = interface
    self.start()

  def start(self):
    subprocess.call(['nmcli', 'dev', 'wifi', 'hotspot', 'ifname', self.interface, 'con-name', self.ssid, 'ssid', self.ssid, 'password', self.password]) 
