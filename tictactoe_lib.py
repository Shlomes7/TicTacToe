def init_board():
    """
    builds a fresh 3x3 board of empty squares, returns it
    :return: an empty 3x3 board
    """
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    return board

def print_board(board):
    """
    prints the board, row by row
    :param board: an empty 3x3 board
    :return: a 3x3 Tic-Tac-Toe board
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def get_move(board, mark=0):
    """
    asks the player for a square (1-9), validates it, returns (row, col)
    :param board: a 3x3 Tic-Tac-Toe board with or without marks
    :param mark: the player move
    :return: the row, col for the player's mark, only if valid.
    """
    row = 0
    col = 0
    while True:
        if 1 <= mark <= 9:
            match mark:
                case 1 | 2 | 3:
                    row = 0
                    col = mark - 1
                case 4 | 5 | 6:
                    row = 1
                    col = mark - 4
                case _:
                    row = 2
                    col = mark - 7
            if board[row][col] == " ":
                break
            else:
                print('already been marked! ')
                mark = 0
                continue
        else:
            try:
                mark = int(input("Enter a number (1-9): "))
            except ValueError:
                print("Please enter a number 1-9")
            else:
                if mark < 1 or mark > 9:
                    print("Please enter a number 1-9")
    return row, col




def check_winner(board):
    """
    returns True if mark has three in a row, column, or diagonal
    :param board: the playing board with player marks
    :return: True/False if there is a winner, if there is one returns its name
    """
    x_wins = False
    o_wins = False
    row = 0
    col = 0
    for _ in range(3): # row check
        x_wins = True if board[row][0] == board[row][1] == board[row][2] == 'X' else False
        o_wins = True if board[row][0] == board[row][1] == board[row][2] == 'O' else False
        row += 1
        if x_wins:
            return True, "the winner is X!"
        elif o_wins:
            return True, "the winner is O!"

    for _ in range(3): # column check
        x_wins = True if board[0][col] == board[1][col] == board[2][col] == 'X' else False
        o_wins = True if board[0][col] == board[1][col] == board[2][col] == 'O' else False
        col += 1
        if x_wins:
            return True, "the winner is X!"
        elif o_wins:
            return True, "the winner is O!"

    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        x_wins = True
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        o_wins = True

    if  x_wins:
        return True, "the winner is X!"
    elif o_wins:
        return True, "the winner is O!"
    else:
        return False

def ask_play_again():
    """
    asks the player if he wants to play another round
    :return: True/False whether he wants to play another round
    """
    play_again = input("do you want to play again? (y/n): ")
    if play_again == "y":
        return True
    return False

def player_turn(turn = 1):
    """
    checks which player is playing ('X' or 'O') based on the turn number
    :param turn: the turn number
    :return: 'X'/'O' depends on the turn
    """
    if turn % 2 == 1:
        playing_player = 'X'
    else:
        playing_player = 'O'
    return playing_player


