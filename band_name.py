#A small program, which creates a band name by concatenating the city name and pet name

print("Welcome to the band name generator")
#taking the input for the city name and storing in the variable city_name
city_name=input("What is the name of the city you grew up in?\n")
#taking the input fot the pet name and storing it in the variable pet_name
pet_name=input("What is the name of your pet?\n")
# concatenated name=city_name+pet_name
band_name=city_name+" "+pet_name
#printing the band name with the message
print("Your band name is: "+band_name)
