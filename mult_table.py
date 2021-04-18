#!/usr/bin/env python3

import sys, getopt, random

elementes = (2, 3, 4, 5, 6, 7, 8, 9)
wrong_answers = 0
re_multiplicable = None
re_multiplier = None
start_multiplicable = int(0)
test_question = int(0)
attempts = len(elementes)
passed_questions = list()
input_attempts = None
input_table = None

# Validate input arguments
try:
   opts, args = getopt.getopt(sys.argv[1:],"h:a:t:")
except getopt.GetoptError:
   print (f'{sys.argv[0]} -a <attempts> -t <table>')
   if sys.argv[1] == "-h" or sys.argv[1] == "--help":
       sys.exit(0)
   sys.exit(2)

for opt, arg in opts:
   if opt == "-h" or opt == "--help":
      print (f'{sys.argv[0]} -a <attempts> -t <table>')
      sys.exit(0)
   elif opt in ("-a", "--attempts"):
       try:
           input_attempts = int(arg)
       except ValueError:
           print("Only numbers are allowed")
           sys.exit(2)
   elif opt in ("-t", "--table"):
       try:
           input_table = int(arg)
           if not 2 <= input_table <= 9:
               print("Tables (-t) allowed: [2 3 4 5 6 7 8 9]")
               sys.exit(2)
       except ValueError:
           print("Only numbers are allowed")
           sys.exit(2)

if input_table is not None:
    start_multiplicable = int(input_table)

if input_attempts is not None:
    attempts = int(input_attempts)

while test_question < attempts:
    if start_multiplicable != 0:
        multiplicable = start_multiplicable
        multiplier = random.choice(elementes)
    else:
        multiplicable = random.choice(elementes)
        multiplier = random.choice(elementes)

    if re_multiplicable is not None:
        multiplicable = re_multiplicable
        multiplier = re_multiplier
        re_multiplier = None 
        re_multiplicable = None
    else:
        string_number = str(multiplicable) + str(multiplier)
        if string_number in passed_questions:
            #print(f"Duplicate - {string_number}")
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

    passed_questions.append(string_number)
    test_question += 1

print(f"Wrong answers - {wrong_answers}")