# wordle_solver.py
import tkinter as tk
from tkinter import messagebox
import random

# Function to read words from a file
def read_word_list(filename):
    with open(filename, 'r') as file:
        return [line.strip().lower() for line in file]

# Read ANSWERS.txt for Wordle words and GUESS.txt for valid guesses
answers = read_word_list('ANSWERS.txt')
guesses = read_word_list('GUESS.txt')

# Select a random word from ANSWERS.txt as the Wordle word
wordle_word = random.choice(answers)

# Initialize variables for tracking guesses
remaining_guesses = 6
current_guess = 0
guessed_letters = set()

# Function to handle guess submission
def submit_guess():
    global remaining_guesses, current_guess

    guess = entry_guess.get().strip().lower()

    if len(guess) != 5 or guess not in guesses:
        messagebox.showerror("Error", "Invalid guess. Please enter a valid 5-letter word.")
        return

    guessed_letters.update(set(guess))
    update_display(guess)

    if guess == wordle_word:
        display_result(f"Congratulations! The word is {wordle_word}")
    else:
        remaining_guesses -= 1
        current_guess += 1
        if remaining_guesses == 0:
            display_result(f"Game Over! The correct word was {wordle_word}")
        else:
            instruction_label.config(text=f"Guess the word ({remaining_guesses} guesses remaining)")

    entry_guess.delete(0, tk.END)

# Function to update display with feedback on guesses
def update_display(guess):
    for i in range(5):
        if guess[i] == wordle_word[i]:
            grid_labels[current_guess][i].config(text=guess[i], bg='green', fg='white')
        elif guess[i] in wordle_word:
            grid_labels[current_guess][i].config(text=guess[i], bg='yellow', fg='black')
        else:
            grid_labels[current_guess][i].config(text=guess[i], bg='gray', fg='white')
    
    guessed_label.config(text=f"Guessed letters: {', '.join(sorted(guessed_letters - set(wordle_word)))}")

# Function to display final result
def display_result(message):
    messagebox.showinfo("Result", message)
    root.destroy()

# Create Tkinter window
root = tk.Tk()
root.title("Wordle by Dario!")
root.geometry("500x600")  # Increase window size

# Create GUI components
instruction_label = tk.Label(root, text=f"Guess the word ({remaining_guesses} guesses remaining)", font=('Helvetica', 14))
instruction_label.pack(pady=10)

grid_frame = tk.Frame(root)
grid_frame.pack(pady=10)

grid_labels = []
for row in range(6):
    row_labels = []
    for col in range(5):
        label = tk.Label(grid_frame, text='_', width=4, height=2, font=('Helvetica', 18), borderwidth=2, relief="groove")
        label.grid(row=row, column=col, padx=5, pady=5)
        row_labels.append(label)
    grid_labels.append(row_labels)

entry_guess = tk.Entry(root, font=('Helvetica', 14))
entry_guess.pack(pady=10)

submit_button = tk.Button(root, text="Submit Guess", command=submit_guess, font=('Helvetica', 14))
submit_button.pack(pady=10)

guessed_label = tk.Label(root, text="Guessed letters: ", font=('Helvetica', 12))
guessed_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
