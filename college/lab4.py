# Program to perform operations on tuples

t = (1, 2, 3, 4, 5)

print("First element of tuple:", t[0])
print("Second element of tuple:", t[1])

print("The tuple is:", t)

l = list(t)
print("Tuple converted into list:", l)

t2 = tuple(l)
print("List converted back into tuple:", t2)

del t
print("Tuple deleted")
