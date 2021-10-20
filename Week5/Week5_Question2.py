"""
# 
# File      : Week5_Question2.py
# Created   : 19/10/2021 17:39
# Author    : M. Curley
# Version   : v1.0.0
# Licencing : (c) 2021 Michael J. Curley, LYIT
#             Available under GNU Public Licence(GPL)
# Description : Encrypt and Decrypt a password in python
#
"""
import base64

if __name__ == '__main__':

    password = "my_password".encode("utf-8")

    encoded = base64.b64encode(password)
    print(encoded)

    decoded = base64.b64decode(encoded)
    print(decoded)