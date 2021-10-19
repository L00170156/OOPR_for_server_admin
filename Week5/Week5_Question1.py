"""
# 
# File      : week5_Question1.py
# Created   : 19/10/2021 16:47
# Author    : M. Curley
# Version   : v1.0.0
# Licencing : (c) 2021 Michael J. Curley, LYIT
#             Available under GNU Public Licence(GPL)
# Description :Write a python script to determine system information
#
"""

import platform

if __name__ == '__main__':

    machine = platform.machine()
    print("The machine type is: " + machine)

    node = platform.node()
    print("The computer network name is: " + node)

    os = platform.system()
    print("The underlying OS on this machine is: " + os)

    uname = ('uname:', platform.uname())

    print('system   :', platform.system())
    print('node     :', platform.node())
    print('release  :', platform.release())
    print('version  :', platform.version())
    print('machine  :', platform.machine())
    print('processor:', platform.processor())