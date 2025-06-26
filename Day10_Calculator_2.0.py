# this program is a simple text-based calculator that performs basic arithmetic operations (+, -, *, /)
#with the use of dictionaries. it repeatedly asks the user to perform calculations until they choose to stop

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________| 
"""

print(logo)

# function to add two numbers
def add(n1, n2):
    return n1 + n2

# function to subtract second number from first
def sub(n1,n2):
    return n1 - n2

# function to multiply two numbers
def mul(n1,n2):
    return n1 * n2

# function to divide first number by second
def div(n1,n2):
    return n1 / n2

# dictionary to store operators and their corresponding functions
oper = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

# to store the result of each calculation
result = 0

# to store user choice for continuing or stopping
choice = None

# to store the first number entered by the user
num1 = int(input("Enter first number: "))

# loop continues until user chooses to stop
while choice != "no":
    # to store the operator chosen by the user
    operator = input("+,-,/,*\nChoose an Operation to perform: ")

    # to store the second number entered by the user
    num2 = int(input("Enter second number: "))

    # apply the selected operation and store the result
    result = oper[operator](num1,num2)

    # display the result
    print(f"{num1} {operator} {num2} = {result}")

    # to get user's decision to continue or not
    choice = input(f"Enter y to continue calculating with {result}, or n end: ").lower()

    if choice == "n":
        break
    else:
        # update num1 to the latest result for next operation
        num1 = result
        continue

# exit message
print('Exiting...')
