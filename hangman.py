
import random

# List of words
words = ["apple", "python", "school", "computer", "flower"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

# ASCII Hangman drawings
stages = [
    """
     +---+
     |   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("=" * 35)
print("       HANGMAN WORD GAME")
print("=" * 35)
print("Guess the hidden word!")
print("You have 6 incorrect guesses.")

# Main game loop
while attempts > 0:

    # Display Hangman drawing
    print(stages[6 - attempts])

    # Display the hidden word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Attempts left:", attempts)

    # Display guessed letters
    if guessed_letters:
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    else:
        print("Guessed letters: None")

    # Check for victory
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Get player's guess
    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Save the guess
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

# Display final result
if attempts == 0:
    print(stages[6])
    print("\nGame over! You ran out of attempts.")
    print("The word was:", secret_word)

print("\nThanks for playing!")
