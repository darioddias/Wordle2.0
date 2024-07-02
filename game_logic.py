from random import choice

class Wordle:
  def __init__(self):
    self.answer = self.get_random_word()
    self.current_guess = ""
    self.guesses = []
    self.feedback = []

  def get_random_word(self):
    # Read answer words from the file
    with open("wordle-answers.txt", "r") as f:
      words = f.readlines()
    words = [word.strip() for word in words]  # Remove trailing newline characters
    return choice(words)

  def make_guess(self, guess):
    self.current_guess = guess.upper()
    self.guesses.append(self.current_guess)
    self.feedback = self.check_guess(self.current_guess)

  def check_guess(self, guess):
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
    return self.current_guess == self.answer

  def is_over(self):
    return len(self.guesses) == 6

  def is_valid_guess(self):
    # Read guessable words from the file
    with open("wordle-guess.txt", "r") as f:
      words = f.readlines()
    words = [word.strip().upper() for word in words]  # Convert to uppercase for case-insensitive matching
    return self.current_guess in words
