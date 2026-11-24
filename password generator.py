import random 
import string

length = int(input("Enter the length of the password: "))
include_digits = input("Include digits? (yes/no): ").lower() == "yes"
include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"


def generate_password(length):

    if length < 2: 
        return "Password length should be at least 2 characters."
    
    password = [] 

    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase)) 

    if include_digits: 
        password.append(random.choice(string.digits)) 
    if include_symbols: 
        password.append(random.choice(string.punctuation))

    all_characters = string.ascii_letters
    if include_digits:
        all_characters += string.digits 
    if include_symbols: 
        all_characters += string.punctuation

    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    random.shuffle(password) 
    return "".join(password)

print("Generated password:",generate_password(length)) 