# Booleans in Python are a fundamental data type that represent only two possible values: 
# True or False. Booleans are used to make decisions and control the flow of a program.

# Think of booleans as a way to answer yes-or-no questions. For example, you might ask, 
# "Is it raining outside?" The answer can be either True (yes, it is raining) or False 
# (no, it is not raining). In Python, we use booleans to represent these types of logical conditions.

name = input("Enter your name: ")

print(bool(name))

if name:
    print("Thank you for entering your name!")

else:
    print("You need to enter a name fucktard!")
    