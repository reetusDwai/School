# Complete the comments below
# Name: Kalem Smith
# Assignment: Lab 2, Exercise 1: pay.py
# Date: 9/15/24

employee_type = int(input("""Enter the type of employee::
(1: Manager; 2: Hourly worker; 3: Commission Worker; 4: Pieceworker) : """))

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
