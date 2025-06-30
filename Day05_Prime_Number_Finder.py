#a program which finds all the prime numbers withing a range
num1 = int(input("Enter first number: ")) #user input for start of range
num2 = int(input("Enter second number: ")) #user input for end of range

#a loop which runs until n is withing the user's given range
for n in range(num1,num2+1):
    #initially isPrime is true
    isPrime = True
    #0 and 1 are not prime
    if n == 0 or n == 1:
        isPrime = False
    #2 is a prime
    elif n == 2:
        isPrime = True
    #for values other than 0,1,2
    else:
        #a loop that runs from 2 to half of n (+1 is done so that it runs at least once)
        for i in range(2,int(n/2) + 1):
            #if number is divisible by any number under from 2 to it's half, even once,
            #it means it is not a prime (we check until half because no number greater than the half
            #can  logically be a multiple of n
            if n % i == 0:
                isPrime = False
                break # no need to check further and we break the loop
       #if nothing happens i the loop, that means the number was a prime
    #if isPrime == True
    if isPrime:
        print(f"Number {n} is Prime")
    #elif isPrime != True
    else:
        print(f"Number {n} is not Prime")


