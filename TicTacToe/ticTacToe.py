import sys
import os


class PlayTicTacToe:

    def __init__(self):
        self.row_1 = [1, 2, 3]
        self.row_2 = [4, 5, 6]
        self.row_3 = [7, 8, 9]

        self.rows = [self.row_1, self.row_2, self.row_3]

    def print_rows(self):
        for row in self.rows:
            print('{:^5}|{:^5}|{:^5}'.format(row[0], row[1], row[2]))

    def check_if_won(self):
        if_won = False
        col_1 = []
        col_2 = []
        col_3 = []

        diag_lr = []
        diag_rl = []

        for row in self.rows:
            # Check if rows are same
            if row[0] == row[1] and row[0] == row[2]:
                print('You won! Items in row {} are same.'.format(self.rows.index(row)+1))
                if_won = True
                return if_won

            # get cols
            col_1.append(row[0])
            col_2.append(row[1])
            col_3.append(row[2])

            # get diags
            if self.rows.index(row) == 0:
                diag_lr.append(row[0])
                diag_rl.append(row[2])
            elif self.rows.index(row) == 1:
                diag_lr.append(row[1])
                diag_rl.append(row[1])
            else:
                diag_lr.append(row[2])
                diag_rl.append(row[0])

        # Check if cols are same
        cols = [col_1, col_2, col_3]
        for col in cols:
            if col[0] == col[1] == col[2]:
                print('You won! Items in col {} are same.'.format(cols.index(col)+1))
                if_won = True
                return if_won

        # check if diag are same
        if diag_lr[0] == diag_lr[1] and diag_lr[0] == diag_lr[2]:
            print('You won! Items in left to right diagonal line are same.')
            if_won = True
            return if_won
        elif diag_rl[0] == diag_rl[1] and diag_rl[0] == diag_rl[2]:
            print('You won! Items in right to left diagonal line are same.')
            if_won = True
            return if_won

        return if_won

    def play_game(self, xo):
        while True:
            try:
                player_input = int(input(f'Enter where do you want to place {xo}: '))
            except ValueError:
                print(f'Enter only integers')
            else:
                if player_input == 0:
                    print('You decided to quite the game!')
                    return False
                if self.update_rows(player_input, xo):
                    break

        self.print_rows()
        if_won = self.check_if_won()
        if if_won:
            return False

        return True

    def update_rows(self, player_input, xo):
        player_input = int(player_input) - 1

        row_to_update = int(player_input / 3)
        index_to_update = int(player_input % 3)

        if self.rows[row_to_update][index_to_update] == 'x' or \
           self.rows[row_to_update][index_to_update] == 'o':
            print('You can not overwrite !')
            return False
        else:
            self.rows[row_to_update][index_to_update] = xo
            return True


game = PlayTicTacToe()

keep_playing = True
print('Enter 0 to exit...')
game.print_rows()

player = 'x'
turn_count = 0

while keep_playing:
    # Check if its a tie
    if turn_count < 9:
        keep_playing = game.play_game(player)
        if player == 'x':
            player = 'o'
        else:
            player = 'x'
        turn_count += 1
    else:
        print('That is a Tie!!!')
        keep_playing = False
