'''
Python3 
UDP_Pinger_Client.py
'''
#IMPORTS (Timing library and socket for network)
import time
from socket import*

serverName ='127.0.0.1'
serverPort = 12000
#Creating a Socket object that accepts an address and datagram
clientSocket = socket(AF_INET,SOCK_DGRAM)
#Giving the socket a timeout of 1 so that it doesn't wait forever
clientSocket.settimeout(1)

#For each i (ten total) send a 'ping' packet
#Its format is 'sequence# timing#'
for i in range(10):
	the_time = int(time.time()*1000)
	message = str(i) + " " + str(the_time)
	
	#Socket sends message to address+port#
	clientSocket.sendto(message.encode(),(serverName, serverPort))

	#Using try/except to detect timeout
	#It will listen for a message and store the address its from until
	# either it gets the message or timesout
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	except timeout as e:
		print (e)
		continue

	#So long as it doesn't timeout it should take the datagram, decode it, split
	# it at the space by its sequence number and timing 
	sequence_num, timing = modifiedMessage.decode().split()
#Would be nice to format the numbers to resemble what they should
#Need to add calculations
	RTT = float((int(time.time()*1000)-int(timing))/1000)
	print (str(sequence_num) + " " + str(RTT)) 
