import os

# game constants
PLAYER1_SYMBOL = 'o'
PLAYER2_SYMBOL = 'x'
BOARD_SIZE = 7
NEEDED_TO_WIN = 4 # how many you need to get in a row to win the game


# print function for printing column header/ footer
def print_header_footer():
  print('   ', end='')
  for i in range(BOARD_SIZE):
    print(i, end='  ')
  print()
  

# print board to console function
def print_board(board):
  # print column number header
  print_header_footer()
  # print() # new line

  # print the board itself
  for i in range(BOARD_SIZE):
    print('  ', end=' ')
    for j in range(BOARD_SIZE):
      if board[i][j] == PLAYER1_SYMBOL:
        print(PLAYER1_SYMBOL, end='  ')
      elif board[i][j] == PLAYER2_SYMBOL:
        print(PLAYER2_SYMBOL, end='  ')
      else:
        print('.', end='  ')
    print()
  
  # print column number footer
  print_header_footer()
  print()


# function to prompt player to enter the number of the column they'd like to place their piece in
def player_move_input(player_symbol):
  while True:
    try:
      column = int(input(f'Player {player_symbol}, enter the column number you want to drop your piece into: '))
      if 0 <= column < BOARD_SIZE:
        return column
    except ValueError:
      pass
    print('Invalid input. Please enter a number between 0 and', BOARD_SIZE-1)


# function to check if the move is valid
def is_valid_move(board, column):
  # loop through row #s, starting from the bottom. in this case, the bottom row is the board size - 1
  for i in range(BOARD_SIZE-1, -1, -1):
    # if the row in the specified column is empty ('.'), return the row #
    if board[i][column] == '.':
      return i
  return -1
  

# function to execute a move on the board
def make_move(board, player_symbol, column):
  row = is_valid_move(board, column)

  if row != -1:
    board[row][column] = player_symbol
  else:
    print(f'This column is full. Player {player_symbol}, please try again and enter a different column.')
    make_move(board, player_symbol, player_move_input(player_symbol))


# function to check if the player has won



def play_game():
  board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
  current_player = PLAYER1_SYMBOL

  while True:
    print_board(board)
    column = player_move_input(current_player)
    make_move(board, current_player, column)

    # logic to switch turns
    current_player = PLAYER2_SYMBOL if current_player == PLAYER1_SYMBOL else PLAYER1_SYMBOL


if __name__ == '__main__':
  os.system('cls' if os.name == 'nt' else 'clear') # clear the console
  play_game()