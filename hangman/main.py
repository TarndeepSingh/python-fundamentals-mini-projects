"""
Project: Hangman Game
Description: A command-line word guessing game where the player
tries to guess the hidden word before running out of lives.
"""

import random
from hangman_words import word_list
from hangman_art import stages, logo

# Game configuration
MAX_LIVES = len(stages) - 1
lives = MAX_LIVES

print(logo)

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game state
display = ["_"] * word_length
guessed_letters = set()
game_over = False

print(f"Word to guess: {' '.join(display)}")

while not game_over:
    print(f"\n❤️ Lives left: {lives}/{MAX_LIVES}")
    guess = input("Guess a letter: ").lower().strip()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.add(guess)

    # Check guess
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print("✅ Good guess!")
    else:
        lives -= 1
        print(f"❌ '{guess}' is not in the word. You lose a life.")

    print("\nWord:", " ".join(display))
    print(stages[lives])

    # Win condition
    if "_" not in display:
        game_over = True
        print("\n🎉 YOU WIN! You guessed the word correctly.")

    # Lose condition
    if lives == 0:
        game_over = True
        print(f"\n💀 YOU LOSE! The word was: {chosen_word}")

