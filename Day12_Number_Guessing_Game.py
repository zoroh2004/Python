# a number guessing game, where i used some emojis and used constant global variables
# in python  we cannot define constant variables like c++ etc, but what we can do is write the
# variable names in uppercase, so that we (developer) know that it is a constant, and we shouldn't change it

#logo to print at the top
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

import random  # a module to use random functions

EASY_LEVEL_TRIES = 10  # constant global variable to use for easy level game
HARD_LEVEL_TRIES = 5  # constant global variable to use for hard level game


def difficulty():
    choice = 0
    while choice != 1 and choice != 2:
        choice = int(input("Press 1 to play easy mode 🟢 and 2 to play hard mode🔴: "))
        if choice == 1:
            return EASY_LEVEL_TRIES
        elif choice == 2:
            return HARD_LEVEL_TRIES
        else:
            print("Enter a valid choice!⚠️")


# a function for the functionality of the guess game
def guess_game(t):
    # taking a random number in 1-100 and storing it in the number variable
    number = random.randint(1, 100)
    # while the number of tries are not zero
    while t > 0:
        print(f"You have {t} tries left⌛...")
        # take the user guess, convert it into integer, and store it in the guess variable
        guess = int(input("Guess a number between 1 and 100❓ "))
        # if the user guesses the actual number, he wins!
        if guess == number:
            print("Congrats, you guessed the number🥳!")
            # break statement so that the loop doesn't run again because it runs until tries are not zero
            break
        # else if the user guesses a number lower than the actual number, print a too low message
        elif guess < number:
            print("Too low🪫!")
            t -= 1  # decrement in the number of tries for wrong guess
        # else if the user guesses a number higher than the actual number, print a too high message
        elif guess > number:
            print("Too high🔋!")
            t -= 1  # decrement in the number of tries for wrong guess
    # after the loop finishes, if tries are 0, then the user lost, so display the correct answer to him
    if t == 0:
        print(f"You lost 😢. The correct answer was {number}!")


# welcome message
print(logo)
print("Welcome to the Number Guessing Game🎮!")

# function call, with the tries as the return value of the difficulty() function
guess_game(difficulty())
