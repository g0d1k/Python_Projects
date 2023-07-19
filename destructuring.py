# Destructuring is a way to extract values from different data structures like 
# lists, tuples, and dictionaries, and assign them to variables in a single line. 
# It allows you to unpack and access specific elements without writing lengthy code.

friends = [("Jim", 43), ("Rick", 76), ("Bob", 54), ("John", 63)]
for name, age in friends:
    print(f"{name} is {age} years old!")

