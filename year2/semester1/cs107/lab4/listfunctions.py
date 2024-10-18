# Fill in a correct implementation for each function.
# Define other functions if you think they make the
# assigned function easier to write or easier to read.

def max(elements):
    """This function returns the largest element in the given list."""
    return 0


def min(elements):
    return 0


def sum(elements):
    return 0


def average(elements):
    return elements

def midpoint(elements):
    return 0

def linear_search(elements, n):
    return False

def reverse(elements):
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
        (sum, [1, 2, 3], 6),
        (sum, [], 0),
        (sum, [-1, 0, 1], 0),
        (sum, [10000, 1000, 100, 10, 1], 11111),
        (max, [3, 2, 1, 2, 3], 3),
        (max, [-1, 4, -2, 10, 1, 5], 10),
        (min, [3, 2, 1, 2, 3], 1),
        (min, [-1, 4, -2, 10, 1, 5], -2),
        (linear_search, [1, 2, 3, 4, 5], 3, True),
        (linear_search, [-3, 12, 16, -6, 5, 9], 7, False),
        (average, [2, 3, 5, 7, 11], 5.6),
        (average, [2, 4, 6, 8, 10, 12], 7),
        (midpoint, [3, 2, 1, 2, 3], 1),
        (midpoint, [1, 2, 3, 4, 5, 6], 3.5),
        (reverse, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        (reverse, [10, 11, 12, 13, 14, 15], [15, 14, 13, 12, 11, 10])
    ]

    passed = 0
    failed = 0

    # Test each function.
    # Print a detailed error message whenever a function fails a test.
    for test in tests:
        f = (test[0])
        if f == linear_search:
            result = f(test[1], test[2])
            expected = test[3]
        else:
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
