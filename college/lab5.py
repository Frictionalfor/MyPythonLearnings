# a) Create a set
numbers = {10, 20, 30, 40}
print("Initial Set:", numbers)

# b) Access elements of a set
print("\nAccessing elements using a loop:")
for item in numbers:
    print(item)

print("\nChecking membership:")
print("20 in numbers?", 20 in numbers)

# c) Update a set
# Adding elements
numbers.add(50)
numbers.update([60, 70])
print("\nAfter adding elements:", numbers)

# Removing elements
numbers.remove(20)      # removes a specific element
print("After removing elements:", numbers)
numbers.discard(10)     # removes element if present (no error if absent)
print("After removing elements:", numbers)
numbers.pop()           # removes a random element
print("After removing elements:", numbers)

# d) Delete a set
del numbers
print("\nSet deleted successfully")
