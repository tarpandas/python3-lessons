numbers = [5,2,1,7,4]

numbers.append(13) # append(int x) add new number
print(numbers)

numbers.insert(0,10) # insert(int x, int y) - insert value at index

numbers.remove(5) # remove(int x) - remove the inserted element

# numbers.clear() # clear() - empties the list

numbers.pop() # pop() - remove the last value only

print(numbers.index(2)) # index(int x) - check the index of the number given

print(50 in numbers) # in operator - to check wheher there is a number or not

numbers.sort() # sort() - sort values in-place
print(numbers)

numbers.reverse() # reverse() - reverses the list
print(numbers)

nums = numbers.copy() # copy() - Makes a new copy
print(nums)

# Example - Removes the duplicates

new_numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in new_numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
