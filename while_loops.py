# With a "while" loop, you set a condition at the beginning. 
# As long as the condition is true, the loop will keep running and repeating the code inside it. 
# You need to make sure that the condition eventually becomes false, otherwise, 
# the loop will go on forever, causing what we call an "infinite loop."

is_learning = True

while is_learning:
    print("You're Learning!")
    user_input = input("Are you still learning? ")
    is_learning = user_input == "yes"
