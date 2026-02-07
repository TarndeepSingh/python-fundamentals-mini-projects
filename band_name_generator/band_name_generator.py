"""
Project: Band Name Generator
Description: Generates a fun band name based on user input.
This project practices basic Python concepts such as input,
variables, string manipulation, and output formatting.
"""

print("🎸 Welcome to the Band Name Generator!")

# Ask the user for inputs
city = input("Which city did you grow up in?\n").strip()
pet = input("What is the name of a pet?\n").strip()

# Basic validation (kept simple for Day 1 level)
if city and pet:
    band_name = f"{city} {pet}"
    print(f"\nYour band name could be: {band_name}")
else:
    print("\nPlease provide valid inputs to generate a band name.")

