import pygame

# Define colors from colors.py
BLACK = ...  # Import from colors.py
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
YELLOW = (200, 200, 0)
GRAY = (128, 128, 128)

# Define screen dimensions
WIDTH = 400
HEIGHT = 600
BOARD_WIDTH = 5  # Number of letter columns
BOARD_HEIGHT = 6  # Number of guess rows
CELL_SIZE = 60  # Size of each letter square on the board
KEY_WIDTH = WIDTH // 10  # Width of each keyboard key
KEY_HEIGHT = 40  # Height of each keyboard key
X_MARGIN = (WIDTH - BOARD_WIDTH * CELL_SIZE) // 2  # Center the board horizontally
Y_MARGIN = (HEIGHT - BOARD_HEIGHT * CELL_SIZE - KEY_HEIGHT * 2) // 2  # Margin between board and keyboard

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle Clone")

# Font for text rendering
font = pygame.font.Font(None, 32)


def draw_board(guesses, feedback):
  # Draw the board grid
  for y in range(BOARD_HEIGHT):
    for x in range(BOARD_WIDTH):
      pygame.draw.rect(screen, BLACK, (X_MARGIN + x * CELL_SIZE, Y_MARGIN + y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

  # Draw the letters based on guesses and feedback
  for y in range(BOARD_HEIGHT):
    for x in range(BOARD_WIDTH):
      if y < len(guesses):
        text_surface = font.render(guesses[y][x], True, BLACK)
        x_offset = (CELL_SIZE - text_surface.get_width()) // 2
        y_offset = (CELL_SIZE - text_surface.get_height()) // 2
        screen.blit(text_surface, (X_MARGIN + x * CELL_SIZE + x_offset, Y_MARGIN + y * CELL_SIZE + y_offset))
      if y < len(guesses) and feedback:
        color = GREEN if feedback[y][x] == "green" else (YELLOW if feedback[y][x] == "yellow" else GRAY)
        pygame.draw.rect(screen, color, (X_MARGIN + x * CELL_SIZE, Y_MARGIN + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_keyboard(unused_keys, pressed_keys):
  # Draw the keyboard keys
  for i in range(26):
    row = i // 10
    col = i % 10
    x = col * KEY_WIDTH + X_MARGIN
    y = row * KEY_HEIGHT + Y_MARGIN + BOARD_HEIGHT * CELL_SIZE
    key = chr(ord('a') + i)
    text_surface = font.render(key.upper(), True, BLACK)
    if key in pressed_keys:
      pygame.draw.rect(screen, GRAY, (x, y, KEY_WIDTH, KEY_HEIGHT))
    else:
      pygame.draw.rect(screen, WHITE, (x, y, KEY_WIDTH, KEY_HEIGHT), 1)
    screen.blit(text_surface, (x + (KEY_WIDTH - text_surface.get_width()) // 2, y + (KEY_HEIGHT - text_surface.get_height()) // 2))


def draw_text(text, x, y):
  text_surface = font.render(text, True, BLACK)
  screen.blit(text_surface, (x, y))


def handle_key_press(game, key):
  if game.is_over() or game.is_won():
    return
  if key in game.is_valid_guess():
    game.make_guess(key)
  elif key == chr(pygame.K_BACKSPACE):  # Handle backspace to erase letters
    if game.current_guess:
      game.current_guess = game.current_guess[:-1]


