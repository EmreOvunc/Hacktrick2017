# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

file = open('/home/$USERNAME/Desktop/dosya.txt', 'w')
file.write('Python for Hackers\n')
file.write('My first file :)')
file.close()

file2 = open("/home/$USERNAME/Desktop/dosya.txt", "r")
lines = file2.read()
print(lines)
file2.close()
