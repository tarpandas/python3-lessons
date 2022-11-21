def greet_user_1():
    print("Hi there!")
    print("Welcome aboard!")

print("Start")
greet_user_1() # Call the function after defining
print("Finish")

# Function parameters

def greet_user_2(first_name, last_name): # first_name and last_name are parameter here
    print(f"Hi, {first_name} {last_name}!")
    print("Welcome aboard!")

print("Start")
greet_user_2("John","Smith") # John and Smith are (positional) arguments
greet_user_2(last_name="Mary",first_name="Jane") # We can specify what argument to come first, by this method. These are keyword arguments.
print("Finish")

# Note: If there are two arguments, one keyword and one positional, make sure that the positional argument comes first

# Return statements

def add_two_numbers(number1, number2):
    return number1 + number2

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

print(f"Sum: {add_two_numbers(number1, number2)}")