# for loop with a string
for item in 'Python':
    print(item)

# for loop with a list
list_example = ["There", "Are", 3, "People"]
for item in list_example:
    print(item)

# for loop with a range function
for item in range(5, 10): #range() is a function (start, end+1, step)
    print(item)

# for loop to add list numbers
prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"Total: Rs. {total}")

# nested for loop
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')