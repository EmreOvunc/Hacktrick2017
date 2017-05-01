# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import _thread
import time

def oddNumbers(number):
    while True:
        time.sleep(2)
        print(number)
        number += 2

def evenNumbers(number):
    while True:
        time.sleep(1)
        print(number)
        number += 2

_thread.start_new_thread(oddNumbers, (1, ))
_thread.start_new_thread(evenNumbers, (0, ))

while 1:
    time.sleep(2)
    print("Python for Hackers!!!")
