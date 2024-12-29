# Using built-in
def find_max(nums):
    if not nums:
        raise ValueError("List is empty")
    return max(nums)

# Using iteration
def find_max(nums):
    if not nums:
        raise ValueError("List is empty")
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

# Using sorting
def find_max(nums):
    if not nums:
        raise ValueError("List is empty")
    return sorted(nums)[-1]

# Not handling empty list
def find_max(nums):
    return max(nums)  # No check for an empty list

# Incorrect Comparison
def find_max(nums):
    if not nums:
        raise ValueError("List is empty")
    max_val = 0  # Incorrect initialization
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val

# Return minimum
def find_max(nums):
    if not nums:
        raise ValueError("List is empty")
    max_val = nums[0]
    for num in nums:
        if num < max_val:  # Incorrect comparison
            max_val = num
    return max_val

test_cases = [
    ([1, 2, 3, 4, 5], 5),
    ([-1, -5, -10], -1),
    ([5], 5),
    ([], ValueError),
    ([10, 20, 30], 30),
]

for i, (input_list, expected) in enumerate(test_cases, 1):
    try:
        result = find_max(input_list)
        assert result == expected, f"Test Case {i} Failed: Expected {expected}, Got {result}"
    except ValueError:
        assert expected == ValueError, f"Test Case {i} Failed: Expected ValueError, Got {result}"
    print(f"Test Case {i}: Passed")