"""
Project: Caesar Cipher
Description: A command-line program that encrypts and decrypts messages
using the Caesar Cipher technique.
"""

from art import logo

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

print(logo)


def caesar_cipher(text: str, shift: int, mode: str) -> str:
    """
    Encrypts or decrypts text using Caesar Cipher.

    Args:
        text (str): Input message
        shift (int): Shift value
        mode (str): 'encode' or 'decode'

    Returns:
        str: Transformed text
    """
    result = ""

    # Normalize shift to stay within alphabet length
    shift = shift % len(ALPHABET)

    if mode == "decode":
        shift *= -1

    for char in text:
        if char.isalpha():
            index = ALPHABET.index(char)
            new_index = (index + shift) % len(ALPHABET)
            result += ALPHABET[new_index]
        else:
            result += char  # keep symbols and spaces unchanged

    return result


while True:
    direction = input("\nType 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    if direction not in ("encode", "decode"):
        print("❌ Invalid choice. Please type 'encode' or 'decode'.")
        continue

    message = input("Type your message:\n").lower()

    try:
        shift_number = int(input("Type the shift number:\n"))
    except ValueError:
        print("❌ Shift must be a number.")
        continue

    output = caesar_cipher(message, shift_number, direction)
    print(f"\n✅ Here is the {direction}d result:\n{output}")

    restart = input("\nType 'yes' to go again, or 'no' to exit:\n").lower()
    if restart == "no":
        print("Goodbye 👋")
        break

