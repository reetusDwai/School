def square():
    """
    blah blah blah
    """
    num = int(input("Please enter a positive integer: "))
    if num <= 1:
        print("Error: the given number should be greater than 1.")
        return
    i = 2
    i_squared = i ** 2
    while (i_squared <= num):
        if i_squared % 2 == 0:
            print(i_squared)
        i += 1
        i_squared = i ** 2


if __name__ == "__main__":
    square()
