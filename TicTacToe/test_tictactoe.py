from .ticTacToe import PlayTicTacToe as ptt
import mock
import builtins
import pytest


class TestTicTacToe:

    def test_won_x_row_1(self):
        row_1 = ['x', 'x', 'x']
        row_2 = [4, 5, 6]
        row_3 = [7, 8, 9]

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_x_row_2(self):
        row_1 = [1, 2, 3]
        row_2 = ['x', 'x', 'x']
        row_3 = [7, 8, 9]

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_x_row_3(self):
        row_1 = [1, 2, 3]
        row_2 = [4, 5, 6]
        row_3 = ['x', 'x', 'x']

    def test_won_o_row_1(self):
        row_1 = ['o', 'o', 'o']
        row_2 = [4, 5, 6]
        row_3 = [7, 8, 9]

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_o_row_2(self):
        row_1 = [1, 2, 3]
        row_2 = ['o', 'o', 'o']
        row_3 = [7, 8, 9]

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_o_row_3(self):
        row_1 = [1, 2, 3]
        row_2 = [4, 5, 6]
        row_3 = ['o', 'o', 'o']

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_x_col_1(self):
        row_1 = ['x', 2, 3]
        row_2 = ['x', 5, 6]
        row_3 = ['x', 8, 9]

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_x_col_2(self):
        row_1 = [1, 'x', 3]
        row_2 = [4, 'x', 6]
        row_3 = [7, 'x', 9]

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_x_col_3(self):
        row_1 = [1, 2, 'x']
        row_2 = [4, 5, 'x']
        row_3 = [7, 8, 'x']

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_x_diag_lr(self):
        row_1 = ['x', 2, 3]
        row_2 = [4, 'x', 6]
        row_3 = [7, 8, 'x']

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_o_diag_lr(self):
        row_1 = ['o', 2, 3]
        row_2 = [4, 'o', 6]
        row_3 = [7, 8, 'o']

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_x_diag_rl(self):
        row_1 = [1, 2, 'x']
        row_2 = [4, 'x', 6]
        row_3 = ['x', 8, 9]

        my_rows = [row_1, row_2, row_3]
        assert True == ptt.check_if_won(self, my_rows)

    def test_won_o_diag_rl(self):
        row_1 = [1, 2, 'o']
        row_2 = [4, 'o', 6]
        row_3 = ['o', 8, 9]

        my_rows = [row_1, row_2, row_3]

        assert True == ptt.check_if_won(self, my_rows)

    def test_update_rows_overwrite(self):
        row_1 = [1, 2, 'o']
        row_2 = [4, 'o', 6]
        row_3 = ['o', 8, 9]

        my_rows = [row_1, row_2, row_3]

        assert False == ptt.update_rows(self, 3, 'x', my_rows)

    def test_update_rows_new(self):
        row_1 = [1, 2, 'o']
        row_2 = [4, 'o', 6]
        row_3 = ['o', 8, 9]

        my_rows = [row_1, row_2, row_3]

        assert True == ptt.update_rows(self, 2, 'x', my_rows)

    def test_play_game_quit(self):
        row_1 = [1, 2, 'o']
        row_2 = [4, 'o', 6]
        row_3 = ['o', 8, 9]

        my_rows = [row_1, row_2, row_3]

        with mock.patch.object(builtins, 'input', lambda _: 0):
            assert False == ptt.play_game(self, 'x', my_rows)

    def test_play_game_char_input(self):
        row_1 = [1, 2, 'o']
        row_2 = [4, 'o', 6]
        row_3 = ['o', 8, 9]

        my_rows = [row_1, row_2, row_3]

        with mock.patch.object(builtins, 'input', lambda _: ['a', '!', 0]):
            with pytest.raises(Exception):
                assert ptt.play_game(self, 'x', my_rows)
