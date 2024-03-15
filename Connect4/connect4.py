import os

# game constants
PLAYER1_SYMBOL = 'o'
PLAYER2_SYMBOL = 'x'
BOARD_SIZE = 7
NEEDED_TO_WIN = 4 # how many you need to get in a row to win the game


# print function for column header/ footer
def print_header_footer():
  print('  ', end='')
  for i in range(BOARD_SIZE):
    print(i, end=' ')
  print()
  

# print board to console
def print_board(board):
  # print column number header
  print_header_footer()
  # print() # new line

  # print the board itself
  for i in range(BOARD_SIZE):
    print(' ', end=' ')
    for j in range(BOARD_SIZE):
      if board[i][j] == PLAYER1_SYMBOL:
        print(PLAYER1_SYMBOL, end=' ')
      elif board[i][j] == PLAYER2_SYMBOL:
        print(PLAYER2_SYMBOL, end=' ')
      else:
        print('.', end=' ')
    print()
  
  # print column number footer
  print_header_footer()
  print()



def play_game():
  board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
  current_player = PLAYER1_SYMBOL

  # while True:
  print_board(board)


if __name__ == '__main__':
  os.system('cls' if os.name == 'nt' else 'clear') # clear the console
  play_game()