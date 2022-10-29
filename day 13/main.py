# Describe the problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
# my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dice_num = randint(0, 5)
# print(dice_num)

# Play computer
year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
    # print("You are a millenial.")
# elif year >= 1994:
    # print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

