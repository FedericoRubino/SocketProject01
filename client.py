from socket import *

pings = [(chr(x + 97) + " Packet") for x in range(10)]
s = socket(AF_INET, SOCK_STREAM)
port = 12000

s.connect((gethostname(), port))

for x in pings:
    print(x)

inputVar = input("string you want to uppercase: ")
inputVar += "\n"

s.sendall(inputVar.encode('utf-8'))


full_msg = ''
while True:
    msg = s.recv(1024)  # how big of data buffer is allowed
    if len(msg) <=0:
        break
    full_msg += msg.decode("utf-8") + "\n"
print(full_msg)
