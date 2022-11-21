# We use try...except blocks to handle exception in our program
try:
    age = int(input('Age: '))
    print(age)
except ValueError: # ValueError is an exception which occurs when integer is not entered
    print("Invalid Value")

# Entering two except
try:
    num1 = int(input('Enter num 1: '))
    num2 = int(input('Enter num 2: '))
    print(num1 / num2)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Error! Divided by 0")