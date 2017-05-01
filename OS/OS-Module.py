# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import os
print("getpid():", os.getpid(), "\n ")
print("getlogin():", os.getlogin(), "\n")
print("uname():", os.uname(), "\n")
print("getcwd():", os.getcwd(), "\n")
print('MyFolder exists:', os.path.exists('MyFolder'), "\n")
print('file.txt isfile:', os.path.isfile('file.txt'), "\n")

os.system("ls -la")

print("\nname:", os.name)
print("sep:", os.sep)
print("listdir:", os.listdir())

