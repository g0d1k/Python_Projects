# 'break' statement: When encountered within a loop, it immediately terminates the loop's 
# execution and transfers control to the next statement after the loop. 
# This means that the remaining iterations of the loop are skipped, 
# and the program resumes execution outside the loop.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stop production line!")
        break
