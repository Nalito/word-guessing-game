# Word Guessing Game

This is a simple Python-based word guessing game. The player tries to guess a randomly chosen word by guessing one letter at a time. The game provides feedback on whether the guessed letter is correct, and the player wins if they successfully guess all the letters in the word before running out of attempts.

## Features

- Randomly selects a word from a predefined list.
- Allows users to guess one letter at a time.
- Tracks the player's progress by showing the partially guessed word.
- Limits the number of incorrect attempts.
- Provides feedback for repeated or invalid guesses.

## How to Play

1. Run the script in your Python environment:
    ```bash
    python word_guessing_game.py
    ```
2. A random word will be chosen, and you will be prompted to guess one letter at a time.
3. You can guess up to the number of letters in the word plus three additional attempts.
4. Correct guesses reveal the position of the guessed letter in the word.
5. Incorrect guesses reduce the remaining attempts.
6. The game ends when you either guess the word or run out of attempts.

## Example Gameplay

```plaintext
Welcome to the Word Guessing Game!
Try to guess the word, one letter at a time.
You have 10 attempts. Good luck!
Word: _ _ _ _ _ _ _

Enter a letter: p
Good guess!
Word: p _ _ _ _ _ _
Remaining attempts: 10

Enter a letter: z
Wrong guess!
Word: p _ _ _ _ _ _
Remaining attempts: 9

...

Congratulations! You've guessed the word: python
