#this program is basically a coffee making machine, which keeps record of the remaining resources as well as
#calculates the user's given coins into dollars

# menu dictionary contains coffee types, their ingredients and cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,  # water required for espresso in ml
            "coffee": 18,  # coffee required for espresso in grams
        },
        "cost": 1.5,  # cost of espresso in dollars
    },
    "latte": {
        "ingredients": {
            "water": 200,  # water required for latte in ml
            "milk": 150,  # milk required for latte in ml
            "coffee": 24,  # coffee required for latte in grams
        },
        "cost": 2.5,  # cost of latte in dollars
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,  # water required for cappuccino in ml
            "milk": 100,  # milk required for cappuccino in ml
            "coffee": 24,  # coffee required for cappuccino in grams
        },
        "cost": 3.0,  # cost of cappuccino in dollars
    }
}

# resources dictionary stores available water, milk, and coffee
resources = {
    "water": 300,  # available water in ml
    "milk": 200,  # available milk in ml
    "coffee": 100,  # available coffee in grams
}


# checks if the user's choice is valid
def valid_choice(ch):
    """Checks if the user entered choice is valid or not"""
    if ch == 'espresso' or ch == 'latte' or ch == 'cappuccino' or ch == 'report':
        return True
    else:
        return False


# calculates total amount of money entered by user
def amount_calculator(quarter, dime, nickle, penny):
    """returns the calculated amount of each given coin into dollar form"""
    return float(quarter * 0.25 + dime * 0.10 + nickle * 0.05 + penny * 0.01)


# checks if the amount entered by user is enough for selected drink
def is_sufficientAmount(drink, amount):
    """tells if the entered amount is sufficient to make the coffee"""
    if MENU[drink]['cost'] <= amount:
        return True
    else:
        return False


# checks if there are enough resources to make the selected drink
def is_sufficientResources(drink):
    """tells if the resources like milk coffee and water in the machine are enough to make the user's coffee or not"""
    if drink == 'espresso' and resources['water'] >= MENU[drink]['ingredients']['water'] and resources['coffee'] >= \
            MENU[drink]['ingredients']['coffee']:
        return True
    elif drink == 'cappuccino' and resources['water'] >= MENU[drink]['ingredients']['water'] and resources['milk'] >= \
            MENU[drink]['ingredients']['milk'] and resources['coffee'] >= MENU[drink]['ingredients']['coffee']:
        return True
    elif drink == 'latte' and resources['water'] >= MENU[drink]['ingredients']['water'] and resources['milk'] >= \
            MENU[drink]['ingredients']['milk'] and resources['coffee'] >= MENU[drink]['ingredients']['coffee']:
        return True
    else:
        return False


# variable to store change amount
change = 0  # change to return to user in dollars

# flag to keep the coffee machine running
cont = True  # controls the while loop

# welcome message
print("Welcome to the coffee Machine!")

# main loop of the coffee machine
while cont:
    # ask user for their choice
    choice = input("What would you like (espresso, latte, cappuccino): ").lower()

    # check if user choice is valid
    if valid_choice(choice):
        # handle the 'report' option
        if choice == 'report':
            # print current resources
            print(f"Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee: {resources["coffee"]} ml")
            continue
        else:
            # ask user to insert coins
            quarters = int(input("Enter Quarters: "))  # number of quarters entered
            dimes = int(input("Enter Dimes: "))  # number of dimes entered
            nickles = int(input("Enter Nickles: "))  # number of nickles entered
            pennies = int(input("Enter Pennies: "))  # number of pennies entered

            # calculate total amount inserted
            total_amount = amount_calculator(quarters, dimes, nickles, pennies)  # total money entered

            # handle espresso order
            if choice == 'espresso':
                if not is_sufficientAmount('espresso', total_amount):
                    # refund if not enough money
                    print("Amount entered is less than the required amount, refunded you amount...")
                    total_amount = 0
                elif not is_sufficientResources('espresso'):
                    # notify if not enough resources
                    print("Not enough resources to make espresso!")
                else:
                    # prepare espresso
                    change = round(total_amount - MENU['espresso']['cost'], 2)  # calculate change
                    resources['water'] -= MENU['espresso']['ingredients']['water']  # deduct water
                    resources['coffee'] -= MENU['espresso']['ingredients']['coffee']  # deduct coffee
                    print(f"Here is your change: ${change}")  # print change
                    print("Your espresso is ready! here you go 🍵")  # coffee ready message

            # handle latte order
            elif choice == 'latte':
                if not is_sufficientAmount('latte', total_amount):
                    # refund if not enough money
                    print("Amount entered is less than the required amount, refunded you amount...")
                    total_amount = 0
                elif not is_sufficientResources('latte'):
                    # notify if not enough resources
                    print("Not enough resources to make latte!")
                else:
                    # prepare latte
                    change = round(total_amount - MENU['latte']['cost'], 2)  # calculate change
                    resources['water'] -= MENU['latte']['ingredients']['water']  # deduct water
                    resources['milk'] -= MENU['latte']['ingredients']['milk']  # deduct milk
                    resources['coffee'] -= MENU['latte']['ingredients']['coffee']  # deduct coffee
                    print(f"Here is your change: ${change}")  # print change
                    print("Your latte is ready! here you go 🍵")  # coffee ready message

            # handle cappuccino order
            elif choice == 'cappuccino':
                if not is_sufficientAmount('cappuccino', total_amount):
                    # refund if not enough money
                    print("Amount entered is less than the required amount, refunded you amount...")
                    total_amount = 0
                elif not is_sufficientResources('cappuccino'):
                    # notify if not enough resources
                    print("Not enough resources to make cappuccino!")
                else:
                    # prepare cappuccino
                    change = round(total_amount - MENU['cappuccino']['cost'], 2)  # calculate change
                    resources['water'] -= MENU['cappuccino']['ingredients']['water']  # deduct water
                    resources['milk'] -= MENU['cappuccino']['ingredients']['milk']  # deduct milk
                    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']  # deduct coffee
                    print(f"Here is your change: ${change}")  # print change
                    print("Your cappuccino is ready! here you go 🍵")  # coffee ready message
            else:
                # invalid choice entered
                print("Invalid choice!!!")

        # ask user if they want another coffee
        choice2 = input("Do you want another coffee? (Y/N): ").lower()  # user's decision
        if choice2 == 'n':
            cont = False  # stop the loop

print("Thank you!")