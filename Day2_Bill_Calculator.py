#a simple program which takes the total bill, asks the percentage of tip,
# and then adds the tip percentage to the total bill, then asks the number of people to
# divide the bill in, then divides the bill and rounds off by two decimal places

print("Welcome to the tip calculator!")
#conversion of the input in float data type
bill = float(input("What was the total bill? $ "))
#conversion of the input in int data type
tip = int(input("How much tip would you like to give? 10 12 15 "))
#conversion of the input in int data type
people = int(input("How many people to split bill: "))
#calculating the tip percentage (tip / 100 * bill)
tip_percentage = tip / 100
tip_perc_calculation = tip_percentage * bill
#calculating the total bill
total = bill + tip_perc_calculation
#rounding off the bill to two decimal points
split = round(total / people, 2)
#using fprint here to print other data type in curly braces, with string
print(f"Each person should pay: ${split}")
