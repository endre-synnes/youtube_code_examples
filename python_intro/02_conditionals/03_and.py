min_age = 10
max_age = 18

age = 8

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
