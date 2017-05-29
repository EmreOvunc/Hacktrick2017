import re
pattern = re.compile("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")
if pattern.match("aa:bb:Cc:11:22:33"):
    print "Ok!"
