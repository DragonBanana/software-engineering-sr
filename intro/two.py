def two_sum(nums, target):
    # Dictionary to store numbers and their indices
    seen = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in seen:
            return [seen[complement], i]  # Return the indices
        
        # Store the current number with its index in the dictionary
        seen[num] = i
    
    # If no solution exists, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of numbers adding up to target:", result)