# BITMEDI

from scapy.all import *
arpPacket = ARP()
targetIP = input('Target IP: ')
targetNetwork = ""

for ip in range(0, 3):
    targetNetwork += targetIP.split(".")[ip] + "."

for ipRange in range(1, 255):
    arpPacket.pdst = targetNetwork + str(ipRange)
    ans = srp(arpPacket)
    print(ans)
