import random
import time
import math

print('Welcome to the Number Guessing Game!')

while True: 
    time.sleep(1) 

    valid_difficulties = ['easy', 'medium', 'hard']
    difficulty = input('Please select a difficulty (Easy, Medium, Hard): ').lower()

    while difficulty not in valid_difficulties:
        print("ERROR: Invalid Input. Please enter 'Easy', 'Medium', or 'Hard'.")
        difficulty = input('Please select a difficulty (Easy, Medium, Hard): ').lower()

    print(f'Selected Difficulty: {difficulty}')

    if difficulty == 'easy':
        max_number = 100
        max_attempts = math.inf
    elif difficulty == 'medium':
        max_number = 200
        max_attempts = 6
    else:  # hard
        max_number = 500
        max_attempts = 6

    number_to_guess = random.randint(1, max_number)
    attempts = 0

    if max_attempts == math.inf:
        print("You have unlimited attempts in this difficulty.")
    else:
        print(f"You have {max_attempts} attempts in this difficulty.")

    while attempts < max_attempts:
        try:
            prompt_attempts = f" ({max_attempts - attempts} attempts left)" if max_attempts != math.inf else ""
            user_guess = int(input(f"Guess a number between 1 and {max_number}{prompt_attempts}: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f'Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!')
                break

        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {max_number}")

    else:
        if max_attempts != math.inf:
            print(f"You've used all {max_attempts} attempts. The number was {number_to_guess}.")

    #Replay prompt
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay not in ['yes', 'y']:
        print("Thanks for playing! Goodbye!")
        break  # Exit the replay loop