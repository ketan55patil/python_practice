from .ticTacToe_V2 import PlayTicTacToe
from ddt import ddt, data, unpack
import unittest


@ddt
class TestTicTacToeV2(unittest.TestCase):

    @data([['a'], ['invalid']],
          [[1, 'a'], [True, 'invalid']],
          [['!', 'a'], ['invalid', 'invalid']],
          [[-1], ['invalid']],
          [[1, 1], [True, 'overwrite']],
          [[1, 4, 2, 5, 3], [True, True, True, True, 'win']],
          [[4, 1, 5, 2, 6], [True, True, True, True, 'win']],
          [[7, 4, 8, 5, 9], [True, True, True, True, 'win']],
          [[1, 1, 4, 2, 5, 3], [True, 'overwrite', True, True, True, 'win']],
          [[1, 2, 4, 5, 7], [True, True, True, True, 'win']],
          [[2, 1, 5, 4, 8], [True, True, True, True, 'win']],
          [[3, 2, 6, 5, 9], [True, True, True, True, 'win']],
          [[1, 2, 5, 6, 9], [True, True, True, True, 'win']],
          [[7, 8, 5, 6, 3], [True, True, True, True, 'win']],
          [[1, 5, 9, 2, 8, 7, 3, 6, 4], [True, True, True, True, True, True, True, True, 'draw']],
          [[0], [False]])
    @unpack
    def test_overwrite_value(self, user_input, output):
        game = PlayTicTacToe()
        for index, value in enumerate(user_input):
            assert game.continue_playing(value) == output[index]
