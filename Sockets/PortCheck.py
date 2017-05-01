# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import socket

targetIP = input("Target IP: ")
portSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    conn = portSocket.connect((targetIP, 80))
    print("Port 80 is OPEN!")
except:
    print("Port 80 is CLOSED!")
