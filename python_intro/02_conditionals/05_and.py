max_age_student = 36
title = "student"

my_age = 20
my_title = "student"

# ex 1
if my_age < max_age_student and my_title == title:
    print("You can purchase student tickets!")
else:
    print("You have to a student and youger than 36 years old to get cheap tickets.")


# ex 2
if my_age < max_age_student and my_title == title:
    print("You can purchase student tickets!")
elif my_title == title:
    print("Students your age does not get cheap tickets :(")
else:
    print("You have to a student to get cheap tickets.")
