# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from Crypto.Cipher import AES

message = "my secret answer"
iv = "This is an IV..."
key = "This is a key..."

ENCobject = AES.new(key, AES.MODE_CBC, iv)
cipherText = ENCobject.encrypt(message)
print("Cipher Text: ", cipherText)

DECobject = AES.new(key, AES.MODE_CBC, iv)
plainText = DECobject.decrypt(cipherText)
print("Plain Text: ", plainText)
