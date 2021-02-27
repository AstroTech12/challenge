import sorting
# Ask for cities
def main_function():
	input("Choose 3 Cities, type Yes to continue ")
	city1 = input("What is your first city? ")
	city2 = input("What is your second city? ")
	city3 = input("What is your third city? ")
	print("Your first city is " + city1 + " your second city is " + city2 + " your third city is " + city3)

	#ask for exposure
	exposure1 = input("How many c-19 cases are there in " + city1 + ". ")
	exposure2 = input("How many c-19 cases are there in " + city2 + ". ")
	exposure3 = input("How many c-19 cases are there in " + city3 + ". ")
	print("There are " + exposure1 + " cases in " + city1 + ", " + exposure2 + " cases in " + city2 + " and there are " + exposure3 + " cases in " + city3 + ".")

	#ask for tendency 
	tendency1 = input("Are the cases going higher, lower or staying stable in " + city1)
	tendency2 = input("Are the cases going higher, lower or staying stable in " + city2)
	tendency3 = input("Are the cases going higher, lower or staying stable in " + city3)
	print("The cases are " + tendency1 + " in " + city1 + " The cases are " + tendency2 + " in " + city2 + " The cases are " + tendency3 + " in " + city3)

	#sort data
	covid_list = [exposure1, exposure2, exposure3]
	covid_list.sort(reverse = True)
	print (covid_list)



main_function()
