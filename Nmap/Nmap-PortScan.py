# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import nmap

portScan = nmap.PortScanner()
targetIP = input("Enter a target IP: ")
targetPORT = input("Enter a port or range: ")
portScan.scan(targetIP, targetPORT)
print(portScan.scaninfo())
print(portScan.all_hosts())
