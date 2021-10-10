"""
# 
# File      : question-2.py
# Created   : 01/10/2021 02:47
# Author    : M. Curley
# Version   : v1.0.0
# Licencing : (c) 2021 Michael J. Curley, LYIT
#             Available under GNU Public Licence(GPL)
# Description :
#
"""

if __name__ == '__main__':
    total_price = 0

    for i in range (1,6):
        print("Please enter book title {}:".format(i))
        booktitle = input()
        print("Please enter value of {}:".format(booktitle))
        price = float(input())
        total_price += price
        print("{0:10s} {1:6.2f}".format(booktitle, price))