import random
import os

min = 1
max = 10
play_loop = "yes"

print("Guess a number between 1 and 10. Good Luck!")
while play_loop == "yes" or "y":
    rand = int(random.randint(min, max))
    guess = int(input("Guess a number: "))
    if guess == rand:
        print("CORRECT!")
        play_loop = input("Play Again? ")
        os.system("clear")
    else:
        print("Incorrect. Guess again!")
    if play_loop == "No" or play_loop == "n":
        print("GOODBYE!")
        break