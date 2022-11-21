names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

print(names[-2])
print(names[1:3])
print(names[3:]) # from index 3 to last
print(names[:4]) # from index 0 to index 3

# Modify elements
names[0] = 'Jon'
print(names)

# Largest element in a list
numbers = [3,68,5,13,21,79]

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"Largest number in the list is {max}")

