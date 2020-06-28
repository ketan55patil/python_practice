from .ticTacToe_V2 import PlayTicTacToe
from ddt import ddt, data
import unittest


@ddt
class TestTicTacToeV2(unittest.TestCase):

    def play_game(self, my_input):
        game = PlayTicTacToe()
        input_sequence = my_input
        for item in input_sequence:
            play_status = game.continue_playing(item)
        return play_status

    @data(['a'], [1, 'a'], ['!', 'a'], [-1])
    def test_invalid_input(self, value):
        assert self.play_game(value) == 'invalid'

    @data([1, 1])
    def test_overwrite_value(self, value):
        assert self.play_game(value) == 'overwrite'

    # def test_won_row(self, player, row):
    @data([1, 4, 2, 5, 3], [4, 1, 5, 2, 6, 3], [7, 4, 8, 5, 9], [1, 1, 4, 2, 5, 3])
    def test_won_row(self, value):
        assert self.play_game(value) == 'win'

    # def test_won_col(self, player, col):
    @data([1, 2, 4, 5, 7], [2, 1, 5, 4, 8], [3, 2, 6, 5, 9])
    def test_won_col(self, value):
        assert self.play_game(value) == 'win'

    # def test_won_diag(self, player, diag):
    @data([1, 2, 5, 6, 9], [7, 8, 5, 6, 3])
    def test_won_diag(self, value):
        """ diag could be lr or rl """
        assert self.play_game(value) == 'win'

    @data([1, 5, 9, 2, 8, 7, 3, 6, 4])
    def test_draw(self, value):
        assert self.play_game(value) == 'draw'

    @data([0])
    def test_quit_game(self, value):
        assert self.play_game(value) == False




