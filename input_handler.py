# input_handler.py

def get_valid_guess():
    """
    Prompts the user to enter a valid guess word for Wordle.
    Validates the input to ensure it meets the criteria.
    Returns the valid guess word.
    """
    while True:
        guess = input("Enter your guess (5-letter word with unique letters): ").strip().lower()
        if len(guess) == 5 and len(set(guess)) == 5:
            return guess
        else:
            print("Invalid guess. Please enter a 5-letter word with unique letters.")
