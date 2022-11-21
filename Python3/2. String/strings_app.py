statement_1 = "This is Ratan's book."
statement_2 = 'This is Mukesh\'s pen.' # Using \' to use '

print(statement_1)
print(statement_2)

statement_3 = '''
Hello programmer,

This is a multiline string.

Thank you,
Programmer

'''
print(statement_3)

statement_4 = "String Indexing"

print(statement_4[0]) # First character of a string
print(statement_4[-1]) # Last character of a string
print(statement_4[0:3]) # 0 is inclusive, 3 is exclusive
print(statement_4[:5]) # 0 is the start index, if nothing is mentioned
print(statement_4[5:]) # Ending index is length of the string
print(statement_4[:]) # Prints whole string
print(statement_4[1:-1]) # From character at index 1 to the character before the last index

first = 'John'
last = 'Smith'

message = first + ' [' + last + '] is a coder.' # String concatenation

print(message)

print(f'{first} [{last}] is a coder.') # String formatting