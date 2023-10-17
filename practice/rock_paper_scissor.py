import random

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. \n")
)

computer_choice = random.randint(0, 2)

# just many many conditions...

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
