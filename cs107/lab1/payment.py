# Complete the comments below
# Name: Kalem Smith
# Assignment: Lab 1, Exercise 1: payment.py
# Date: 8/30/24
# List any issues you had with this lab

# Write a program that asks the user to enter a U.S. dollar amount and then shows how to pay
# the ammount using the smallest number of $20, $10, $5, and $1 dollar bills. Store the given
# number as an ineger. The results will also be stored as integers

starting_amount = input("Enter a dollar ammount: ")
starting_amount = int(starting_amount)

amount_20s = starting_amount // 20
remainder = starting_amount % 20
print("$20 bills: ", amount_20s)

amount_10s = remainder // 10
remainder %= 10
print("$10 bills: ", amount_10s)

amount_5s = remainder // 5
remainder %= 5
print("$5 bills: ", amount_5s)

amount_1s = remainder // 1
remainder %= 1
print("$1 bills: ", amount_1s)
