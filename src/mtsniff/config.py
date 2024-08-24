SLEEP_TIME = 1

class MessageConfig:
  DUMMY_PAYLOAD = bytes(bytearray.fromhex('deadbeef112233445566778899aabbccddeeffb00bface112233feedbabe74f0'))

class NetworkConfig:
  INTERFACE = 'wlan1'
  CHANNEL = 11
  SSID = 'moduletest'
  PSK = 'test1234'

class GPSConfig:
  HOST = '172.20.10.1'
  PORT = 11000