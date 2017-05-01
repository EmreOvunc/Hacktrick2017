# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from scapy.all import *
arpPacket = ARP()
targetIP = input('Target IP: ')
arpPacket.pdst = targetIP

arpPacket.show()
send(arpPacket)
