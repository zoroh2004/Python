#a program that repeatedly asks the user to enter a password until they enter a strong password
#A strong password has:
#atleast 8 characters
#one uppercase letter
#one lowercase letter
#one digit
#one special character

isStrong = False #a boolean variable to check if the password is strong or not
character = "!@#$%^&*()_-" #all special characters in a string
# a while loop which runs until the password is not strong (while isStrong != True)
while not isStrong:
    #some boolean variables for each condition
    has_upper = False
    has_lower = False
    has_digit = False
    has_char = False
    #input password in a variable
    password = input("Enter the password for your account: ")
    #a for loop which runs withing the password string to check each character of the string
    for ch in password:
        #checks if the current character is uppercase
        if ch.isupper():
            has_upper = True
        #checks if the current character is lowercase
        elif ch.islower():
            has_lower = True
        #checks if the current character is a digit
        elif ch.isdigit():
            has_digit = True
        #checks if the current character is from the special character string
        elif ch in character:
            has_char = True

    #if all the conditions are true, then password is strong (isStrong = True)
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_char:
        print("Password is Strong!")
        isStrong = True
    #else print message for respective error
    else:
        if len(password)<8:
            print("Password should be at least 8 characters long!")
        if not has_upper:
            print("Password should have at least one uppercase letter!")
        if not has_lower:
            print("Password should have at least one lowercase letter!")
        if not has_digit:
            print("Password should have at least one digit!")
        if not has_char:
            print("Password should have at least one special character")
