#!/bin/python3

import argparse
import socket
import os
import signal
import time
import threading
import sys
import subprocess
from queue import Queue
from datetime import datetime

# Start Port scanner with clear terminal
subprocess.call('clear', shell=True)
print("-" * 60)
print("""
 ____            _       ____  
|  _ \ ___  _ __| |_    / ___|  ___ __ _ _ __  _ __   ___ _ __
| |_) / _ \| '__| __|___\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | ||_____|__) | (_| (_| | | | | | | |  __/ |
|_|   \___/|_|   \__|   |____/ \___\__,_|_| |_|_| |_|\___|_|
Made By Sancho 
""")   


# Main Function
def main(ip):
    global outfile
    global t1
    socket.setdefaulttimeout(0.4)
    print_lock = threading.Lock()
    discovered_ports = []
    time.sleep(1)
    target = ip 
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
    #Banner
    print("-" * 60)
    print("Scanning target "+ t_ip)
    print("Time started: "+ str(datetime.now()))
    print("-" * 60)
    t1 = datetime.now()

    def portscan(port):

       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       try:
          conx = s.connect((t_ip, port))
          with print_lock:
             print("Port {} is open".format(port))
             discovered_ports.append(str(port))
          conx.close()

       except (ConnectionRefusedError, AttributeError, OSError):
          pass

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()
      
    q = Queue()
     
    for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

    for worker in range(1, 65536):
       q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print("Port scan completed in "+str(total))
    print("-" * 60) 
    print("*" * 60)
    print("nmap -p{ports} -A -T4 -vv -Pn -oN {ip} {ip}".format(ports=",".join(discovered_ports), ip=target))
    print("*" * 60)
    outfile = "nmap -p{ports} -A -vv -Pn -T4 -oN {ip} {ip}".format(ports=",".join(discovered_ports), ip=target)
    t3 = datetime.now()
    total1 = t3 - t1


#autmomatic NMAP scan

def automate(choice):
    while True:
        if choice == "0":
            print("Would you like to run Nmap or quit to terminal?")
            print("-" * 60)
            print("1 = Run suggested Nmap scan")
            print("2 = Run another port scan")
            print("3 = Exit to terminal")
            print("-" * 60)
            choice = input("Option Selection: ")
        elif choice == "1":
            try:
                print(outfile)
                os.system(outfile)
                t3 = datetime.now()
                total1 = t3 - t1
                print("-" * 60)
                print("Combined scan completed in "+str(total1))
                print("Press enter to quit...")
                input()
                sys.exit()
            except FileExistsError as e:
                print(e)
                exit()
        elif choice == "4":
            try:
                print(outfile)
                os.system(outfile)
                t3 = datetime.now()
                total1 = t3 - t1
                print("-" * 60)
                print("Combined scan completed in "+str(total1))
                break
            except FileExistsError as e:
                print(e)
                exit()
        elif choice == "2":
            ip_addr = input("IP Address: ")
            main(ip_addr)
            automate("0")
        elif choice == "3":
            sys.exit()
        else:
            print("Please make a valid selection")
            automate("0")
    

parser = argparse.ArgumentParser(description='port scan single or multiple IP addresses')
parser.add_argument('-i', '--IP', metavar='', help='single IP address to use')
parser.add_argument('-l', '--list', metavar='', help='Path to list of IP addresses')
parser.add_argument('-n', '--nmap', action='store_true', help='Do NMAP scan automatically after port scan')
args = parser.parse_args()

if __name__ == '__main__':
    if args.list and args.nmap:
        for i in open(args.list):
            main(i.rstrip())
            automate("4") 

    elif args.list:
        for i in open(args.list):
            main(i.rstrip())
        automate("0")

    elif args.IP and args.nmap:
        try:
            main(args.IP)
            automate("1")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()
    
    elif args.IP:
        try:
            main(args.IP)
            automate("0")  
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()
    
