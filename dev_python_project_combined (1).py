
# Dev's Simple Python Projects

import random
import string

# Number Guessing Game
def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    tries = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {tries} tries.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Password Generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Main Menu
def main():
    print("Select a project to run:")
    print("1. Number Guessing Game")
    print("2. Password Generator")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        number_guessing_game()
    elif choice == "2":
        password_generator()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
