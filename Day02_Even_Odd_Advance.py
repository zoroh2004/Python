#An easy little code which tells if a number is even or odd, further tells if the even number
#is multiple of 4, or if the odd number is greater than 50
num = int(input("Enter the number you want to check: "))
#condition to check if even
if num % 2 == 0:
    #nested-if statement for checking multiple of 4
    print("Even number")
    if num % 4 == 0:
        print("It's also a multiple of 4")
#condition to check if odd
elif num% 2 == 1:
    #nested-if to check for greater than 50
    print("Odd number")
    if num > 50:
        print("It's also greater than 50")