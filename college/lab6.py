"""
6.Implement a python program to perform following operations on the Dictionary:
a)	Create a Dictionary
b)	 Access Dictionary
c)	 Update Dictionary
d)	 Delete Dictionary	
"""

# a) Create a Dictionary
my_dict = {
    "name": "Happy",
    "age": 17,
    "city": "New York"
}
print("Dictionary created:", my_dict)   

# b) Access Dictionary
print("Name:", my_dict["name"])  # Accessing value using key

# c) Update Dictionary
my_dict["age"] = 18  
print("Updated Dictionary:", my_dict)   

# d) Delete Dictionary
del my_dict["city"]
print("Dictionary after deletion:", my_dict)

#using copy() method to create a copy of the dictionary
my_dict_copy = my_dict.copy()
print("Copy of the Dictionary:", my_dict_copy)

#using fromkeys() method to create a new dictionary with specified keys and values
keys = ["name", "age", "city"]
values = ["Happy2", 20, "Vice City"]
new_dict = dict.fromkeys(keys, values)
print("New Dictionary created using fromkeys():", new_dict)

#using get() method to access value of a key
print("Name using get():", my_dict.get("name"))

#using items() method to get a view object of the dictionary's key-value pairs
print("Dictionary items:", my_dict.items())

#using keys() method to get a view object of the dictionary's keys
print("Dictionary keys:", my_dict.keys())

#using pop() method to remove a key-value pair from the dictionary
removed_value = my_dict.pop("age")
print("Removed value:", removed_value)
print("Dictionary after popping:", my_dict)

#using popitem() method to remove the last inserted key-value pair from the dictionary
removed_item = my_dict.popitem()
print("Removed item:", removed_item)
print("Dictionary after popping item:", my_dict)

#using setdefault() method to get the value of a key, and if the key does not exist, insert the key with a specified value
default_value = my_dict.setdefault("country", "India")
print("Default value for 'country':", default_value)
print("Dictionary after setdefault():", my_dict)

#using update() method to update the dictionary with another dictionary
update_dict = {"name": "Happy3", "age": 19}
my_dict.update(update_dict)
print("Dictionary after update:", my_dict)

#using values() method to get a view object of the dictionary's values
print("Dictionary values:", my_dict.values())

#using clear() method to delete all items from the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)