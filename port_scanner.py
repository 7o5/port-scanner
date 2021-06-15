#!/usr/bin/python3

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

# Main Function
def main(ip):
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()
    discovered_ports = []
    time.sleep(1)
    target = ip
    error = "SYNTAX: python3 thread_port_scanner.py" 
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
     
    #startTime = time.time()
     
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

#Nmap Integration (in progress)

    def automate():
       choice = '0'
       while choice =='0':
          print("Would you like to run Nmap or quit to terminal?")
          print("-" * 60)
          print("1 = Run suggested Nmap scan")
          print("2 = Run another port scan")
          print("3 = Exit to terminal")
          print("-" * 60)
          choice = input("Option Selection: ")
          if choice == "1":
             try:
                print(outfile)
                os.system(outfile)
                t3 = datetime.now()
                total1 = t3 - t1
                print("-" * 60)
                print("Combined scan completed in "+str(total1))
                print("Press enter to quit...")
                input()
             except FileExistsError as e:
                print(e)
                exit()
          elif choice =="2":
              ip_addr = input("IP Address: ")
              main(ip_addr)
          elif choice =="3":
             sys.exit()
          else:
             print("Please make a valid selection")
             automate()
    

parser = argparse.ArgumentParser(description='port scan single or multiple IP addresses')
parser.add_argument('-i', '--IP', metavar='', help='single IP address to use')
parser.add_argument('-l', '--list', metavar='', help='Path to list of IP addresses')
args = parser.parse_args()

if __name__ == '__main__':
    if args.list:
        with open(args.list) as f:
            ip_list = f.readlines()
            size = (len(ip_list) - 1)
            for i in range(0,size):
                ip = ip_list[i].rstrip()  
                main(ip)
     
    elif args.IP:
        try:
            main(args.IP)
     
        except KeyboardInterrupt:
            print("\nGoodbye!")
            quit()
   
