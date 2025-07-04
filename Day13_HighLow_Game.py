#this program simulates a game where the player guesses the celebrity whose followers are more out of the two options given
#if he guesses right, he gets an increment in score, the game continues as long as player is guessing right

#importing a list of dictionaries containing celebrities data from other .py file
from Day13_HighLow_Game_Data import data
#importing random module to use random functions
import random

#two logos to print on the console
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (___ ) 
|___/____/
"""


print(logo)
current_score = 0   #a variable to keep track of the player score

#description given in the docstring
def random_create():
    """a function that returns a random index (dictionary) from the data list"""
    return random.choice(data)
#description given in the docstring
def main_board(c1,c2):
    """a functions which is used to print the compare messages from the data of the two dictionaries"""
    print("Compare A: " + c1['name'] + ", " + c1['description'] + ", " + "from " +  c1['country'])
    print(vs)
    print("Against B: " + c2['name'] + ", " + c2['description'] + ", " + "from " +  c2['country'])

correct = True  #a variable which is used for while loop iterations
celeb1 = random_create() #variable which stores the return value of random create as first celeb to compare
celeb2 = random_create() #variable which stores the return value of random create as first celeb to compare

#while correct == True
while correct:
    #function call to print the main board
     main_board(celeb1, celeb2)
    #ask the user for the choice he wants and convert it to lowercase for ease
     choice = input("Who has more Followers? Type 'A' or 'B': ").lower()
    #if the user's choice is A and the celebrity corresponding to A has more followers than B
     if choice == 'a' and celeb1['follower_count'] > celeb2['follower_count']:
         #increment 1 in score
         current_score += 1
         # save celeb2 in celeb1
         celeb1 = celeb2
         #using this loop to make sure both celebrities are different
         while celeb1 == celeb2:
             # take another random in celeb2
             celeb2 = random_create()
         print("\n"*50)     #to make it seem like a new page on console
         print(f"You're Right! Current score: {current_score}")
    #else if user's choice is B and the celebrity corresponding to A has more followers than B
     elif choice == 'b' and celeb2['follower_count'] > celeb1['follower_count']:
         #increment 1 in score
         current_score += 1
         # save celeb2 in celeb1
         celeb1 = celeb2
         #using this loop to make sure both celebrities are different
         while celeb1 == celeb2:
             # take another random in celeb2
             celeb2 = random_create()
         print("\n"*50) #to make it seem like a new page on console
         print(f"You're Right! Current score: {current_score}")
     else:
         #else make correct variable false to terminate the while loop
         correct = False
print("\n"*50)  #to make it seem like a new page on console
#final message when user gets the wrong answer
print(f"Sorry That's Wrong, Final score: {current_score}")
