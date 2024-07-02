# Wordle2.0
A self taught project using python of the popular game Wordle


This is a Python implementation of the popular word-guessing game Wordle. It incorporates separate word lists for answers and guessable words, and offers a visual interface using Pygame.

Features:

Guess a 5-letter word in 6 tries.
Receive color-coded feedback (green for correct letter in the right spot, yellow for correct letter in the wrong spot, gray for incorrect letter).
Separate files for answer words and guessable words for customization.
Visual interface with a game board and keyboard.

Requirements:

Python 3
Pygame library (pip install pygame)

How to Play:

Clone or download this repository.
Install Pygame: pip install pygame
Run the game: python main.py
Enter your guess and press Enter.
The game will provide feedback based on your guess (green, yellow, or gray).
You have 6 tries to guess the correct word.

Project Structure:

wordle_clone/
├── colors.py      # Defines color constants for the game
├── game_logic.py  # Handles game logic (word selection, guess checking, etc.)
├── wordle-answers.txt  # File containing answer words
├── wordle-guess.txt  # File containing guessable words
├── main.py         # Main script that runs the game
└── wordle_graphics.py  # Implements the visual interface using Pygame

Customization:

You can modify the words in wordle-answers.txt and wordle-guess.txt to personalize your word lists.
The wordle_graphics.py file allows for further customization of the visual interface (colors, fonts, etc.).
Optional Visual Interface:

By default, the game runs in a command-line interface. To enable the visual interface using Pygame, make sure you have Pygame installed and run the game with python main.py.

Contributing:

Feel free to fork this repository and contribute your improvements!
