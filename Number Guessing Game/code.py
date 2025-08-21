import random

print("Welcome to the Number Guessing Game!")
print("You have 5 chances to guess the number.")

# Define the guessing range
low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

# Generate a random number in range
num = random.randint(low, high)
chances = 5  # total allowed guesses
attempts = 0

while attempts < chances:
    attempts += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {attempts} attempts.")
        break
    elif guess > num:
        print("Too high! Try a lower number.")
    elif guess < num:
        print("Too low! Try a higher number.")

    if attempts == chances and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time.")
