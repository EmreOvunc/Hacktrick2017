
# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import re
import sys
import os

if len(sys.argv) == 1:
    print ("Usage: python3 Emails.py /path/to/text/file.txt")
    sys.exit()

elif len(sys.argv) == 2:
    if os.path.exists(sys.argv[1]):
        match = re.findall(r'[\w\.-]+@[\w\.-]+', open(sys.argv[1], 'r').read())
        print (match)
    else:
        print (sys.argv[1]," is not FOUND!")

else:
    print ("Do not give more parameter!")
    print ("Usage: python3 Emails.py /path/to/text/file.txt")
    sys.exit()
