from game_logic import Wordle
from wordle_graphics import main_loop

def main():
  game = Wordle()
  main_loop(game)

if __name__ == "__main__":
  main()
