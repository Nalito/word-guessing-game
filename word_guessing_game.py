import random

def word_guessing_game():
    # List of words to guess
    words = ["python", "developer", "programming", "software", "engineer", "guessing", "project"]
    
    # Randomly select a word from the list
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts = len(word_to_guess) + 3  # Allow more attempts than the word length
    guessed_letters = set()

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word, one letter at a time.")
    print("You have", attempts, "attempts. Good luck!")
    print("Word:", " ".join(guessed_word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1

        print("Word:", " ".join(guessed_word))
        print("Remaining attempts:", attempts)

        # Check if the word is fully guessed
        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word:", word_to_guess)
            break
    else:
        print("Out of attempts! The word was:", word_to_guess)

# Start the game
if __name__ == "__main__":
    word_guessing_game()