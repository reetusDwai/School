# Fill in a correct implementation for each function.
# Define other functions if you think they make the
# assigned function easier to write or easier to read.

def odds(elements):
    return elements


def evens(elements):
    return elements


def every_other(elements):
    return elements


def every_other_odd(elements):
    return elements


def every_other_even(elements):
    return elements

# -----------------------------------------------------------------------------
# Do not alter code below this point
def run_tests():
    """This function tests each function defined in this module."""

    # A single test is a tuple containing the function
    # which is being tested, a sample input, and the correct output.
    # Tests should be written using the unittest or pytest modules,
    # but, hopefully, this code is easier to understand.
    tests = [
        # This test will be used to check if `sum([1, 2, 3])` is `6`.
        (odds, [1, 2, 3, 4], [1, 3]),
        (odds, [1, 100, 45, 23, 10, 2, 4, 13], [1, 45, 23, 13]),
        (odds, [], []),
        (evens, [1, 2, 3, 4], [2, 4]),
        (evens, [1, 100, 45, 23, 10, 2, 4, 13], [100, 10, 2, 4]),
        (evens, [], []),
        (every_other, [1, 2, 3, 4], [1, 3]),
        (every_other, [1, 100, 45, 23, 10, 2, 4, 13], [1, 45, 10, 4]),
        (every_other, [], []),
        (every_other_odd, [1, 2, 3, 4], [1]),
        (every_other_odd, [1, 100, 45, 23, 10, 2, 4, 13], [1, 23]),
        (every_other_odd, [], []),
        (every_other_even, [1, 2, 3, 4], [2]),
        (every_other_even, [1, 100, 45, 23, 10, 2, 4, 13], [100, 2]),
        (every_other_even, [], []),
    ]

    passed = 0
    failed = 0

    # Test each function.
    # Print a detailed error message whenever a function fails a test.
    for test in tests:
        f = (test[0])
        result = f(test[1])
        expected = test[2]
        if result == expected:
            passed += 1
        else:
            failed += 1

            # f.__name__ is the function's name
            # for example, evens.__name__ is the string "evens"
            print("Function '{}' given argument {}".format(f.__name__, test[1]))
            print("Expected {}, but returned {}".format(expected, result))
    print("\nPassed {} out of {} tests.".format(passed, passed + failed))


if __name__ == "__main__":
    run_tests()
