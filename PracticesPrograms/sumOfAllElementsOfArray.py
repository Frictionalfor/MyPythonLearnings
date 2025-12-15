#This file consist of a problem's solution which is Sum of all elements of an array.

def sum_of_array(arr):
    """
    This function takes an array of numbers as input and returns the sum of all its elements.
    
    Parameters:
    arr (list): A list of numerical values.
    
    Returns:
    int/float: The sum of all elements in the array.
    """
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

# Example usage:

print("Enter the number of elements in the array:")
sizeOfArray = int(input())
array = []
print("Enter the elements of the array:")
for _ in range(sizeOfArray):
    element = float(input())
    array.append(element)  

result = sum_of_array(array)
print("The sum of all elements in the array is:", result)