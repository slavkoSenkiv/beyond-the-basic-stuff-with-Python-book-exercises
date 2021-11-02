import copy
import pyinputplus

all_cells = list('123456789')
current_player, next_player = 'X', 'O'


class RegularBoard:
    def __init__(self):
        self._board = {}
        for space in all_cells:
            self._board[space] = ' '

    def update_board(self, move, player):
        self._board[move] = player
        return self._board

    def get_board_string(self):
        b = self._board
        board_string = f'''
RegularBoard
{b['1']}|{b['2']}|{b['3']}  1 2 3
-----
{b['4']}|{b['5']}|{b['6']}  4 5 6
-----
{b['7']}|{b['8']}|{b['9']}  7 8 9'''
        return board_string

    def move_is_valid(self, move):
        if self._board[move] != ' ':
            print('enter valid move, this already taked')
            return False
        return True

    def there_is_winner(self, player):
        b, p = self._board, player
        if      b['1'] == b['2'] == b['3'] == p or \
                b['4'] == b['5'] == b['6'] == p or \
                b['7'] == b['8'] == b['9'] == p or \
                b['1'] == b['5'] == b['9'] == p or \
                b['7'] == b['5'] == b['3'] == p or \
                b['1'] == b['4'] == b['7'] == p or \
                b['2'] == b['5'] == b['8'] == p or \
                b['3'] == b['6'] == b['9'] == p:
            return True
        return False

    def there_are_free_cells(self):
        if ' ' in self._board.values():
            return True
        return False


class MiniBoard(RegularBoard):
    def get_board_string(self):
        b = self._board
        for cell in all_cells:
            if b[cell] == ' ':
                b[cell] = '.'

        board_string = f'''
MiniBoard
{b['1']}{b['2']}{b['3']} 123
{b['4']}{b['5']}{b['6']} 456
{b['7']}{b['8']}{b['9']} 789'''

        for cell in all_cells:
            if b[cell] == '.':
                b[cell] = ' '

        return board_string


class HintBoard(RegularBoard):
    def get_board_string(self):
        board_string = super().get_board_string()
        board_string = 'HintBoard' + board_string
        current_player_can_win = False
        next_player_can_win = False
        original_cells = self._board
        for cell in all_cells:

            # Simulate X moving on this space:
            self._board = copy.copy(original_cells)
            if self._board[cell] == ' ':
                self._board[cell] = current_player
                if self.there_is_winner(current_player):
                    board_string += f'\n!!! {current_player} can win with move on {cell}'

            # Simulate O moving on this space:
            self._board = copy.copy(original_cells)
            if self._board[cell] == ' ':
                self._board[cell] = next_player
                if self.there_is_winner(next_player):
                    board_string += f'\n!!! {next_player} can win with move on {cell}'

        self._board = original_cells
        return board_string


board_type = pyinputplus.inputMenu(['regular', 'mini', 'with hints'], numbered=True, prompt='pick board type:\n')
if board_type == 'regular':
    board = RegularBoard()
if board_type == 'mini':
    board = MiniBoard()
if board_type == 'with hints':
    board = HintBoard()


print(board.get_board_string())
while board.there_are_free_cells():
    move = input(f'player {current_player} enter your move: ')
    if board.move_is_valid(move):
        board.update_board(move, current_player)
        if board.there_is_winner(current_player):
            print(board.get_board_string())
            print(f'{current_player} is winner')
            exit()
        print(board.get_board_string())
        current_player, next_player = next_player, current_player
print('there are no free cells')