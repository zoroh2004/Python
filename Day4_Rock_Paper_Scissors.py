#this is a rock paper scissors game, where the user tells
#what shape he wants to make and the computer chooses one shape
#randomly, and then the game tell who won XD
import random #this library/module is used for random functions

#rock shape 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#paper shape
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#scissors shape
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#user input is stored in player_choice after converting it to int
player_choice = int(input("Enter 0 for rock, 1 for papers, and 2 for scissors: "))
#computer choice is chosen from a list 3 elements, rock paper and scissors
#it can also be done with the randint function by linking number with shapes
computer_choice = random.choice(["Rock", "Paper", "Scissors"])

#The following code prints the shapes of both the user and the
#computer and tell if the user wins or the computer or if it's a draw
#if player chose rock
if player_choice == 0:
    #if player chose rock and:
    #computer chose rock,then draw
    if computer_choice == "Rock":
        print("Your choice:\n", rock, "\n")
        print("Computer's choice:\n", rock, "\n")
        print("Draw")
    #computer chose paper, then player loses
    elif computer_choice == "Paper":
        print("Your choice:\n", rock, "\n")
        print("Computer's choice:\n", paper, "\n")
        print("you Lose")
    #computer chose scissors, player wins
    elif computer_choice == "Scissors":
        print("Your choice:\n", rock, "\n")
        print("Computer's choice:\n", scissors, "\n")
        print("You Win")
#if player chose paper
elif player_choice == 1:
    #if player chose paper and:
    #computer chose rock, then player wins
    if computer_choice == "Rock":
        print("Your choice:\n", paper, "\n")
        print("Computer's choice:\n", rock, "\n")
        print("You Win")
    #computer chose paper, then draw
    elif computer_choice == "Paper":
        print("Your choice:\n", paper, "\n")
        print("Computer's choice:\n", paper, "\n")
        print("Draw")
    #computer chose scissors, then player loses
    elif computer_choice == "Scissors":
        print("Your choice:\n", paper, "\n")
        print("Computer's choice:\n", scissors, "\n")
        print("You Lose")
#if player chooses scissors
elif player_choice == 2:
    #if player chooses scissors and:
    #computer chooses rock, then player loses
    if computer_choice == "Rock":
        print("Your choice:\n", scissors, "\n")
        print("Computer's choice:\n", rock, "\n")
        print("You Lose")
    #computer chooses paper, then player wins
    elif computer_choice == "Paper":
        print("Your choice:\n", scissors, "\n")
        print("Computer's choice:\n", paper, "\n")
        print("you Win")
        #computer chooses scissors, then draw
    elif computer_choice == "Scissors":
        print("Your choice:\n", scissors, "\n")
        print("Computer's choice:\n", scissors, "\n")
        print("Draw")
#any choice other than the given 3, then invalid
else:
    print("Invalid choice!!!")