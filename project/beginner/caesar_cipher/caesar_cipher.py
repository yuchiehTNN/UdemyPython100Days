alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    encrypted_result = []
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        result_index = letter_index + shift_amount
        while result_index > len(alphabet) - 1:
            result_index = result_index - len(alphabet) - 1
        encrypted_result.append(alphabet[result_index])
    return "".join(encrypted_result)


def decrypt(plain_text, shift_amount):
    encrypted_result = []
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        result_index = letter_index - shift_amount
        while result_index < 0:
            result_index = result_index + len(alphabet) - 1
        print(result_index)
        encrypted_result.append(alphabet[result_index])
    return "".join(encrypted_result)


def caesar(cipher_direction, plain_text, shift_amount):
    encrypted_result = []
    while shift_amount > len(alphabet):
        shift_amount = shift_amount % len(alphabet)
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        print(letter_index, shift_amount)
        result_index = letter_index + shift_amount
        if result_index > len(alphabet):
            result_index = result_index - len(alphabet)
        encrypted_result.append(alphabet[result_index])
    return "".join(encrypted_result)


try_again = "yes"
while try_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(plain_text=text, shift_amount=shift, cipher_direction=direction))
    try_again = input("Type 'yes' if you want to try again")

# if direction == "encode":
#     print(encrypt(text, shift))
# else:
#     print(decrypt(text, shift))
# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
