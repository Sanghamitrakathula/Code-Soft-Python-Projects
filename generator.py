import random

# Lists of characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to Password Generator!")

# User inputs
n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

# Generate password
password = ""

# Add letters
for _ in range(n_letters):
    password += random.choice(letters)

# Add symbols
for _ in range(n_symbols):
    password += random.choice(symbols)

# Add numbers
for _ in range(n_numbers):
    password += random.choice(numbers)

# Shuffle the password to randomize character order
password = ''.join(random.sample(password, len(password)))

# Output the generated password
print(f"Your generated password is: {password}")
