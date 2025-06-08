#this is a treasure hunting game where you are given different options to choose from
#and the correct choices will lead you to the treasure! whereas the wrong choice will cause your death!

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#ask the direction in which the player wants to go
direction = input("Where do you want to go? Left or Right: ")
#if the player says right or Right, he gets lost and loses
if direction == 'right' or direction == 'Right':
    print("Opposite direction! You lose :(")
# if the player chooses left, then he proceeds further in game
elif direction == 'left' or direction == 'Left':
    #ask player if he wants to wait for boat or swim to the island
    choice = input("You're at a lake but there's no boat available right now, do you want to swim or wait? ")
    #if he chooses to swim, then sharks attack him and he dies
    if choice == 'swim' or choice == 'Swim':
        print("You got attacked by sharks :( Game Over...")
    #if he chooses to wait, a boat comes to him and takes him to the island and he proceeds further
    elif choice == 'wait' or choice == "Wait":
        print("Your arrived at the Island unharmed. There are three doors. Red,Yellow,Blue")
        #after player reaches the island, he is given the final choice to choose between the doors
        door = input("Which door do you want to enter? ")
        #if door color is red or blue, then player enters the lava room and dies
        if door == 'red' or door == 'Red' or door == 'Blue' or door == 'blue':
            print("The floor was Lava! Game Over :(")
        #if the door color is yellow, then he reaches the treasure room and wins!!
        elif door == 'yellow' or door == 'Yellow':
            #congratulations message for the user
            print("Congratulation!! You won the game!!!")
        #if the user entered any other door color, display invalid color message
        else: print("Invalid door color!")
    #if the user enters choice other than swim or wait, display invalid choice message
    else: print("Invalid choice!")
#if the user enters any other direction, display invalid direction message
else: print("Invalid direction")
