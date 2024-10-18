# Complete the comments below
# Name: Kalem Smith
# Assignment: Lab 1, Exercise 2: mean.py
# Date: 8/30/24
# List any issues you had with this lab

# Write a program that accepts 10 floating point numbers from the user and prints the running
# average after each number is entered.

sum = 0
count = 0
running_avg = 0

for i in range(10):
    num = int(input("Enter number: "))
    sum += num
    count += 1
    running_avg = sum / count
    print("Running Average: ", running_avg)


