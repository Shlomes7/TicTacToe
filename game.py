from tictactoe_lib import *
board = init_board()
turn = 1 # turn number
while True:
    if check_winner(board): ### winner check
        _, the_winner_is = check_winner(board)
        print(the_winner_is)
        if ask_play_again():
            board = init_board() # reset board
            turn = 1 # reset turn number
        else:
            print('Good match, goodbye!')
            break
    elif turn == 10: ### draw check
        print('the board is full! DRAW')
        if ask_play_again():
            board = init_board() # reset board
            turn = 1 # reset turn number
        else:
            print('Good match, goodbye!')
            break
    else: # The game continues
        row, col = get_move(board) # if the move is valid, the move's coordinates are given
        board[row][col] = player_turn(turn) # the move is implemented into the board based on the appropriate player's move
        print_board(board)
        turn += 1
