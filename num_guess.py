import random

min = 1
max = 10
go = "yes"
play_loop = True
play_again = "yes"

while play_loop == True:

    rand = int(random.randint(min, max))

    print("Guess a number between 1 and 10. Good Luck!")
    while go == "yes" or go == "y":
        guess = int(input("Guess a number: "))
        if guess == rand:
            print("CORRECT!")
        else:
            print("Incorrect. Guess again!")
            play_loop = input("Play again? ")