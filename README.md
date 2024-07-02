Wordle 2.0


This is a self taught Wordle application built with Python and Tkinter using online tutorials. The program helps users solve Wordle puzzles by allowing them to make guesses and providing visual feedback based on the correctness of each guess.

Features
- Randomly selects a word from ANSWERS.txt as the Wordle word.
- Validates user input against GUESS.txt.
- Provides a 6x6 grid for input, mimicking the actual Wordle game.
- Displays colored feedback for each guess:
- Green for correct letters in the correct position.
- Yellow for correct letters in the wrong position.
- Gray for incorrect letters.
- Tracks the number of remaining guesses.
- Displays the correct word if the user fails to guess within six attempts.

Prerequisites
- Python 3.x
- Tkinter (usually included with Python)
- ANSWERS.txt - a file containing the list of possible Wordle answers (one word per line).
- GUESS.txt - a file containing the list of valid guesses (one word per line).

Installation
- Clone the repository or download the source code.
- Ensure you have ANSWERS.txt and GUESS.txt in the same directory as wordle_solver.py.

Running the Program
- Run the file named runWordle.bat
OR
- Open a terminal or command prompt.
- Navigate to the directory containing wordle.py.
- Run the program using Python:
    - python wordle_solver.py

Usage
- Enter a 5-letter word guess into the input field.
- Click the "Submit Guess" button.
- The grid will update to provide feedback:
  - Green for correct letters in the correct position.
  - Yellow for correct letters in the wrong position.
  - Gray for incorrect letters.
- The program will track the number of remaining guesses.
  - If the correct word is guessed, a congratulations message will be displayed.
  - If all guesses are used and the word is not guessed, the correct word will be revealed.

License
- This project is open-source and available under the MIT License.

Acknowledgements
- This project uses the tkinter library for the graphical user interface.
- Word lists used for ANSWERS.txt and GUESS.txt can be sourced from various online Wordle resources.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.
