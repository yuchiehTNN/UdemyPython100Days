import random

# print(random.randint(1, 10))
# print(random.random() * 5)

nameString = input("Give me everybody's names, seperated by a comma \n")
nameArr = nameString.split(", ")
randomInteger = random.randint(0, len(nameArr) - 1)
print(f"{nameArr[randomInteger]} is going to pay")

print(random.choice(nameArr))
