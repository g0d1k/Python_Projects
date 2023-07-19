# Iterating Over Other Objects:
# In Python, many objects are iterable, meaning you can iterate over their elements using a loop. 
# For example, you can iterate over elements in a list, characters in a string, 
# key-value pairs in a dictionary, etc. The for loop is typically used to iterate over these objects.

friend_ages = {"Jim": 43, "Rick": 76, "Bob": 54, "John": 63}

for name, age in friend_ages.items():

    print(f"{name} is {age} years old!")
