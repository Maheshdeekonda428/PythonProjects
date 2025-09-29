import random

name = input("What is your name? ")
print(f"Good Luck, {name}!")
print("Guess the word (only from programming language names)\n")

words = ['java', 'javascript', 'sql', 'aws', 'python', 'html', 'css', 'database', 'mongodb']
word = random.choice(words)  # Random word
guesses = ''                 # To store guessed letters
turns = 12                   # Number of attempts


while turns > 0:
    failed = 0

    # Display word progress
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()  # new line

    # Check win condition
    if failed == 0:
        print("You Win! The word is:", word)
        break

    guess = input("Guess a character: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter only.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        print("You have", turns, "more guesses.\n")

        if turns == 0:
            print("You Lose! The word was:", word)
