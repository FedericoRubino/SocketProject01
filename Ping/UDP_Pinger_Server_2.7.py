'''
UDP Pinger Server
Python 2.7 Version
September 20, 2019
Will be updated to Python 3
Federico Rubino
Timothy Hanneman
'''
import random
from socket import *

#Create a UDP socket
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is a constant used for ipv4 adresses and a port number
# Creates a socket object named serverSocket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
# Bind is used for server side
serverSocket.bind(('',12000))

while True:
	# Generate random number in the range of 0 to 10
	rand = random.randint(0, 10)
	# Receive the client packet along with the address it is coming from. 1024 is the buffer size
	#Return type of .recvfrom is a message of bytes, address
	message, address = serverSocket.recvfrom(1024)
	# If rand is less than 4, we consider the packet lost and do not respond
	if rand < 4:
		continue
	# Capitalize the message from the client
	message = message.upper()
	#Otherwise, the server responds
	serverSocket.sendto(message, address)
