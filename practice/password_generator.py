import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

passwordList = []
for ln in range(1, nr_letters + 1):
    passwordList.append(random.choice(letters))
for ls in range(1, nr_symbols + 1):
    passwordList.append(random.choice(symbols))
for ln in range(1, nr_numbers + 1):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)

password = ""
for char in passwordList:
    password += char

print(password)
