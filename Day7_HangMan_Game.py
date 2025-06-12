#This program that demonstrates a hangman game, with a specified number of lives
#and visual representation of hang-man XD

import random #a library to use random functions

#ASCII to print hanged man at on each live count
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#a list of all word used in the game
word_list = ["apple", "orange", "pineapple", "banana", "mango", "strawberry", "blueberry", "watermelon"]

#total lives
lives = 6

already_guessed = []
#random function to choose a random word from the list
chosen_word = random.choice(word_list)

#the word guessed by the player
guessed_word = ""

#a placeholder to keep the list of current array of guessed and unguessed index
placeholder = []

#loop which iterated till i is in within chosen_word list
for i in chosen_word:
    #append _ in the list to show number of total words
    placeholder.append("_")
    guessed_word+="_"

print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-WELCOME TO THE HANGMAN GAME-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-HINT: The word is a Fruit-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
#print the guessed word to initially show dashes for count of characters
print(guessed_word)

#runs in a loop until the user guesses the complete word
while guessed_word != chosen_word:
    #a boolean variable to check if the guessed character is correct
    correct = False

    #print the hanged man corresponding to the current live
    print(stages[lives])
    #if the user used all his lives and still didn't guess right
    if lives == 0:
        #user looses and the game ends by using break statement
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-You Lose!-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        break

    #else, guess a letter
    guess = input("Guess A Letter: ")

    #convert the letter into lower case to compare
    guess = guess.lower()

    #a flag which is used to check all the "already used" letters
    already_guessed_flag = False

    #a loop which iterates while i is within length of already_guessed list
    for i in range(len(already_guessed)):
        #if the player's guess is anywhere in the list of guessed,
        # then make the already_guessed_flag = true
        if guess == already_guessed[i]:
            already_guessed_flag = True

    #if the player's guess was withing the list, then print the message
    if already_guessed_flag == True:
        print(f"You have already guessed the letter {guess}")

    # else a loop which runs the length of chosen_word
    else:

        for i in range(0,len(chosen_word)):
            #if the guessed character is equal to
            #any character from the chosen_word, then add that character to
            #the corresponding index in the placeholder list
            if chosen_word[i] == guess:
                placeholder[i] = guess
                #correct is turned to true, because of matched character
                correct = True
                already_guessed.append(guess)

        #if the character didn't match even one in the chosen_word,
        # then decrement lives by 1 and append the guess in the already_guessed list
        if correct == False:
            lives -= 1
            already_guessed.append(guess)

    #make the guessed word null
    guessed_word = ""

    #add the new guessed string from placeholder to guessed_word
    for i in range(len(chosen_word)):
        guessed_word+=placeholder[i]
        #print the guessed word for ease of user

    print(guessed_word)
#if the loop ended and user guessed the word, he wins.
# here this if statement is used because the loop can also break if user loses
if guessed_word == chosen_word:
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-You win!-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

