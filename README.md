# `moduletest-utils`
Tools designed for analysis of IoT devices probing for 802.11 AP with SSID `moduletest`.

## Background
Devices probing for the SSID `moduletest` are likely to be IoT devices running a modified version of Tuya ESP8266 firmware.
Sniffing the devices in layer 2 is tricky as the devices send probes on different channels.
The tools help create an AP with SSID `moduletest`, up the AP, recon the devices probing for the SSID and connect to devices on port 6668 to force communication with the device, making a constant stream of packets for obtaining the signal strength.

## Utils
Create access point with SSID `moduletest`:
```bash
$ python3 main.py -a create [-i <interface>]
```

Show connections:
```bash
$ python3 main.py -a show
```

If the connection `moduletest` isn't up, then up the access point:
```bash
$ python3 main.py -a up
```

Run the tool for recon devices, connect to the devices, force communication and monitor the signal strength:
```bash
$ python3 main.py -cs [-i <interface>]
```


