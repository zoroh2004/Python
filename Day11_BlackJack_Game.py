#this program simulates the blackjack card game, also used some emojis to make it look fun😁

#importing random library to use random function
import random

#a logo to print on top. used r so that it takes the \ as a character and not part of code
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#a list of the score on each card, 11 an ace,1-10 numbers, and last three 10s for King Queen and Jack
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_list = []  #a list which will store the cards/number that the player got
dealer_list = []    # a list to store the cards/numbers the dealer got
final_score_player = 0    #variable to store the score of player
final_score_dealer = 0    #variable to store the score of dealer

#print statements to print the initial empty lists and scores
print(f"Your final hand: {player_list}, final score: undefined")
print(f"Dealer's final hand: {dealer_list}, final score: undefined")

#asking user for input and converting to lowercase
choice = input("Do you want to play a game of Blackjack (Y/N)🤔: ").lower()

#if user chooses y or Y, then
if choice == "y":
    #while the choice is not no, do the following
    while choice != 'n':
        #welcome screen
        print(logo)
        print("Welcome to the Blackjack game!")

        #add two random cards/numbers from the cards list to the player_list
        player_list.append(random.choice(cards))
        player_list.append(random.choice(cards))

        #add those cards/number to the final_score_player
        final_score_player += player_list[0]
        final_score_player += player_list[1]

        #print the cards and score on the terminal
        print(f"your cards are: {player_list}, current score: {final_score_player}")

        #add a random card/number to the dealer list once
        dealer_list.append(random.choice(cards))

        #add the dealer's first drawn card to the dealer's total score
        final_score_dealer += dealer_list[0]

        #print the dealer's first visible card on screen
        print(f"Dealer's first card: {dealer_list[0]}")

        #a function to simulate the dealer's move after player finishes
        def dealerFunc():
            #using global so we can modify original dealer variables
            global final_score_dealer, dealer_list

            #dealer will draw cards until score reaches at least 17
            while final_score_dealer < 17:
                #get a random card from deck
                card = random.choice(cards)

                #if card is ace and dealer might bust, use 1 instead
                if card == 11 and final_score_dealer > 10:
                    dealer_list.append(1)  #append 1 instead of 11 to prevent bust
                else:
                    dealer_list.append(card)  #append the card to dealer hand

                #update dealer score with new card
                final_score_dealer += dealer_list[-1]

            #show final dealer hand and score
            print(f"Dealer's cards are: {dealer_list}, current score: {final_score_dealer}")

        #flag to continue giving player more cards
        continue_choice = 'y'

        #loop while player wants another card
        while continue_choice == 'y':

            #if player has blackjack, stop asking
            if final_score_player == 21:
                break

            #ask for more card
            continue_choice = input("Type Y to get another card, Type N to pass: ").lower()

            if continue_choice == 'y':
                #draw a random card for player
                card = random.choice(cards)

                #adjust ace if player might bust
                if card == 11 and final_score_player > 10:
                    player_list.append(1)
                else:
                    player_list.append(card)

                #update player score with new card
                final_score_player += player_list[-1]

                #if still under 21, show current state
                if final_score_player <= 21:
                    print(f"your cards are: {player_list}, current score: {final_score_player}")

                #if over 21, check if any ace can convert to 1
                elif final_score_player > 21:
                    for i in player_list:
                        if i == 11:
                            player_list.remove(i)
                            player_list.append(1)
                            final_score_player -= i
                            final_score_player += 1

                        #show adjusted score
                        print(f"your cards are: {player_list}, current score: {final_score_player}")

                #final check for bust after ace adjustment
                if final_score_player > 21:
                    print("Your score is greater than 21, you lose!")   #print lose message
                    break

        #if player stops or gets blackjack
        if continue_choice == "n" or final_score_player == 21:
            dealerFunc()   #let dealer play

        #if player busts, it's a loss
        if final_score_player > 21:
            print("You lose!😢")
        #if dealer busts, player wins
        elif final_score_dealer > 21:
            print("You win!😎")
        #if player has higher score
        elif final_score_player > final_score_dealer:
            print("You win!😎")
        #if dealer has higher score
        elif final_score_dealer > final_score_player:
            print("You lose!😢")
        else:
            print("Draw!🤷‍♂️")   #if scores equal, it's a draw

        #ask for another round
        choice = input("Do you want to play another game of Blackjack? (Y/N)🤔: ")

        if choice == "y":
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            player_list = []
            dealer_list = []
            final_score_player = 0
            final_score_dealer = 0
            print("\n"*40)   #prints 40 newlines to give a fresh screen look for the next game
            #reinitializing the cards list to its original values with all card types
            #clearing player and dealer lists to remove any previously drawn cards
            #resetting both final scores back to 0 to start the next round fresh