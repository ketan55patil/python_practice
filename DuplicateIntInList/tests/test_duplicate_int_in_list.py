import pytest
from unittest.mock import patch
from DuplicateIntInList import duplicate_int_in_list as dup


class TestDuplicateIntInList:
    # Using mock decorator
    @patch('builtins.input', side_effect=[1, 2, 3, 'q'])
    def test_get_user_input_decorator(self, mock_inputs):
        assert [1, 2, 3] == dup.DuplicateIntInList.get_user_input(self)

    # # Using mock context manager
    # def test_get_user_input_context(self):
    #     with patch('builtins.input', side_effect=[1, 2, 3, 'q']):
    #         assert [1, 2, 3] == dup.DuplicateIntInList.get_user_input(self)

    @patch('builtins.input', side_effect=['a', 'q'])
    def test_get_user_input_decorator_char_input(self, mock_inputs):
        assert [] == dup.DuplicateIntInList.get_user_input(self)

    @patch('builtins.input', side_effect=[1, 2, 1, 'q'])
    def test_get_user_input_decorator_dup(self, mock_inputs):
        assert [1, 2, 1] == dup.DuplicateIntInList.get_user_input(self)

    @pytest.mark.parametrize('input_list, output_list',
                             [([1, 2, 1], [1]),
                              ([1, 1, 1, 2, 2, 3, 3], [1, 2, 3]),
                              ([4, 1, 1, 2, 2, 3, 3, 5], [1, 2, 3]),
                              ([4, 1, 1, 2, 2, 3, 3, 4], [1, 2, 3, 4])])
    def test_find_duplicates(self, input_list, output_list):
        assert output_list == dup.DuplicateIntInList.find_duplicates(self, input_list)
