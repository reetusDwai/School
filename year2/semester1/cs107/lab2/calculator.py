# Complete the comments below
# Name: Kalem Smith
# Assignment: Lab 2, Exercise 2: calculator.py
# Date: 9/15/24

import math

num = float(input("Enter a number to use: "))
operation = input("Which operation? sqrt (s), arcsin (a), arccos (c), arctan (t): ")

match operation:
    case 's':
        if num > 0:
            ans = math.sqrt(num)
            print("The square root of the input is\n", ans)
        else:
            print("Input should be greater than 0")
    case 'a':
        if -1 <= num <= 1:
            ans = math.asin(num)
            print("The arcsine of the input is\n", ans)
        else:
            print("Input should be between -1 and 1")
    case 'c':
        if -1 <= num <= 1:
            ans = math.acos(num)
            print("The arccos of the input is\n", ans)
        else:
            print("Input should be between -1 and 1")
    case 't':
        ans = math.atan(num)
        print("The arctangent of the input is\n", ans)
    case _:
        print("Not a valid operation")
