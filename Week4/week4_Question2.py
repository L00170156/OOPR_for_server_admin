"""
# 
# File      : Question_2.py
# Created   : 10/10/2021 06:14
# Author    : M. Curley
# Version   : v1.0.0
# Licencing : (c) 2021 Michael J. Curley, LYIT
#             Available under GNU Public Licence(GPL)
# Description :Generating random lotto numbers for a list of names
#
"""

import random

if __name__ == '__main__':

    week_1 = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]
    wk1_list_size = len(week_1)
    # Itnitialise the dictionary to hold the week 1 lotto numbers for each player
    lotto_num_wk1 = {}

    # Iterate over the list to generate lotto number
    for i in range(0, wk1_list_size):
        num = random.randint(1, 20)
        lotto_num_wk1[week_1[i]] = num

    # print(lotto_num_wk1)

    week_2 = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
    wk2_list_size = len(week_2)
    lotto_num_wk2 = {}

    for i in range(0, wk2_list_size):
        num = random.randint(1, 20)
        lotto_num_wk2[week_2[i]] = num

    # print(lotto_num_wk2)

    played_both_weeks = []
    unique_names = []
    week_1_set = set(week_1)
    week_2_set = set(week_2)

    # Question 2.1 - Who bought tickets on both weeks
    played_both_weeks = week_1_set & week_2_set
    print(played_both_weeks)

    # Question 2.2 - Unique players over both weeks
    unique_names = week_1_set | week_2_set
    print(unique_names)

    # Question 2.3 - Most common lotto numbers

    all_lotto_numbers = list(lotto_num_wk1.values()) + list(lotto_num_wk2.values())
    print(all_lotto_numbers)

    from collections import Counter

    c = Counter(all_lotto_numbers)

    print(c)

    # Question 2.4 - Did any member pick the same number on multiple occasions