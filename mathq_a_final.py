#!/usr/bin/env python3
# mathq_a_final.py -- an interactive math program
# Written by Department of Computer Science of Hunter College
# September 5, 2020
# Usage: mathq_a_final.py

#-----------------------------------------------------------------------------
# Main program
#-----------------------------------------------------------------------------

import random # can you guess what random is for?
import re     # what about this module?
print("Welcome to the mathq program.")
keep_asking_questions = True
while keep_asking_questions:
    # <<Generate a random math question and its solution>>
    first_num = random.randint(0, 9)
    second_num = random.randint(0, 9)
    operator = random.randint(0, 1)
    if operator == 1:
        # <<create multiplication question and solution>>
        solution = first_num * second_num
        question = "%d x %d = " % (first_num, second_num)
    else:
        # <<create division question and solution>>
        # Ensure second_num is not zero to avoid division by zero
        second_num = random.randint(1, 9)
        solution = first_num
        first_num = first_num * second_num
        question = "%d / %d = " % (first_num, second_num)
    # <<Display the question and get valid response>>
    response_is_not_valid = True
    while response_is_not_valid:
        print(question, '?')
        response = input("> ")
        # <<check if response is valid>>
        match = re.search("^[0-9]+$|^q$", response)
        if match:
            response_is_not_valid = False
        else:
            print("That was an invalid response. Enter a number or 'q' to quit.")
    # <<Check correctness of user's response>>
    if response == 'q':
        keep_asking_questions = False
    else:
        if int(response) == solution:
            print('Correct!')
        else:
            print("Incorrect! %s %d" % (question, solution))
print("Exiting the mathq program.")