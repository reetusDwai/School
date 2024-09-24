num = int(input("Enter a number: "))
if (num <= 0):
    print("Not a positive number!")
else:
    i = 1
    while i <= num:
        print("{} {}{}".format(i, ("Fizz" if i % 3 == 0 else ""), ("Buzz" if i % 5 == 0 else "")))
        i += 1
