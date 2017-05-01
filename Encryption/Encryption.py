# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import os
import random
import struct
from Crypto.Cipher import AES


def encrypt_file(FileName, chunksize):
    key = raw_input("Enter a key: ")
    if len(key) == 16:
        output = FileName + '.xxx'

        iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        fileSize = os.path.getsize(FileName)

        with open(FileName, 'rb') as input_File:
            with open(output, 'wb') as output_File:
                output_File.write(struct.pack('<Q', fileSize))
                output_File.write(iv)

                while True:
                    chunk = input_File.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)

                    output_File.write(encryptor.encrypt(chunk))
    else:
        print ("The key must be 16 bytes.")
        print ("Your key length is", len(key), ".")

encrypt_file("PythonForHackers-Logo.png", 16*1024)
