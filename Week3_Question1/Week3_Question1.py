"""
# 
# File      : Question 1.py
# Created   : 01/10/2021 01:34
# Author    : M. Curley
# Version   : v1.0.0
# Licencing : (c) 2021 Michael J. Curley, LYIT
#             Available under GNU Public Licence(GPL)
# Description : A guessing game
#
"""
import random

if __name__ == '__main__':
    num = random.randint(0,100)
    guess = input("Enter a number")
    guess = int(guess)
    count = 1
    ans = ""

    while guess!=num:
        if guess>num:
            print("The number you guessed is too high")
            print("Would you like to guess again")
            ans=input("Please enter Y/N")
            if ans== "Y" or ans == "y" or ans == "yes" or ans == "Yes":
                guess=input("Please enter another number")
                guess=int(guess)
            else:
                print("Thank you for playing the game")
                break
        elif guess < num:
            print("The number you guessed is too low")
            print("Would you like to guess again")
            ans = input("Please enter Y/N")
            if ans== "Y" or ans == "y" or ans == "yes" or ans == "Yes":
                guess = input("Please enter another number")
                guess=int(guess)
            else:
                print("Thank you for playing the game")
                break
        else:
            print("Congratulations, you have guessed the right number")
            print("The correct number was " + str(num))
    print("Game Over")

