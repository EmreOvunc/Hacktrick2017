# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import paramiko

ServerIP = input('Enter server IP: ')
username = input('Username: ')
password = input('Password: ')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(ServerIP, username=username, password=password)
session = client.get_transport().open_session()
if session.active:
    command = input('Command: ')
    session.exec_command(command)
    print('Server: ', session.recv(1024))
