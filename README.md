 ____            _       ____
|  _ \ ___  _ __| |_    / ___|  ___ __ _ _ __  _ __   ___ _ __
| |_) / _ \| '__| __|___\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | ||_____|__) | (_| (_| | | | | | | |  __/ |
|_|   \___/|_|   \__|   |____/ \___\__,_|_| |_|_| |_|\___|_|


![badge](https://img.shields.io/github/downloads/lSANCHOl/port-scanner/total)

Usage:
- run port-scanner.py -h for help menu
- use -l to scan IPs from a list
- use -i to scan a single IP
- use -n to autmoatically nmap scan after a single or each port scan


Example:
```
python3 port-scanner.py -i [IP-address]
python3 port-scanner.py -l [Path-to-list]
python3 port-scanner.py -n -i [IP-address] 
python3 port-scanner.py -n -l [Path-to-list]
```
