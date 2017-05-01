# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import platform

def platformOS():
    if platform.system() == "Linux":
        print("Linux System")

    elif platform.system() == "Windows":
        print("Windows System")

    else:
        print("[ERROR] Unknown operating system!")

platformOS()
