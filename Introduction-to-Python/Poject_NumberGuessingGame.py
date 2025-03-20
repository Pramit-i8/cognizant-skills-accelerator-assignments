import random

#Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

attempts = 0
max_attempts = 10


print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100. You have 10 attempts.")

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1  # Increase the number of attempts
    
    # Check if the guess is correct, too high, or too low
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break  # Exit the loop if the user guesses correctly
    
    # If they reached the max attempts, end the game
    if attempts == max_attempts:
        print(f"Game over! Better luck next time! The correct number was {number_to_guess}.")
