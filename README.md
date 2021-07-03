# port-scanner

<h1> Threaded Port Scanner </h1>

Usage:
- run port-scanner.py -h for help menu
- use -l to scan IPs from a list
- use -i to scan a single IP
- use -n to autmoatically nmap scan after a single or each port scan


Example:
'''
python3 port-scanner.py -i [IP-address]
python3 port-scanner.py -l [Path-to-list]
python3 port-scanner.py -n -i [IP-address] 
python3 port-scanner.py -n -l [Path-to-list]
'''
