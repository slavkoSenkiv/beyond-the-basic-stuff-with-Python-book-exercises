all_cells = list('123456789')
current_player, next_player = 'X', 'O'


class TTTBoard:
    def __init__(self):
        self._board = {}
        for space in all_cells:
            self._board[space] = ' '

    def update_board(self, move, player):
        self._board[move] = player
        return self._board

    def print_board(self):
        b = self._board
        print(f'''
            {b['1']}|{b['2']}|{b['3']}      1 2 3
            -----
            {b['4']}|{b['5']}|{b['6']}      4 5 6
            -----
            {b['7']}|{b['8']}|{b['9']}      7 8 9
            ''')

    def move_is_valid(self, move):
        if self._board[move] != ' ':
            print('enter valid move, this already taked')
            return False
        return True

    def there_is_winner(self, player):
        b, p = self._board, player
        if b['1'] == b['2'] == b['3'] == p or \
                b['4'] == b['5'] == b['6'] == p or \
                b['7'] == b['8'] == b['9'] == p or \
                b['1'] == b['5'] == b['9'] == p or \
                b['7'] == b['5'] == b['3'] == p or \
                b['1'] == b['4'] == b['7'] == p or \
                b['2'] == b['5'] == b['8'] == p or \
                b['3'] == b['6'] == b['9'] == p:
            self.print_board()
            print(f'{p} is winner')
            return True
        return False

    def there_are_free_cells(self):
        if ' ' in self._board.values():
            return True
        return False


class MiniBoard(TTTBoard):
    def print_board(self):
        b = self._board
        for cell in all_cells:
            if b[cell] == ' ':
                b[cell] = '.'

        print(f'''
         {b['1']}{b['2']}{b['3']} 123
         {b['4']}{b['5']}{b['6']} 456
         {b['7']}{b['8']}{b['9']} 789''')

        for cell in all_cells:
            if b[cell] == '.':
                b[cell] = ' '


if input('use mini board? y/n: ').lower().startswith('y'):
    board = MiniBoard()
else:
    board = TTTBoard()

board.print_board()
while board.there_are_free_cells():
    move = input(f'player {current_player} enter your move: ')
    if board.move_is_valid(move):
        board.update_board(move, current_player)
        if board.there_is_winner(current_player):
            exit()
        board.print_board()
        current_player, next_player = next_player, current_player
print('there are no free cells')