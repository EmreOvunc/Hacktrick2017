# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from scapy.all import *
arpPacket = ARP()
networkID = input('Enter Network ID: ')
IP = '.'.join(networkID.split(".")[x] for x in range(3)) + "."

for IPs in range(1, 255):
    arpPacket.pdst = IP + str(IPs)
    send(arpPacket)
