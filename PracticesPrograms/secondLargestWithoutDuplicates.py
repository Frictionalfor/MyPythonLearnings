#Problem-Question

"""Write a function that returns the second largest unique number in a list.
Example:
Input:  [4, 1, 7, 3, 7]
Output: 4
(7 is largest, 4 is second largest)
Rules
Do not use sort()
Do it in one pass if possible
Handle duplicates
If no second largest exists, return None
"""

def second_largest(nums):
    if not nums:
        return None
    
    largest = None
    second_largest = None
    
    for num in nums:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
            
    return second_largest

# Test cases
print(second_largest([4, 1, 7, 3, 7]))
print(second_largest([1, 2, 3, 4, 5]))
print(second_largest([5, 5, 5]))
print(second_largest([]))
print(second_largest([10]))
print(second_largest([10, 20, 20, 30, 30, 40]))
