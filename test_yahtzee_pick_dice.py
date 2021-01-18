from unittest import TestCase
import yahtzee
from unittest.mock import patch


class TestPickDice(TestCase):

    @patch('builtins.input', side_effect=['abc89'])
    def test_pick_dice_no_hold_meaningless_input(self,  mock_input):
        d = [2, 3, 6, 6, 6]
        actual = yahtzee.pick_dice(d)
        expected = [[], [0, 0, 0, 0, 0]]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[''])
    def test_pick_dice_no_hold_empty_input(self, mock_input):
        d = [1, 2, 3, 3, 6]
        actual = yahtzee.pick_dice(d)
        expected = [[], [0, 0, 0, 0, 0]]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1'])
    def test_pick_dice_hold_1(self, mock_input):
        d = [2, 3, 6, 6, 6]
        actual = yahtzee.pick_dice(d)
        expected = [[2], [0, 0, 0, 0]]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['1345'])
    def test_pick_dice_hold_4(self, mock_input):
        d = [1, 2, 2, 3, 6]
        actual = yahtzee.pick_dice(d)
        expected = [[1, 2, 3, 6], [0]]
        self.assertEqual(expected, actual)
