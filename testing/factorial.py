# recursive
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# iterative
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# math library
import math

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return math.factorial(n)

# incorrect base case
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    return n * factorial(n - 1)  # No base case

# handle only positive
def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):  # Starts from 1, incorrect for n == 0
        result *= i
    return result

# does not raise error for negative numbers
def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Does not validate negative input
        result *= i
    return result

test_cases = [
    (5, 120),
    (0, 1),
    (1, 1),
    (-5, ValueError),
    (10, 3628800),
]

for i, (input_val, expected) in enumerate(test_cases, 1):
    try:
        result = factorial(input_val)
        assert result == expected, f"Test Case {i} Failed: Expected {expected}, Got {result}"
    except ValueError:
        assert expected == ValueError, f"Test Case {i} Failed: Expected ValueError, Got {result}"
    print(f"Test Case {i}: Passed")