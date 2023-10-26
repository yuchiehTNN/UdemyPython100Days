import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages

answer = random.choice(word_list)

correctCount = 0
currentGuess = []
life = 0

print(hangman_art.logo)

for i in range(1, len(answer) + 1):
    currentGuess.append("_")

while correctCount != len(answer) and life < 6:
    user_input = input("Guess a letter: ").lower()
    count = 0
    temp = correctCount
    for letter in answer:
        if user_input == letter:
            correctCount += 1
            currentGuess[count] = letter
        count += 1
    if temp == correctCount:
        life += 1
        print("Wrong, loose one life")
        print(stages[life])
    print(currentGuess)


print("Game Over")
