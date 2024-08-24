# `moduletest-utils`
Tools designed for analysis of IoT devices probing for 802.11 AP with SSID `moduletest`.

## Background
Devices probing for the SSID `moduletest` have been found all over the city of Santiago, Chile. This devices are likely to be IoT devices running a modified version of Tuya ESP8266 firmware.
Locating the devices through trilateration and sniffing in layer 2 is tricky as the devices send probes on different channels.

We can achieve a better signal strength monitoring in layer 3 if we can make the devices connect to a custom WiFi Access Point with SSID `moduletest`, forcing the communication in only one channel and thus calculate more precisely the signal strength of the devices.

The tools help create the WiFi AP, put up the AP, scan the network actively through arp scan, obtaining a constant stream of packets from which calculate and monitor the signal strength, and connecting to the devices on port 6668/tcp for detecting versions in the wild.

## Setup and Usage
Install the requirements either on the user's environment or in a virtual environment
```bash
$ pip3 install -r requirements
# OR RUN THIS ON THE DIRECTORY ROOT
$ python3 -m venv .
```
### `mtsniff`
Run `mtsniff` for setting up the WiFi AP/Hotspot, monitor the devices signal strength, ARP scan for device's IPs, connect to the devices in port 6668/tcp and send dummy payload for version detection and get verbose logs.
```bash
$ sudo python3 main.py mtsniff -cv [-i <interface>]
```

### `mtxtract`
...

### `mtmap`
...

Disclaimer: The tool manages the network via NetworkManager, the default way to manage wireless networks on Debian-like distributions, such as Debian, Ubuntu and Kali.

## To-Do List
- [ ] Web server for monitoring from outside the command line.
- [ ] Mapping utils
- [ ] ...