# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import socket
mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
mySocket.connect(('192.168.1.30', 8088))
print(mySocket.recv(1024).decode())
mySocket.close()
