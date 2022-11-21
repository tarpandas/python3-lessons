# Dictionary - key:value pairs
customer = {
    "name": "Jaon Smith",
    "age" : 30,
    "is_verified" : True
}

# Each key in Disctionary should be unique

print(customer["age"])

print(customer.get("birthdate", "Jan 1 1980"))
# get() method helps avoid unnecessary error beimng thrown
# if a key is not present, a 'None' object is shown
# The second argument is the default value

# Assigning value
customer["name"] = "Jack Smith"

# Assiging new key:value pair
customer["birthday"] = "Jan 1 1990"

# Example - Output name for numbers
phone = input("Phone:")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)