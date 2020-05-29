#!/bin/python3

import sys #used to get arguments when running the script
import socket #used to scan for ports
from datetime import datetime #nice date and time banner for looks

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # translating a hostname to IPv4
else:
	print("Invalid amount of arguments!")
	print("SYNTAX: python3 port_scanner.py <IPv4>")

#add pretty banner
print("=" * 40)
print("Scanning target "+target)
print("Time started:"+str(datetime.now()))

try: #try to connect to port with the exceptions below the for loop
                                
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #if it cant connect to port in 1 sec it will move on
		result = s.connect_ex((target,port)) #returns an error indicator. open port = 0
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt: #if the user does Ctrl C or one like that it will exit 
	print("Exiting program.")
	sys.exit()

except socket.gaierror: #if the hostname can not be turned to IPv4 it will exit
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error: #cant make connection in general will exit
	print("Couldn't connect ot server.")
	sys.exit()
		
	

