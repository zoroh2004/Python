#this program simulates an menu-driven ATM system

#a function which shows user the current balance of account
def check_balance():
    #rounds of the number to 2 decimal places
    print(f"Your balance  is: {round(balance,2)}")

#a function used to deposit money in the account
def deposit_money(amount):
    #defining the use of the globally declared variable
    global balance
    balance += amount
    #adding the transaction in the transaction history list
    transactions.append("Deposited of: $" + str(amount) + ", Balance: $" + str(balance))

#a function used to withdraw money in the account
def withdraw_money(amount):
    # defining the use of the globally declared variable
    global balance
    #a check to see if the withdrawal amount is withing the account balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        # adding the transaction in the transaction history list
        transactions.append("Withdrawal of: $" + str(round(amount,2)) + ", Balance: $" + str(round(balance,2)))

#a function used to display the transaction history
def transaction_history():
    print("Transaction History:")
    #a loop which iterates within the transaction history list
    for i in transactions:
        print(i)

#pre defined global variables
balance = None #initial balance to none
PIN = '1234' #user account pin
transactions = [] #transaction list
print("Welcome to Python Bank!")
#number of tries for the user before the program terminates
tries = 3
#loop run until tries are nor zero
while tries > 0:
    pin_try = input("Enter PIN: ")
    #if user's entered pin is the same as the actual pin, then login successful
    if pin_try == PIN:
        print("Login Successful!")
        #break the loop as we don't want to try thr pin again
        break
        #else decrement 1 in tries and run the loop again if tries left
    else:
        print("Incorrect PIN")
        tries-=1
#if tries finished, then try sometime later
if tries == 0:
    print("Try again Later")
#else don't print the try again later message and move towards the menu
else:
    #initialize choice to none
    choice = None
    #run the loop until choice isn't the exit choice
    while  choice != 5:
        #asak user the choice in digit and convert to integer
        choice = int(input("1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Transaction History\n5.Exit\n"))
       #call check_balance function
        if choice == 1:
            check_balance()
        #ask user the deposit amount and convert it to float value,then call the deposit_amount function
        elif choice == 2:
            deposit_amount = float(input("Enter amount you want to deposit: "))
            deposit_money(deposit_amount)
            print("Amount deposit successful!")
        #ask user the withdrawal amount and convert it to float value, then call the withdraw_amount function
        elif choice == 3:
            withdraw_amount = float(input("Enter amount you want to withdraw: "))
            withdraw_money(withdraw_amount)
            print("Amount withdrawal successful!")
        #call transaction_history function
        elif choice == 4:
            transaction_history()
        #exit the program
        elif choice == 5:
            print("Exiting...")
        #if choice is any other, print invalid choice
        else:
            print("Invalid choice!")