import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Welcome message
print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Loop until the correct guess
while True:
    # Prompt for guess and convert to integer
    guess = input("Enter your guess: ")
    guess = int(guess)
    
    # Check if guess is too high, too low, or correct
    if guess > secret_number:
        print("Your guess is too high. Guess again.")
    elif guess < secret_number:
        print("Your guess is too low. Guess again.")
    else:
        print("Congratulations! You guessed the number correctly!")
        break