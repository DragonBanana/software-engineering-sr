# iterative
def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# recursive
def is_prime(n, divisor=None):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    if divisor is None:
        divisor = int(n ** 0.5)
    if divisor < 2:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor - 1)

# using sieve of eratosthenes
class PrimeChecker:
    def __init__(self, max_value=1000):
        self.max_value = max_value
        self.sieve = self._generate_sieve(max_value)

    def _generate_sieve(self, max_value):
        is_prime = [True] * (max_value + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_value ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_value + 1, i):
                    is_prime[j] = False
        return is_prime

    def is_prime(self, n):
        if not isinstance(n, int):
            raise TypeError("Input must be an integer")
        if n < 0 or n > self.max_value:
            return False
        return self.sieve[n]

# incorrect boundary check
def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# divisibility by 2
def is_prime(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    return True

# missing type check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

test_cases = [
    (2, True),
    (15, False),
    (0, False),
    (13, True),
    ("17", TypeError),
    (-7, False),
]

for i, (input_val, expected) in enumerate(test_cases, 1):
    try:
        result = is_prime(input_val)
        assert result == expected, f"Test Case {i} Failed: Expected {expected}, Got {result}"
    except TypeError:
        assert expected == TypeError, f"Test Case {i} Failed: Expected TypeError, Got {result}"
    print(f"Test Case {i}: Passed")