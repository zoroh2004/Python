#this is similar to the coffee machine i did yesterday but this is done using oop concepts

# models the machine that makes the coffee
class CoffeeMaker:
    """Models the machine that makes the coffee"""

    # initialize the coffee machine resources
    def __init__(self):
        self.resources = {  # dictionary of ingredients
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    # prints the current resource levels
    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    # checks if resources are enough for the selected drink
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True  # flag for resource sufficiency
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    # deducts used resources and serves coffee
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")


# models each drink item on the menu
class MenuItem:
    """Models each Menu Item."""

    # initialize menu item details
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name  # name of the drink
        self.cost = cost  # cost of the drink
        self.ingredients = {  # required ingredients
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


# models the menu with all available drinks
class Menu:
    """Models the Menu with drinks."""

    # initialize the menu with predefined drinks
    def __init__(self):
        self.menu = [  # list of menu items
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    # returns all available menu options as a string
    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""  # string to store drink names
        for item in self.menu:
            options += f"{item.name}/"
        return options

    # finds a drink by name in the menu
    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")


# models the money handling for the coffee machine
class MoneyMachine:
    """Handles money transactions for the coffee machine"""

    CURRENCY = "$"  # currency symbol

    COIN_VALUES = {  # value of each coin type
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    # initialize money tracking
    def __init__(self):
        self.profit = 0  # total profit made
        self.money_received = 0  # total money received

    # prints the current total profit
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    # calculates total from inserted coins
    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    # handles payment and returns True if successful
    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)  # calculate change
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost  # add to profit
            self.money_received = 0  # reset money received
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0  # reset money received
            return False


# main program starts here

# create instances of menu, coffee maker, and money machine
menu = Menu()  # menu object
coffee_maker = CoffeeMaker()  # coffee maker object
money_machine = MoneyMachine()  # money machine object

is_on = True  # flag to keep machine running

# main loop to run the coffee machine
while is_on:
    # ask user what they want to order
    options = menu.get_items()  # get available drinks
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        # turn off the coffee machine
        print("Turning off the coffee machine... thank yu!")
        is_on = False
    elif choice == "report":
        # print resource and money reports
        coffee_maker.report()
        money_machine.report()
    else:
        # find the selected drink in the menu
        drink = menu.find_drink(choice)
        if drink:
            # check if enough resources for the drink
            if coffee_maker.is_resource_sufficient(drink):
                # process the payment
                if money_machine.make_payment(drink.cost):
                    # make the coffee if payment successful
                    coffee_maker.make_coffee(drink)
