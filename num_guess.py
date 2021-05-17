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
            play_again = input("Play again? ")
    if play_again == "yes" or play_again == "y":
        play_loop = True
    else:
        play_loop = False
        else:
            print("Incorrect. Guess again!") 
  