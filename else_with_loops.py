# In Python, the else statement can be used in conjunction with loops to specify a 
# block of code that should be executed when the loop has completed all iterations 
# without encountering a break statement. The else block is 
# optional and follows the loop block.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stop production line!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer.")
else:
    print("All cars built successfully!")
