import math 

while True: 
    name = input("Enter your name: ").strip()
    if name: 
        break 
    print("Name cannot be empty. Please try again.")
#Loop to get valid vage 
while True: 
    age_input = input("Enter your age: ").strip()

    if not age_input: 
        print("Age cannot be empty. Please try again.")
        continue
    try: 
        age = int(age_input) 
        if age < 0: 
            print("Age cannot be negative. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input for age. Please enter a valid integer.")

category = "Adult" if age >= 18 else "Minor" 
parity = "Even age" if age % 2 == 0 else "Odd age"
voting_status = "Can vote" if age >= 21 else "Too young to vote"

print(f'{name}, {age} years old. {category}. {parity}. {voting_status}.')
        