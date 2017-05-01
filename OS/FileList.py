# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import os
userHome = os.path.expanduser('~')
desktop = userHome + os.sep + 'Desktop'
for files in enumerate(os.listdir(desktop)):
    if files[1].endswith("pcap"):
        print(files)
