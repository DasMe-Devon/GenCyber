#!/usr/bin/env python
	# Defines that we want to use python to interpret the code.

import socket
	# the socket library is utilized to communicate with other sockets. 
	# Socket = IP Address + Port. IE: 192.168.187.131:80

target = raw_input("What IP should I scan? ")
	# Prompt the user for an IP address.
port = raw_input("What port? ")
	# Prompt the user for a port to scan on an IP address.

# We use a try/except block to determine if a port is open or not.
# If the port is open, it will print out what was received.
# If the port is closed, the except: block is hit and it prints an error.
try:
	socketObj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		# AF_INET = IPv4 Address
		# SOCK_STREAM = TCP Connection
		# This object is a prototype that wil require an IP and PORT to connect with.
	socketObj.connect((target,int(port)))
		# Connect to the target on a particular port.
	socketObj.send("GET / \r\n\r\n")
		# Send data to the listening service.
	results = socketObj.recv(1024)
		# Record the output.
	print results
		# Print the results.
except:
	print "Error while trying to connect to: %s:%s" % (target,port)