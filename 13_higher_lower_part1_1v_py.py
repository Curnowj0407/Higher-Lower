import random

cpu_num = random.randint(1,100)
guess = int(input("enter a number between 1-100:"))

while guess != cpu_num:
    guess = int(input("enter a number between 1-100:"))
    if guess > cpu_num:
        print("too high!")
    elif guess < cpu_num:
        print("too low!")
    else:
        print("well done!")