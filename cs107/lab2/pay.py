# Complete the comments below
# Name: Kalem Smith
# Assignment: Lab 2, Exercise 1: pay.py
# Date: 9/15/24

"""
A company pays its employees as managers (who receive a fixed weekly salary), hourly workers
(who receive a fixed hourly wage for up to the first 40 hours they work and "time-and-a-half"-
i.e., 1.5 times their hourly wage for overtime hours worked), commission workers (who receive
$250 plus 5.7% of their gross weekly sales), or pieceworkers (who receive a fixed amount of
money for each of the items that they produce–each pieceworker within this company works
on only one item type). Write a program that computes the weekly pay for each employee.
Each type of employee has its own pay code: Managers have paycode 1, hourly workers have
code 2, commission workers have code 3, and pieceworkers have code 4.
"""

employee_type = int(input("Enter the type of employee::\n(1: Manager; 2: Hourly worker; 3: Commission Worker; 4: Pieceworker) : "))

match employee_type:
    case 1:
        weekly_salary = int(input("Enter weekly salary: "))
        print("The managers pay is ", weekly_salary)
    case 2:
        hourly_salary = int(input("Enter hourly salary: "))
        hours_worked = int(input("Enter the total hours worked: "))
        if hours_worked > 40:
            overtime = hours_worked % 40
            pay = 40 * hourly_salary + overtime * hourly_salary * 1.5
        else:
            pay = hours_worked * hourly_salary
        print("The worker's pay is ", pay)
    case 3:
        gross_weekly_sales = int(input("Enter gross weekly sales: "))
        pay = 250 + 0.057 * gross_weekly_sales
        print("The commision worker's pay is ", pay)
    case 4:
        pieces_made = int(input("Enter number of pieces made: "))
        wage_per_piece = int(input("Enter the wage per piece: "))
        pay = pieces_made * wage_per_piece
        print("The workers pay is ", pay)
    case _:
        print("""Error, the given employee code is not valid.
Valid codes are:
1: Manager; 2: Hourly worker; 3: Commission Worker; 4: Pieceworker""")
