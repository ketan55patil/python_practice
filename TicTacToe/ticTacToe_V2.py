
class PlayTicTacToe:

    def __init__(self):
        self.player = 'x'
        self.play_count = 0

        row_1 = [1, 2, 3]
        row_2 = [4, 5, 6]
        row_3 = [7, 8, 9]

        self.rows = [row_1, row_2, row_3]

    def print_rows(self):
        for row in self.rows:
            print('{:^5}|{:^5}|{:^5}'.format(row[0], row[1], row[2]))

    def is_win(self):

        if self.check_rows():
            return True
        elif self.check_cols():
            return True
        elif self.check_diags():
            return True
        else:
            return False

    def check_rows(self, new_rows=''):
        if new_rows == '':
            new_rows = self.rows

        for row in new_rows:
            # print(f'row is {row}')
            if len(set(row)) == 1:
                return True
                break

        return False

    def check_cols(self):
        new_rows = [[self.rows[0][0], self.rows[1][0], self.rows[2][0]],
                    [self.rows[0][1], self.rows[1][1], self.rows[2][1]],
                    [self.rows[0][2], self.rows[1][2], self.rows[2][2]]]
        return self.check_rows(new_rows)

    def check_diags(self):
        new_rows = [[self.rows[0][0], self.rows[1][1], self.rows[2][2]]]
        if self.check_rows(new_rows):
            return True

        new_rows = [[self.rows[0][2], self.rows[1][1], self.rows[2][0]]]
        if self.check_rows(new_rows):
            return True

        return False

    def is_draw(self):
        if self.play_count < 9:
            return False
        else:
            return True

    def is_overwrite(self, row_to_update, index_to_update):
        if self.rows[row_to_update][index_to_update] in ['x', 'o']:
            return True
        else:
            return False

    def update_rows(self, player_input):
        player_input = int(player_input) - 1

        row_to_update = int(player_input / 3)
        index_to_update = int(player_input % 3)

        if not self.is_overwrite(row_to_update, index_to_update):
            self.rows[row_to_update][index_to_update] = self.player
            self.play_count += 1
            return True
        else:
            # print(f'You can not overwrite the value at position {player_input+1}!!! Please try again...')
            return False

    def continue_playing(self, player_input):

        try:
            player_input = int(player_input)
        except ValueError:
            return 'invalid'

        # if player_input < 0 or player_input > 9:
        if not 0 <= player_input <= 9:
            return 'invalid'

        if player_input == 0:
            return False

        if self.update_rows(player_input):
            if self.is_win():
                return 'win'
            elif self.is_draw():
                return 'draw'
        else:
            return 'overwrite'

        # Next player
        if self.player == 'x':
            self.player = 'o'
        else:
            self.player = 'x'

        # print(f'play count is {self.play_count}')
        return True


if __name__ == "__main__":
    game = PlayTicTacToe()

    while True:
        game.print_rows()
        my_player_input = input(f'Enter where do you want to place {game.player}: ')

        play_status = game.continue_playing(my_player_input)
        # print(f'inside main - play status is {play_status}')

        if play_status == 'overwrite':
            print(f'You can not overwrite the value at position {my_player_input}!!! Please try again...')
        elif play_status == 'invalid':
            print(f'Invalid input. Acceptable values are \'1\' to \'9\' or enter \'0\' to exit...')
        elif play_status != True:
            if play_status == 'draw':
                print('Its a draw!!!')
                game.print_rows()
            elif play_status == 'win':
                print(f'Player {game.player} won!!!')
                game.print_rows()
            else:
                print('Thanks for playing!!!')
            break

