import subprocess

from src.config import NetworkConfig as NC

class AP:
  def create(iface):
    subprocess.call(['nmcli' ,'con','add','type','wifi','ifname',iface,'con-name',NC.SSID,'ssid',NC.SSID,'mode','ap'])
    subprocess.call(['nmcli', 'con', 'modify', NC.SSID, '802-11-wireless.band', 'bg'])
    subprocess.call(['nmcli', 'con', 'modify', NC.SSID, '802-11-wireless.channel', f'{NC.CHANNEL}'])
    subprocess.call(['nmcli', 'con', 'modify', NC.SSID, '802-11-wireless.cloned-mac-address', '00:11:22:33:44:55'])
    subprocess.call(['nmcli', 'con', 'modify', NC.SSID, 'ipv4.method','shared'])
    subprocess.call(['nmcli', 'con', 'modify', NC.SSID, 'wifi-sec.key-mgmt','wpa-psk'])
    subprocess.call(['nmcli', 'con', 'modify', NC.SSID, 'wifi-sec.psk',f'"{NC.PSK}"'])
    subprocess.call(['nmcli', 'con', 'modify', NC.SSID, 'connection.autoconnect', 'no'])
  def up():
    subprocess.call(['nmcli', 'con', 'up', NC.SSID])
  def down():
    subprocess.call(['nmcli', 'con', 'down', NC.SSID])
  def delete():
    subprocess.call(['nmcli', 'con', 'delete', NC.SSID])
  def clear(iface):
    bin = subprocess.check_output(['nmcli', 'con', 'show'])
    string = bin.decode('utf-8')
    lines = string.split('\n')
    cons = []
    for line in lines:
      if iface in line:
        cons.append(line.split(' ')[0])
    for con in cons:
      subprocess.call(['nmcli', 'con', 'down', con])

    