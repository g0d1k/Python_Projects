# A "for" loop is used when you want to repeat something a specific number of times or when you want to go 
# through a list of items one by one. Instead of setting a condition, 
# you give the loop a sequence or a collection to work with. 
# The loop will automatically go through each item in that sequence or collection 
# and run the code for each item.

students = [
    {"name": "Bobby", "grade": 90},
    {"name": "Sara", "grade": 87},
    {"name": "Nikki", "grade": 94},
]

for student in students:
    name = student["name"]
    grade = student["grade"]

print(f"{name} has a grade of {grade}.")