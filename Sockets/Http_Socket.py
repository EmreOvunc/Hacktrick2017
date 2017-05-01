# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import socket
mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
mySocket.connect(('www.google.com', 80))
mySocket.send('GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'.encode())
data = mySocket.recv(2048)
mySocket.close()
print(data.decode())
