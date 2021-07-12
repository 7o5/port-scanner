<h1> Port Scanner </h1>


<p align="center">
    <img alt="ViewCount" src="https://views.whatilearened.today/views/github/lSANCHOl/port-scanner.svg">
    <a href="https://github.com/lSANCHOl/port-scanner"><img alt="GitHub Clones" src="https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://github.com/lSANCHOl/blob/master/clone.json?raw=True&logo=github"></a>
</p>

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
