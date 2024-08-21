# `moduletest-utils`
Tools designed for analysis of IoT devices probing for 802.11 AP with SSID `moduletest`.

## Background
Devices probing for the SSID `moduletest` are likely to be IoT devices running a modified version of Tuya ESP8266 firmware.
Sniffing the devices in layer 2 is tricky as the devices send probes on different channels.
The tools help create an AP with SSID `moduletest`, set up the AP, scan the network actively through arp scan, obtaining a constant stream of packets from which calculate and monitor the signal strength, and connecting to the devices on port 6668/tcp for detecting versions in the wild.

## Utils
Clear (put down) active connections on your interface
```bash
$ python3 main.py -a clear [-i <interface>]
```

Create access point with SSID `moduletest` (if not created yet):
```bash
$ python3 main.py -a create [-i <interface>]
```

Run the tool for scan the network for devices, monitor the devices signal strength, connect to the devices in port 6668/tcp and send dummy payload for version detection, and get verbose logs.
```bash
$ python3 main.py -cmv [-i <interface>]
```


## To-Do List
- [ ] Connection to GPS server
- [ ] SQLite / InfluxDB for storing known devices, measurements and coordinates, responses to commands on port 6668.
- [ ] Web server for monitoring from outside the command line.
- [ ] Mapping utils
- [ ] ...