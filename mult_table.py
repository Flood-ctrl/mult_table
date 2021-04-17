#!/usr/bin/env python3

import sys, getopt, random

elementes = (2, 3, 4, 5, 6, 7, 8, 9)
wrong_answers = 0
re_multiplicable = None
re_multiplier = None
start_multiplicable = int(0)
test_question = int(0)
attempts = int(10)
passed_questions = list()

def input_args():
   input_attempts = ''
   input_table = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <input_attempts> -o <input_table>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <input_attempts> -o <input_table>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         input_attempts = arg
      elif opt in ("-o", "--ofile"):
         input_table = arg
   print ('Input file is "'), input_attempts
   print ('Output file is "'), input_table


if start_multiplicable != 0:
    attempts = len(elementes)

if sys.argv[0] is not None:
    start_multiplicable = int(sys.argv[1])

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
            print(f"Duplicate - {string_number}")
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
#print(test_question)

#print(passed_questions)