# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

import os
import struct
from Crypto.Cipher import AES


def decrypt_file(FileName, chunksize):
    key = raw_input("Enter a key: ")
    if len(key) == 16:
        output = os.path.splitext(FileName)[0]

        with open(FileName, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)

            with open(output, 'wb') as output_File:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    output_File.write(decryptor.decrypt(chunk))

                output_File.truncate(origsize)
    else:
        print("The key must be 16 bytes.")
        print("Your key length is", len(key),".")

decrypt_file("PythonForHackers-Logo.png.xxx", 16*1024)
