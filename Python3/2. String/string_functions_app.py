statement = "This is a string"

print(len(statement)) # Return length of a string. len() is a general purpose function
print(statement.upper()) # upper() is a method to convert string to upper case. Doesn't change actual string.
print(statement.lower())

# methods are functions belonging to an object specifically.

print(statement.find('s')) # Returns the first index of character if present. Returns -1 when no character is present.
print(statement.find('is')) # Also returns index of first character of a string inserted, if present.

print(statement.replace('i','u')) # Replace first character with the second one.

print('This' in statement) # Boolean to check whether this sequence of character is present or not.

print(statement.title()) # Convert first character of every word capital