"""
Project: Password Generator
Description: Generates a random password based on user-selected
numbers of letters, symbols, and digits.
"""

import random

# Character pools
LETTERS = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
NUMBERS = list("0123456789")
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("🔐 Welcome to the Password Generator!")

# User input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate password characters
password_chars = []

for _ in range(nr_letters):
    password_chars.append(random.choice(LETTERS))

for _ in range(nr_symbols):
    password_chars.append(random.choice(SYMBOLS))

for _ in range(nr_numbers):
    password_chars.append(random.choice(NUMBERS))

# Shuffle to make password unpredictable
random.shuffle(password_chars)

# Convert list to string
password = "".join(password_chars)

print(f"\nYour generated password is:\n{password}")

