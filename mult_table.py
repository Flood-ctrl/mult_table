#!/usr/bin/env python3

wrong_answers = 0
re_multiplier = None
re_multiplicable = None
test_question = int(0)

for multiplicable in range(1, 10):
    for multiplier in range(1, 10):
        test_question = +1
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
        if input_result == result:
            continue
        else:
            wrong_answers = +1
            print(f"{multiplicable} x {multiplier} = {result}")

print(f"Wrong answers - {wrong_answers}")