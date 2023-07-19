import time
import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.title("Welcome to your MAD-LIB!")

label = tk.Label(root, text="Are you ready to laugh?", fg=('black'), font=('Arial', 18))

root.mainloop() 

print("Welcome to your MAD LIB!")
time.sleep(3)

color = input("Enter a color: ")
print(f"You picked {color}!")
time.sleep(3)

adjective = input("Enter an adjective: ")
print(f"You picked {adjective}!")
time.sleep(3)

thetime = input("Enter a time of day: ")
print(f"You picked {thetime}!")
time.sleep(3)

adjective2 = input("Enter another adjective: ")
print(f"You picked {adjective2}!")
time.sleep(3)

place = input("Enter a place: ")
print(f"You picked {place}!")
time.sleep(3)

food = input("Enter a food: ")
print(f"You picked {food}!")
time.sleep(3)

food2 = input("Enter another food: ")
print(f"You picked {food2}!")
time.sleep(3)

verb = input("Enter a verb: ")
print(f"You picked {verb}!")
time.sleep(3)

noun = input("Enter a noun: ")
print(f"You picked {noun}!")
time.sleep(3)

number = input("And finally, enter a number: ")
print(f"You picked {number}!")
time.sleep(3)

print("Are you ready to laugh?!")
time.sleep(3)

print(f"Bats are so cool! They are {color}, {adjective} animals which have wings.") 
time.sleep(5)

print(f"They like to fly around at {time} which makes some people scared of them.")
time.sleep(5)

print(f"But bats are {adjective2}, and they don't want to hurt people. I have a pet bat that lives in {place}.")
time.sleep(5)

print(f"I like to feed him {food} and {food2}. He likes to {verb}. I am his favorite person, but he also likes {noun}.")
time.sleep(5)

print(f"I want to convince my parents to get me {number} more bats.")
time.sleep(5)

print("Thanks for playing!")
