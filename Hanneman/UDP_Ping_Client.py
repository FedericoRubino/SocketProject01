'''
Python 2.7
UDP_Pinger_Client.py
'''
import time
from socket import*

serverName ='127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
	the_time = int(time.time()*1000)
	message = str(i) + " " + str(the_time)
	clientSocket.sendto(message.encode(),(serverName, serverPort))
	try:
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	except timeout as e:
		print e
		continue
	sequence_num, timing = modifiedMessage.decode().split()
#Would be nice to format the numbers to resemble what they should
#Need to add calculations
	RTT = int(time.time()*1000)-int(timing)
	print str(sequence_num) + " " + str(RTT) 
