name = input('What is your name? ') # Takes string input
favourite_color = input('What is your favourite color? ')
# input() is a function

print('Hi ' + name)
print(name + ' likes ' + favourite_color)

# Type conversion
birth_year = int(input("Enter your year of birth: ")) # String to Integer
birth_year = 2022 - birth_year
print("You age is {0}".format(birth_year)) # String formatting used

# Example: Pound to Kilograms
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print("{0} lbs is equivalent to {1} kg.".format(weight_lbs,weight_kg))