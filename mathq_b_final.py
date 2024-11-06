#!/usr/bin/env python3
# mathq_b_final.py -- an interactive math program
# Usage : nested_if.py
# Author : Jose Ortiz
# Created on : November 6, 2024
# Description : mathq_b_final.py
#
#*************************************************************

import random
import re

def generate_question():
    operator = random.randint(0, 3)
    if operator == 0:  # Addition
        first_num = random.randint(0, 9)
        second_num = random.randint(0, 9)
        solution = first_num + second_num
        question = f"{first_num} + {second_num} = "
        return question, solution, 'addition'
    elif operator == 1:  # Subtraction
        second_num = random.randint(0, 9)
        if second_num == 0:
            first_num = 0
        else:
            first_num = random.randint(second_num, 9)
        solution = first_num - second_num
        question = f"{first_num} - {second_num} = "
        return question, solution, 'subtraction'
    elif operator == 2:  # Multiplication
        first_num = random.randint(0, 9)
        second_num = random.randint(0, 9)
        solution = first_num * second_num
        question = f"{first_num} x {second_num} = "
        return question, solution, 'multiplication'
    else:  # Division
        second_num = random.randint(1, 9)
        solution = random.randint(0, 9)
        first_num = second_num * solution
        question = f"{first_num} / {second_num} = "
        return question, solution, 'division'

def main():
    print("Welcome to the mathq program.")
    print("You can type 'q' or 'Q' at any time to quit the program.")

    keep_asking_questions = True
    correct_answers = 0
    incorrect_answers = 0
    total_questions = 0
    stats = {
        'addition': {'correct': 0, 'total': 0},
        'subtraction': {'correct': 0, 'total': 0},
        'multiplication': {'correct': 0, 'total': 0},
        'division': {'correct': 0, 'total': 0}
    }

    while keep_asking_questions:
        question, solution, q_type = generate_question()
        stats[q_type]['total'] += 1

        response_is_not_valid = True
        while response_is_not_valid:
            print(question, '?')
            response = input("> ")
            match = re.search("^[0-9]+$|^q$", response, re.IGNORECASE)
            if match:
                response_is_not_valid = False
            else:
                print("That was an invalid response. Enter a number or 'q' to quit.")

        if response.lower() == 'q':
            keep_asking_questions = False
        else:
            total_questions += 1
            if int(response) == solution:
                print('Correct!')
                correct_answers += 1
                stats[q_type]['correct'] += 1
            else:
                print(f"Incorrect! {question} {solution}")
                incorrect_answers += 1

    if total_questions > 0:
        print(f"You answered {correct_answers} out of {total_questions} questions correctly, or {correct_answers / total_questions * 100:.0f}% correctly.")
        for q_type, data in stats.items():
            if data['total'] > 0:
                print(f"For the {q_type} problems, you answered {data['correct'] / data['total'] * 100:.0f}% correctly.")
    else:
        print("You did not answer any questions.")

    print("Thank you for playing mathq.")