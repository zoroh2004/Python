# this program is a simple calculator using match-case (similar to switch case)
# it performs basic arithmetic operations (+, -, *, /) and lets the user continue calculations

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

# display the logo
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

    # use match-case to choose the operation
    match operator:
        case "+":
            result = add(num1, num2)
        case "-":
            result = sub(num1, num2)
        case "*":
            result = mul(num1, num2)
        case "/":
            # divide and round result to 2 decimal places
            result = round(div(num1, num2), 2)
        case _:
            # handle invalid operator input
            print("Invalid input!")

    # show the calculation result
    print(f"{num1} {operator} {num2} = {result}")

    # ask user if they want to continue with result or exit
    choice = input(f"Enter y to continue calculating with {result}, or n end: ").lower()

    if choice == "n":
        break
    else:
        # update num1 for the next operation
        num1 = result
        continue

# exit message
print('Exiting...')
