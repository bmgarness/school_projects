import.random
def main():
    game_board = [
        [ ' ', ' ', ' ' ],
        [ ' ', ' ', ' ' ],
        [ ' ', ' ', ' ' ]
        ]
    display_board(game_board)
    user = 0
    if random.randint( 0, 1) == user:
        user = '0'
        computer = 'X'
        whose_turn = 'computer'
    else:
        user = 'X'
        computer = 'O'
        whose_turn = 'user'
    game_over = False
    

def display_board(game_board):
    for r in range(len(game_board)):
        for c in range(len(game_board[r])):
            symbol = ' '
            if game_board [r] [c]:
                symbol = game_board [r] [c]

            print( '_{}_'.format(symbol), end=' ')
            if c in (0, 1):
                print( ' l ', end=' ')
            else:
                print( ' ' )

def get_user_move(game_board, symbol):
    row = int(input( 'What row do you want to play from 0-2?')
    column = int(input( 'What column do you want to play from 0-2?')
    while not is_legal_move(game_board, row, column):
        row = int(input('illegal move, what row do you want to play from 0-2?')
        column = int(input('illegal move, what column do you want to play from 0-2?')
    game_board [row] [column] = symbol

def get_computer_move(game_board, symbol):
    row = random.randint (0, 2)
    column = random.randint (0, 2)
    while not is_legal_move(game_board, row, column):
        row = random.randint (0, 2)
        column = random.randint (0, 2)
    game_board [row] [column] = symbol


def is_legal_move(game_board, row, column):
    if row < 0 or row > 2:
        return False
    if column < 0 or col > 2:
        return False
    if game_board [row] [column]:
        return False

    return True

def has_player_won(game_board, symbol):
    """Check to see if the given symbol has won the game in any of the possible
       ways."""
    
    # Remember, with sequences the multiplication
    # operator repeats the value so 'X' * 3 == 'XXX'
    winner_sequence = symbol * 3 
    
    # Check for horizontal wins
    for r in range(len(game_board)):
        row_symbols = ''
        for c in range(len(game_board[r])):
            row_symbols += game_board[r][c]
        if row_symbols == winner_sequence:
            return True
        
    # Check for vertical wins
    for c in range(len(game_board[0])):
        col_symbols = ''
        for r in range(len(game_board)):
            col_symbols += game_board[r][c]
        if col_symbols == winner_sequence:
            return True
            
    # Check for the two diagonal wins
    # Note this will only work on a square board!
    diag_symbols = ''
    anti_diag_symbols = ''
    for rc in range(len(game_board)):
        diag_symbols += game_board[rc][rc]
        anti_diag_symbols += game_board[rc][len(game_board) - 1 - rc]
    if winner_sequence in (diag_symbols, anti_diag_symbols):
        return True
    
    # If we got here, nobody won yet
    return False
                     
def is_draw(game_board):
    for r in range(len(game_board)):
        for c in range(len(game_board[r])):
            if not game_board [r] [c]:
                return False
    return True
    


main()
    
