num = int(input("Enter the number you want to check: "))
if num % 2 == 0:
    print("Even number")
    if num % 4 == 0:
        print("It's also a multiple of 4")
elif num% 2 == 1:
    print("Odd number")
    if num > 50:
        print("It's also greater than 50")