#!/usr/bin/env python3

import random

elementes = (2, 3, 4, 5, 6, 7, 8)
wrong_answers = 0
re_multiplier = None
re_multiplicable = None
test_question = int(0)
attempts = int(5)

while test_question < 5:
    
    print(f"attempts {attempts} and question - {test_question}")
    multiplicable = random.choice(elementes)
    multiplier = random.choice(elementes)

    if re_multiplicable is not None:
        multiplicable = re_multiplicable
        multiplier = re_multiplier
        re_multiplier = None 
        re_multiplicable = None

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
        print(f"{multiplicable} x {multiplier} = {result}")
    else:
        wrong_answers += 1
    test_question += 1

print(f"Wrong answers - {wrong_answers}")