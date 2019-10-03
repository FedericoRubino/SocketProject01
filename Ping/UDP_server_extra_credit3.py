'''
Heartbeat Server
Federico Rubino
Timothy Hanneman
'''
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverName = '127.0.0.1'
serverPort = 12000


# Assign IP address and port number to socket
serverSocket.bind((serverName, serverPort))

# The timeout for a heartbeat before we consider client disconnected
HEARTBEAT_TIMEOUT = 10000

# The last sequence number and the time it came at
last_sequence_num = 0
last_time = 0.0

print("Server up and running!")

while True:

    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    # Get the sequence number and time
    ping, current_seq_num, current_time, formated_time = message.split()
    current_seq_num, current_time = int(current_seq_num),float(current_time)

    # If the sequence numbers aren't in order print the number of
    # lost packets
    if(current_seq_num != last_sequence_num+1 and current_time - last_time < HEARTBEAT_TIMEOUT):
        print ("Packet loss has occured!")

    # If the sequence numbers were in order and the heartbeat
    # is still going (less than 10s since last one) print the time
    elif(last_time != 0 and current_time - last_time < HEARTBEAT_TIMEOUT):
        print ("Heartbeat")

    # Capitalize the message from the client
    message = message.upper()

    # If rand is less is than 4, we consider the packet
    # lost and do not respond
    if rand < 4:
        continue

    # Otherwise, the server responds
    serverSocket.sendto(message, address)

    # Save the sequence number and time
    last_sequence_num = current_seq_num
    last_time = current_time
