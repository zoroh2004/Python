#A program which simulates a silent bidding system which ask for bidders and their
#bids until no more bidders want to join, and then announce the highest bidder

#a logo of a bidding hammer
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


print(logo)
#a bid_winner function which calculates highest bidder after
# no more bidders want to participate
def bid_winner(bid_dict):
    #variables to store bid winner name and his bid amount
    bid_winner_name = ""
    bid_winner_amount = 0
    #a loop which iterates in the dictionary
    for key in bid_dict:
        #if the value(bid amount) for the corresponding key(name) in the dictionary is greater than the value in
        # bid_winner_amount, then but the value in the variable and the bidder name in the other variable
        if bid_dict[key] > bid_winner_amount:
            bid_winner_amount = bid_dict[key]
            bid_winner_name = key
    #after the loop finished to check all the bidders, show the bid_winner_name and bid_winner_amount
    print(f"The bid winner {bid_winner_name} with the bid of {bid_winner_amount}")

#a dictionary to keep records of the bidders and their bids
bidder_dictionary = {}
#boolean variable for while loop
continue_bid = True
while continue_bid: #while continue_bid == True
    #ask for user's name and bid
    name = input("What is you name?\n")
    #rounds the bid of user to 2 decimal places
    bid = round(float(input("What is your bid?\n")),2)
    #save the input data in the dictionary
    bidder_dictionary[name] = bid
    #ask if any more bidders want to participate and convert the input in lowercase for ease
    ask_for_bidders = input("Are there any other bidders? 'Yes' or 'No'? ").lower()
    #if the user says no, the make the boolean variable false to terminate while loop
    #and call the bid_winner function  with dictionary as parameter
    if ask_for_bidders == 'no':
        continue_bid = False
        bid_winner(bidder_dictionary)
    #else if user says yes, clear the screen by printing new line 50 times, so that
    #the new user cannot see the other users bids, and then print the hammer logo again
    elif ask_for_bidders == 'yes':
        print("\n" * 50)
        print(logo)
