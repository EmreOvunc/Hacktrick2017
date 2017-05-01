# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from scapy.all import *
ipPacket = IP()
icmpPacket = ICMP()
targetIP = input('Target IP: ')
ipPacket.dst = targetIP
sourceIP = input('Source IP: ')
ipPacket.src = sourceIP

ipPacket.show()
icmpPacket.show()
send(ipPacket/icmpPacket)
