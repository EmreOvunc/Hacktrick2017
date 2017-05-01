# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import socket

targetIP = input("Hedef IP: ")
port_Start = int(input("Baslangic portu: "))
port_End = int(input("Bitis portu: "))

for port in range(port_Start, port_End):
    portSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    portSocket.settimeout(0.05)
    try:
        conn = portSocket.connect((targetIP, port))
        print("Port ", port, " --> OPEN")
    except:
        print("Port ", port, " --> CLOSED")
