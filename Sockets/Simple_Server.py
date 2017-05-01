# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import socket
mySocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
mySocket.bind(('192.168.1.30', 8088))
mySocket.listen(1)

while True:
    client, addr = mySocket.accept()
    print(addr[0], 'is connected to the server!')
    client.send('Server loves you bro'.encode())
    client.close()
