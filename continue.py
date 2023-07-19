# continue statement: When encountered within a loop, it immediately skips the rest 
# of the code inside the loop for the current iteration and moves on to the next 
# iteration. The loop's execution continues from the beginning, 
# excluding the remaining statements for that particular iteration. 

# Both break and continue statements provide you with control over the flow of your 
# loops, allowing you to selectively execute or skip certain 
# iterations based on specific conditions.


cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...!")
        continue
    print(f"This car is {status}")
    print("Ship new car to customer!")