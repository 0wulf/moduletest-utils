# `moduletest-utils`
Tools designed for analysis of IoT devices probing for 802.11 AP with SSID `moduletest`.

## Background
Devices probing for the SSID `moduletest` are likely to be IoT devices running a modified version of Tuya ESP8266 firmware.
Sniffing the devices in layer 2 is tricky as the devices send probes on different channels.
The tools help create an AP with SSID `moduletest`, set up the AP, scan the network actively through arp scan, obtaining a constant stream of packets from which calculate and monitor the signal strength, and connecting to the devices on port 6668/tcp for detecting versions in the wild.

## Utils
Before setting up the access point, make sure yout interface is clean and has all connections down (this is going to be implemented on the utils).


Create access point with SSID `moduletest`:
```bash
$ python3 main.py -a create [-i <interface>]
```

Show connections:
```bash
$ python3 main.py -a show
```

If the connection `moduletest` isn't up, then set up the access point:
```bash
$ python3 main.py -a up
```

Run the tool for scan the network for devices, monitor the devices signal strength, connect to the devices in port 6668/tcp and send dummy payload for version detection, and get verbose logs.
```bash
$ python3 main.py -cmv [-i <interface>]
```


## To-Do List
- [ ] Method for clearing interface connections
- [ ] Connection to GPS server
- [ ] SQLite for storing known devices, measurements and coordinates, responses to commands on port 6668.
- [ ] Web server for monitoring from outside the command line.
- [ ] ... 