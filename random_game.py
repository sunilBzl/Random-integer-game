import random

clu = random.randint(0,100)
choice = 5

while choice > 0:
    user_input = int(input("Enter your number: "))

    if user_input == clu:
        print("Correct answer: ", clu)

    elif user_input > clu:
        print("Your number is greater.")

    else:
        print("your number is less") 

    choice -=1

print("Right answer is: ", clu)

