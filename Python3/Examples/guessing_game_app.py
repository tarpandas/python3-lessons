import random

secret_number = random.randrange(1,10)
print("A secret number is generated between 1 and 10.")
print("Guess the number.\nNOTE: The number remains the same for 3 tries.")

guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input(f"Guess {guess_count + 1}: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break # Breaks the entire loop on condition
else:
    print("You fail.")
    print(f"The correct number is {secret_number}")
    