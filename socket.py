import random
from socket import *

print("Server is up and running!")

s = socket(AF_INET, SOCK_STREAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

port = 12000


s.bind((gethostname(), port)) # bind to server a tuple (host, portnumber)
# A socket is the end point
s.listen(5)  # the number is the size of the possible Queue


while True:  # listen for ever
    rand_var = random.randint(0,10)


    clientsocket, address = s.accept()  # accept any client
    print("Connection from", address, "has been established")


    data = clientsocket.recv(1024)
    msg = data.decode("utf-8").upper()


    print("The random variable is:", rand_var)
    if(rand_var < 4):  # this resembles packet loss
        print("packet loss has occured")
        print("The server lost:",msg)
        clientsocket.send(bytes("The Packet has been lost!!", "utf-8"))
    else:

        clientsocket.send(msg.encode("utf-8").upper())
        clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()
