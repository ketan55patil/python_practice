from .ticTacToe_V2 import PlayTicTacToe
import mock
import builtins

class TestTicTacToeV2:

    def play_game(self, my_input):
        game = PlayTicTacToe()
        input_sequence = my_input
        for item in input_sequence:
            play_status = game.continue_playing(item)
        return play_status

    def test_invalid_input(self):
        assert self.play_game([1, 'a']) == 'invalid'

    def test_overwrite_value(self):
        assert self.play_game([1, 1]) == 'overwrite'

    # def test_won_row(self, player, row):
    def test_won_row(self):
        assert self.play_game([1, 4, 2, 5, 3]) == 'win'

    # def test_won_col(self, player, col):
    def test_won_col(self):
        assert self.play_game([1, 2, 4, 5, 7]) == 'win'

    # def test_won_diag(self, player, diag):
    def test_won_diag(self):
        """ diag could be lr or rl """
        assert self.play_game([1, 2, 5, 6, 9]) == 'win'

    def test_draw(self):
        assert self.play_game([1, 5, 9, 2, 8, 7, 3, 6, 4]) == 'draw'

    def test_quit_game(self):
        assert self.play_game([0]) == False




