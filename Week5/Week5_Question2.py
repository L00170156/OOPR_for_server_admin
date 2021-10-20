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


def encrypt_password(password):
    my_password = password.encode("utf-8")
    encoded = base64.b64encode(my_password)
    return encoded


def decrypt_password(encoded):
    my_encoded = encoded.encode("utf-8")
    decoded = base64.b64decode(my_encoded)
    return decoded


if __name__ == '__main__':
    import timeit

    encode = encrypt_password("Michael")

    print(timeit.timeit("encrypt_password('Michael')", setup="from __main__ import encrypt_password"))

    print(timeit.timeit("decrypt_password(encode)", setup="from __main__ import decrypt_password"))
