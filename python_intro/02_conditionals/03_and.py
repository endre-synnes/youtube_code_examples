age_input = input()
min_age = 10
max_age = 18

# Typecasting the input to Integer
age = int(age_input)

# And - to old
if age <= max_age and age >= min_age:
    print("You are within the age group")
elif age > max_age:
    print("You are to old 👴")
else:
    print("You are to yong 👶")

""" Simplified version
# And - to old
if max_age > age > min_age:
    print("You are within the age group")
"""
