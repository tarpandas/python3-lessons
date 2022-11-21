print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3) # Returns actual division value
print(10 // 3) # Returns quotient
print(10 % 3) # Returns remainder
print(10 ** 3) # x ** y means x to the power y

x = 10
x = x + 3
print(x)

# Augmented assignment operator

x = 10
x += 3 # x += y, x-= y, x*= y, x/= y, etc. are applicable
print(x)

# Operator Precedence

'''
parenthesis
exponent
multiplication or division
addition or suntraction
'''

x = 10 + 3 * 2 ** 2
print(x)

x = 10 + (3 * 2) ** 2
print(x)