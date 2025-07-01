#this code simulates the TicTacToe Game

xScore = 0   #a variable to store the number of wins by player of X
oScore = 0   # a variable to store the number of wins by player of O

#Function to print the wins of each player
def printScore():
    #a docstring used to display information about the function when cursor is hovered on the function name
    """Functions to print the number of wins of each player"""
    #using global variables
    global xScore, oScore
    print(f"SCORE:   X = {xScore}, O = {oScore} ")

#a function used to display the TicTacToe board
def display_board():
    #docstring to display info about the function when hovering the cursor on function name
    """A user-defined function to display the board"""
    n=0     #a variable used in the nested loop for printing
    for i in range(3):
        print(" | ",end="")
        for j in range(n,n+3):
            print(pattern[j] + " | ",end=" ")
        n+=3
        print()
        print(" - - - - - - - -")

#boolean function used for checking if there is any empty block left in the board
def isEmpty():
    #docstring to display info about the function when hovering the cursor on function name
    """Checks if the board is empty"""
    for i in pattern:
        if i != 'X' and i != 'O':
            return True     #return true if empty place
    return False     #return false if no empty space

#a function used to check if any pattern of win is made by the sign (X or O)
def checkWin(sign):
    #dosctring to display info when hovering the cursor on function name
    """Checks if the sign given as parameter won the tictactoe game"""
    #a nested list/ 2D list with pre-defined win patterns
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]
    ]
    #a for loop to check if any combination is made for the sign given in parameter
    for combo in win_combinations:
        if pattern[combo[0]] == pattern[combo[1]] == pattern[combo[2]] == sign:
            return True     #return true if made
    return False    #return false if not made

playAgain = True    #a boolean variable made to check if the user wants to play again or not

#loop runs until user wants to play the game

while playAgain:
    #a list of numbers for each block in the board
    pattern = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #loop runs while there is an empty space left in the board
    printScore()  # print the score
    while isEmpty():

        display_board()    #print the board
        valid = False    #boolean variable to ask for input until valid index is entered

        while not valid:
            index = int(input("Enter index for X (1-9): ")) -1    #-1 to get the index of the list
            #a condition to check if the entered index is valid
            if index in range(9) and pattern[index] != 'X' and pattern[index] != 'O':
                valid = True
            else:
                print("Enter a valid Index")

        #make that index 'X' in the list, which was entered by the player
        pattern[index] = 'X'

        #check for a win after each input
        if checkWin("X"):
            #if user won, then print a winner message and break the inner while loop
            print("Game Over. X wins!")
            break

        #If the board is full, break the inner while loop
        if not isEmpty():
            break

        valid = False   #make valid again false to check the same for the input or player O

        while not valid:
            index = int(input("Enter index for O (1-9): ")) - 1    #-1 to get the index of the list
            #a condition to check if the entered index is valid
            if index in range(9) and pattern[index] != 'X' and pattern[index] != 'O':
                valid = True
            else:
                print("Enter a valid Index")

        #make that index 'O' in the list, which was entered by the player
        pattern[index] = 'O'
        if checkWin("O"):
            print("Game Over. O wins!")
            break

    #a condition to add score in X or O if one of them won,
    if checkWin("X"):
        xScore += 1
    elif checkWin("O"):
        oScore += 1
    # or just print a draw message if it was a draw
    else:
        print("It is a draw")

    #board display at the end to show the final board
    display_board()

    #ask user if he wants to play again and convert choice in lowercase for ease of checking
    choice = input("Do you want to play again? (Y/N): ").lower()
    #if choice is not, just make the variable false so the outer while loop doesn't run again
    if choice == 'n':
        playAgain = False
        print("Thank you for playing!")

#print the score at the end to show the players the final result
printScore()