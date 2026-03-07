#Problem-Question
"""Return the k-th largest element in a list.
Example:
Input:  [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Now you need:
Either sorting
Or heap
Or QuickSelect"""

def kth_largest(nums, k):
    if k <= 0 or k > len(nums):
        return None
    
    largest = None
    
    for _ in range(k):
        largest = max(nums)
        nums.remove(largest)
    
    return largest

# Test cases
print(kth_largest([3, 2, 1, 5, 6, 4], 2))  
print(kth_largest([3, 2, 1, 5, 6, 4], 1))  
print(kth_largest([3, 2, 1, 5, 6, 4], 3))  
print(kth_largest([3, 2, 1, 5, 6, 4], 6))  
print(kth_largest([3, 2, 1, 5, 6, 4], 7))  
print(kth_largest([], 1))
