# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import subprocess
firefox_Proc = subprocess.Popen(['ps -A | grep firefox | cut -c -6'], stdout=subprocess.PIPE, shell=True)
(out, err) = firefox_Proc.communicate()
if out.decode() != "":
    print('Firefox PID:', out.decode())
else:
    print('Firefox not found in ps!')
