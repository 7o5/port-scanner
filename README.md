<h1> Port Scanner </h1>


<p align="center">
    <img alt="ViewCount" src="https://views.whatilearened.today/views/github/lSANCHOl/port-scanner.svg">
    [![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=<url>?raw=True&logo=github)](https://github.com/lSANCHOl/port-scanner)

</p>

Usage:
```
usage: port-scanner [-h] [-i] [-l] [-n] [-q]

port scan single or multiple IP addresses

optional arguments:
  -h, --help    show this help message and exit
  -i , --IP     single IP address to use
  -l , --list   Path to list of IP addresses
  -n, --nmap    Do NMAP scan automatically after port scan
  -q, --quiet   Don't print banner at the start
```


Example:
```
python3 port-scanner.py -i [IP-address]
python3 port-scanner.py -l [Path-to-list]
python3 port-scanner.py -n -i [IP-address] 
python3 port-scanner.py -n -l [Path-to-list]
```
