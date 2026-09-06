import random

number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Congratulations! You guessed correctly.")
else:
    print("Sorry! The correct number was", number)
