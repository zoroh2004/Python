#A small number guessing game where player has 8 guesses and has to guess the unknown number with given hints

import random #library/module to use random functions
#store a random number between 1 and 100 in num variable before start of game
num = random.randint(1,100)

print("Welcome to the number Guessing Game!")
tries = 8
#while loop which run while the tries lift are non-zero
while tries > 0:
    print(f"You have {tries} guesses")
    #stores the player's guess each time in the form of an integer
    guess = int(input("Take a Guess of the number"))
    #if the player guessed the number, congratulate and break
    if guess == num:
        print("Congratulations! You guessed the right number!")
        break
    #else if the guess is higher than the number, give player a hint that it's too high
    elif guess > num:
        print("Too High!")
    #else give hint that the guess is too high
    else:
        print("Too Low!")
    # decrement in the tries everytime the player guesses
    tries-=1

#if user used all tried and didn't guess, then the game is finished
if tries == 0:
    print("You are out of tries :(")