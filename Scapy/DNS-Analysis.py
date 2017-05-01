# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from scapy.all import *
from scapy.layers.dns import DNS

def capturedPacket(packet):
    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
        print('Packet:', packet.summary().split("/")[3])

while True:
    sniff(iface="eth0", filter="udp port 53", prn=capturedPacket)
