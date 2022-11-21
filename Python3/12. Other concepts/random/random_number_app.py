import random

for i in range(3):
    print(random.random()) # Between 0 and 1
    print(random.randint(10, 20)) # Random value between 10 and 20

members = ["John", "Mary", "Joshua", "Thomas"]
print(random.choice(members)) # Chooses random item



