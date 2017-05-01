# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import nmap

portScan = nmap.PortScanner()
targetIP = input("Enter a target IP: ")
targetPORT = input("Enter a port or range: ")
portScan.scan(targetIP, targetPORT)
print(portScan[targetIP].state())
print(portScan[targetIP].has_tcp(80))
print(portScan[targetIP].has_udp(53))
