# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import nmap

portScan = nmap.PortScanner()
targetIP = input("Enter a target IP: ")
targetPORT = input("Enter a port or range: ")
portScan.scan(targetIP, targetPORT)
for hosts in portScan.all_hosts():
    print("Host:", hosts)
    print("Port:", portScan[hosts].all_tcp())
    print("State:", portScan[hosts].state(), "\n")
