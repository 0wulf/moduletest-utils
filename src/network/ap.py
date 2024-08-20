import subprocess

from src.config import NetworkConfig as NC

class AP:
  def create(iface):
    subprocess.call(f'nmcli con add type wifi ifname {iface} con-name {NC.SSID} ssid {NC.SSID} mode ap', shell=True)
    subprocess.call(f'nmcli con modify {NC.SSID} 802-11-wireless.band bg', shell=True)
    subprocess.call(f'nmcli con modify {NC.SSID} 802-11-wireless.channel {NC.CHANNEL}', shell=True)
    subprocess.call(f'nmcli con modify {NC.SSID} 802-11-wireless.cloned-mac-address 00:11:22:33:44:55', shell=True)
    subprocess.call(f'nmcli con modify {NC.SSID} ipv4.method shared', shell=True)
    subprocess.call(f'nmcli con modify {NC.SSID} wifi-sec.key-mgmt wpa-psk', shell=True)
    subprocess.call(f'nmcli con modify {NC.SSID} wifi-sec.psk "{NC.PSK}"', shell=True)
  def up():
    subprocess.call(f'nmcli con up {NC.SSID}', shell=True)
  def down():
    subprocess.call(f'nmcli con down {NC.SSID}', shell=True)
  def delete():
    subprocess.call(f'nmcli con delete {NC.SSID}', shell=True)
  def show():
    subprocess.call('nmcli con show', shell=True)