# The 'in' keyword helps us check if a value is present in a list, string, tuple, or set. 
# It's like asking Python, "Is this thing inside that group of things?" 
# If the answer is yes, it returns True. If not, it returns False.

friends = ["Jim", "Rick"]
family = ["Donna", "Robert", "Michelle"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("Hello, Friend!")
elif user_name in family:
    print("Hello family member!")
else:
    print("You're not my family!")
