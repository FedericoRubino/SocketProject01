'''
  Python3
  UDP_Pinger_Client.py
'''

"""
You need to implement the following client program.
The client should send 10 pings to the server.

# check

Because UDP is an unreliable protocol, a packet
sent from the client to the server may be lost in the network,
or vice versa. For this reason, the
client cannot wait indefinitely for a reply to a ping message. You should
get the client wait up to
one second for a reply; if no reply is received within one second, your
client program should
assume that the packet was lost during transmission across the network.

# check

You will need to look up the Python documentation to
find out how to set the timeout value on a datagram socket.
The program must calculate the round-trip
time for each packet and prints it out individually.

# check

Modify this to correspond to the way the standard ping program works.
You will need to report the minimum, maximum, and average RTTs at the end
of all pings from the client. Suggest what should be the timeout
period based on the timeout. In addition, calculate the packet loss
rate(in percentage).

# check

"""





#IMPORTS (Timing library and socket for network and math functions)
import time
from socket import*
import statistics



serverName ='127.0.0.1'
serverPort = 12000

# list to be used for tracking RTTs
RTT_times = [(-1) for _ in range(10)]



#Creating a Socket object that accepts an address and datagram
clientSocket = socket(AF_INET,SOCK_DGRAM)

#Giving the socket a timeout of 1 so that it doesn't wait forever
clientSocket.settimeout(1)

#For each i (ten total) send a 'ping' packet
#Its format is 'sequence# timing#'
for i in range(10):
    the_time = time.time()*1000

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

    # So long as it doesn't timeout it should take the datagram,
    # decode it, split
    # it at the space by its sequence number and timing
    sequence_num, timing = modifiedMessage.decode().split()
    #Would be nice to format the numbers to resemble what they should
    #Need to add calculations

    # Roundtrip time is calculated by finding the difference between the
    # time before the message was sent and after it was received
    #RTT = float((int(time.time()*1000)-int(timing))/1000)
    RTT = '%.5f' % ((time.time()*1000 - the_time)/1000)
    RTT_times[i] = float(RTT)
    print ("Ping Number:",str(sequence_num),"RTT:", str(RTT))


found_packages = list(filter(lambda x: x > 0,RTT_times))
print()
print("Package loss rate: "+ str((10-len(found_packages))/10 *100) + "%")
print()
print("min:",'%.5f' % min(found_packages))
print("max:",'%.5f' % max(found_packages))
print("mean:",'%.5f' % statistics.mean(found_packages))
print()
print("Suggested timerate is:", '%.5f' % (max(found_packages)*100))

