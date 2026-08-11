import random

secret_number = random.randint(1,10)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 10.")

while True:
    user_input = input("Take a guess: ")
    guess = int(user_input)

    if guess == secret_number:
        print("Wow! You guessed it! You win!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")