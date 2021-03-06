all_cells = list('123456789')


def get_board():
    board = {}
    for space in all_cells:
        board[space] = ' '
    return board


def update_board(board, move, player):
    board[move] = player
    return board


def print_board(board):
    b = board
    print(f'''
        {b['1']}|{b['2']}|{b['3']}      1 2 3
        -----
        {b['4']}|{b['5']}|{b['6']}      4 5 6
        -----
        {b['7']}|{b['8']}|{b['9']}      7 8 9
        ''')


def move_is_valid(board, move):
    if board[move] != ' ':
        print('enter valid move, this already taked')
        return False
    return True


def there_is_winner(board, player):
    b, p = board, player
    if      b['1'] == b['2'] == b['3'] == p or \
            b['4'] == b['5'] == b['6'] == p or \
            b['7'] == b['8'] == b['9'] == p or \
            b['1'] == b['5'] == b['9'] == p or \
            b['7'] == b['5'] == b['3'] == p or \
            b['1'] == b['4'] == b['7'] == p or \
            b['2'] == b['5'] == b['8'] == p or \
            b['3'] == b['6'] == b['9'] == p:
        print_board(board)
        print(f'{p} is winner')
        return True
    return False


def there_are_free_cells():
    if ' ' in board.values():
        return True
    return False


current_player, next_player = 'X', 'O'
board = get_board()
print_board(board)

while there_are_free_cells():
    move = input(f'player {current_player} enter your move: ')
    if move_is_valid(board, move):
        update_board(board, move, current_player)
        if there_is_winner(board, current_player):
            exit()
        print_board(board)
        current_player, next_player = next_player, current_player
print('there are no free cells')


