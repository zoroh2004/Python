#This program generated a strong password of random alphabets, characters, and numbers!

import random   #the library/module to use random functions
#List of all alphabets (uppercase and lowercase)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#List of number from 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#List of symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#An empty list which we will use
random_pass = []

print("Welcome to the PyPassword Generator!")
#asking user for the number of letters, characters,symbols
# and converting the input in integer value
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#A temporary variable which we will use
temp=""
#for loop which iterates from 0 to the value of nr_letters
for n in range(0,nr_letters):
    #take a random letter from the letter list and put it in temp
    temp=random.choice(letters)
    #add that random letter to the end of the random_pass list using append function
    random_pass.append(temp)

for n in range(0,nr_symbols):
    #take a random symbol from the symbol list and put it in temp
    temp = random.choice(symbols)
    #and that random symbol to the end of the random_pass list using append function
    random_pass.append(temp)

for n in range(0, nr_numbers):
    #take a random number from the number list and put it in temp
    temp = random.choice(numbers)
    #add that random number to the end of the random_pass list using append function
    random_pass.append(temp)

#now we have random letters, numbers, and symbols in the random_pass list
#so we will first print the random_pass list so the user can see the number
#letters,characters,symbols the user wanted to add
print(random_pass)
#shuffle function used the shuffle the values in the list
random.shuffle(random_pass)
#printing the list after shuffling
print(random_pass)

#making a variable password to save the password in a non-list form
password=""

#for loop which iterates i within the values of list the random_pass from start to end
for i in random_pass:
    #concatenate each value from the list to the password
    password+=i

#printing the password in the non_list, normal form
print(f"Your Password is: {password} ")
