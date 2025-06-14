#a program to encrypt or decrypt a message with the caesar cipher method

#logo to print on top of the screen
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
#a list which keeps all the alphabets in lowercase
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#a function to perform encryption, taking the text entered,
# and the number of shifts and parameter
def encrypt(txt, sh):
    #a string encrypt_msg used to keep the encrypted message
    encrypt_msg = ""
    # a loop which for each character of txt
    for i in txt:
        #if the character of txt is space, then add space to the encrypt_msg
        if i == " ":
            encrypt_msg += " "
        #else make a variable shift_position equal to the current index of the
        # txt character in the alphabet list + the shift amount
        else:
            shift_position = alphabet.index(i) + sh
            #if the shift makes a number out of bound, the function wrap-arounds
            #to come to the first index
            if shift_position > 25:
                shift_position -= 26 #wrap around
            #concatenated the alphabets with the encrypted string
            encrypt_msg += alphabet[shift_position]

    print(f"Encrypted msg is: {encrypt_msg} ")

#a decrypt function which takes the number of shifts and text entered as parameter
def decrypt(txt, sh):
    #a decrypt_msg string which stores the decrypted message
    decrypt_msg = ""
    # a loop which for each character of txt
    for i in txt:
        #if the character of txt is space, then add space to the encrypt_msg
        if i == " ":
            decrypt_msg += " "
        # else make a variable shift_position equal to the current index of the
        # txt character in the alphabet list - the shift amount
        else:
            shift_position = alphabet.index(i) - sh
            # if the shift makes a number out of bound, the function wrap-arounds
            # to come to the last index
            if shift_position < 0:
                shift_position += 26
            # concatenated the alphabets with the decrypted string
            decrypt_msg += alphabet[shift_position]

    print(f"Decrypted msg is: {decrypt_msg}")

#start of the program:
#prints the caesar cipher logo
print(logo)
# a boolean variable to check if the program is asked to run again or not
run = True
#run the program while run == True
while run:
    #the direction for encoding or decoding
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    #if the user entered 'encode':
    if direction == "encode":
        #input text and the number of shifts(int)
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        #function call with parameters
        encrypt(text,shift)
    #else if the directions is 'decode':
    elif direction == "decode":
        #input teh text and number of shifts(int)
        text2 = input("Type your message:\n").lower()
        shift2 = int(input("Type the shift number:\n"))
        #function call for decrypt
        decrypt(text2, shift2)
    #if the direction is none of the above, then print an error message
    else:
        print("Invalid choice!")
        continue
    choice = ""
    while choice != "yes" and choice != "no":
        # after each encryption/decryption, ask the user if he wants to continue
        choice = input("do you want to continue? yes or no? ").lower()
        # if yes, keep the run variable true to keep the while condition running
        if choice == 'yes':
            run = True  # loop will continue because run is still True
        # else if choice is no, make it false
        elif choice == 'no':
            run = False  # loop will stop after this iteration
        else:
            print("invalid choice!")  # handles any input other than "yes" or "no"
