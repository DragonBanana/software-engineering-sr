# String slicing
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # Remove spaces and punctuation, convert to lowercase
    return cleaned == cleaned[::-1]

# Using two pointers
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # Remove spaces and punctuation, convert to lowercase
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

# Using a stack
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # Remove spaces and punctuation, convert to lowercase
    stack = list(cleaned)  # Push all characters to the stack
    reversed_str = ''.join(stack.pop() for _ in range(len(stack)))  # Pop characters to create reversed string
    return cleaned == reversed_str

# Incorrect comparison
def is_palindrome(s):
    return s == s[::-1]  # Does not clean or normalize the input

# Case sensitive issue
def is_palindrome(s):
    cleaned = ''.join(c for c in s if c.isalnum())  # Removes spaces and punctuation but ignores case
    return cleaned == cleaned[::-1]

# Incorrect indexing
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # Properly cleans the input
    left, right = 0, len(cleaned) - 1
    while left <= right:  # Off-by-one error; should be while left < right
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

test_cases = [
    ("radar", True),
    ("hello", False),
    ("A man, a plan, a canal: Panama", True),
    ("", True),
    ("Was it a car or a cat I saw?", True),
]

for i, (input_str, expected) in enumerate(test_cases, 1):
    print(f"Test Case {i}: {is_palindrome(input_str) == expected}")

test_cases = [
    ("radar", True),
    ("hello", False),
    ("A man, a plan, a canal: Panama", True),
    ("Radar", True),
    ("abcba", True),
]

for i, (input_str, expected) in enumerate(test_cases, 1):
    print(f"Test Case {i}: {is_palindrome(input_str) == expected}")