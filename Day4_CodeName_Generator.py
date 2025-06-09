#A code which gives a code name to an agent, and then provides a normal mission without
#verification, and asks for verification for secret missions
import random #library/module for random functions

print("Welcome Agent! Let's Generate Your Codename!\n")
#Agent's real name
name = input("Enter Your Full Name:\n")
#Agent's Year of Birth
DOB = input("Enter Your Year of Birth:\n")
#This line adds the first two characters from the Agents name to code_name to make the code name
code_name = name[0:2]
#This line adds  starts from the 5th character FROM THE END, and goes till the end, with step of 4,
#(choosing every 4th character) and concatenating with the previous two characters
code_name+= name[-5::4]
#converting the name to uppercase
code_name = code_name.upper()
# adding the last two digits of the year od birth to the code_name
code_name+=DOB[2:]
#printing code name
print("\nYour Code name is: " + code_name)
#choosing a random mission from the mission list using choice function
mission = random.choice(["Talk to General", "Meet William", "Deliver The Letter","Meet the president", "Assassination", "Bank Robbery"])
print("Randomizing your mission...\n")
#checking if the mission is a normal one
if mission == "Talk to General" or mission == "Meet William" or mission == "Deliver The Letter":
    #if mission is normal, then give the mission without verification
    print("Mission: " + mission)
    print(f"You're cleared! Good luck Agent {code_name}")
#else if the mission is top secret, then verify:
else:
    #choosing 4 random number between 1 and 20
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    num3 = random.randint(1, 20)
    num4 = random.randint(1, 20)
    #A solution of the question to be asked, saving to match later to the agents answer
    solution = num1 * num2 - num3 + num4
    print("Top Secret Mission!\n To proceed, solve this:\n")
    #taking agents guess as input to the question and converting it to int type for comparison
    agent_guess = int(input(f"{num1} * {num2} - {num3} + {num4} = "))
    #if agents answer matches the solution, then show the mission and grant permission
    if agent_guess == solution:
        print(f"You're cleared Agent {code_name}!")
        print("Mission: " + mission)
        #else don't show the mission! the person is suspicious!!!
    else:
        print("Wrong Answer! Access Denied!")
