#!/usr/bin/env python3

import random

elementes = (2, 3, 4, 5, 6, 7, 8, 9)
wrong_answers = 0
re_multiplier = None
re_multiplicable = None
test_question = int(0)
attempts = int(10)
passed_questions = dict()

while test_question < attempts:

    multiplicable = random.choice(elementes)
    multiplier = random.choice(elementes)

    if re_multiplicable is not None:
        multiplicable = re_multiplicable
        multiplier = re_multiplier
        re_multiplier = None 
        re_multiplicable = None
    else:
        if multiplicable in passed_questions.keys():
            print(multiplicable)
            if passed_questions[multiplicable] == multiplier:
                print(multiplier)
                continue

    result = multiplicable * multiplier
    print(f"{multiplicable} x {multiplier} =", end=' ')

    try:
        input_result = int(input())
    except ValueError:
        print("Only numbers allowed")
        re_multiplicable = multiplicable
        re_multiplier = multiplier
        continue

    if input_result != result:
        print(f"Wrong answer, correct - {multiplicable} x {multiplier} = {result}")
        wrong_answers += 1

    passed_questions[multiplicable] = multiplier
    test_question += 1

print(f"Wrong answers - {wrong_answers}")
print(test_question)

for pairs in passed_questions.items():
    print(pairs)