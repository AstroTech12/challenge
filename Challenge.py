# Ask for cities, exp, tendency
# Validate the data
def ask_for_data():
    cities = input("How many cities do you want to input from 1-3 ")
    what_cities = input("What cities do you want to input ")
    exp = input("How much c-19 exposure is there in " + what_cities)
    tendency = input("Is the exposure rising, stable, or falling ")
    print(cities, what_cities, exp, tendency)
    print("Your amount of cities is " + cities, "Your cities are " +  what_cities, "The exposure is " + exp, "The tendency is " + tendency)


ask_for_data()


# sort the data
