# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from pynput.keyboard import Listener

def on_press(key):
    print("Key:", str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
