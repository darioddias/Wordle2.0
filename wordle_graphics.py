from random import choice


class Wordle:
    """
    This class represents the Wordle game logic.
    """

    def __init__(self):
        """
        Initializes the game state with a random answer word, empty guess history, and empty feedback list.
        """
        self.answer = self.get_random_word()
        self.current_guess = ""
        self.guesses = []
        self.feedback = []

    def get_random_word(self):
        """
        Reads answer words from the file "wordle-answers.txt" and returns a random word.
        """
        with open("wordle-answers.txt", "r") as f:
            words = f.readlines()
        words = [word.strip() for word in words]  # Remove trailing newline characters
        return choice(words)

    def make_guess(self, guess):
        """
        Stores the uppercase guess, appends it to the guess history, and calculates feedback for the guess.

        Args:
            guess (str): The player's guess in lowercase.
        """
        self.current_guess = guess.upper()
        self.guesses.append(self.current_guess)
        self.feedback = self.check_guess(self.current_guess)

    def check_guess(self, guess):
        """
        Compares the guess with the answer and returns a feedback list indicating correct letter placement ("green"),
        correct letter but wrong placement ("yellow"), or incorrect letter ("gray").

        Args:
            guess (str): The player's guess.

        Returns:
            list: A list of feedback strings for each letter in the guess.
        """
        feedback = []
        for i in range(len(guess)):
            if guess[i] == self.answer[i]:
                feedback.append("green")
            elif guess[i] in self.answer:
                feedback.append("yellow")
            else:
                feedback.append("gray")
        return feedback

    def is_won(self):
        """
        Checks if the current guess matches the answer word.

        Returns:
            bool: True if the guess is correct, False otherwise.
        """
        return self.current_guess == self.answer

    def is_over(self):
        """
        Checks if the maximum number of guesses (6) is reached.

        Returns:
            bool: True if the maximum number of guesses is reached, False otherwise.
        """
        return len(self.guesses) == 6

    def is_valid_guess(self):
        """
        Checks if the current guess is a valid guessable word from the "wordle-guess.list" file.

        (Optional Improvement: Consider storing the guessable words in a set during initialization for faster lookups)

        Returns:
            bool: True if the guess is valid, False otherwise.
        """
        with open("wordle-guess.txt", "r") as f:
            guessable_words = set(word.strip().upper() for word in f)  # Convert to uppercase and store in a set for faster lookup
        return self.current_guess in guessable_words
