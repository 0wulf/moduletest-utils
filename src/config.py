SLEEP_TIME = 1

class MessageConfig:
  DUMMY_PAYLOAD = bytes(bytearray.fromhex('deadbeef112233445566778899aabbccddeeffb00bface112233feedbabe74f0'))

class NetworkConfig:
  IPv4s = ['10.42.0.169']
  INTERFACE = 'wlan1'
  CHANNEL = 11
  SSID = 'moduletest'
  PSK = 'test1234'