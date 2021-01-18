from unittest import TestCase
import yahtzee


class TestSortDice(TestCase):
    def test_sort_dice_no_hold(self):
        actual = yahtzee.sort_dice([[], [5, 2, 3, 4, 2]])
        expected = [2, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_sort_dice_hold_1(self):
        actual = yahtzee.sort_dice([[1], [5, 2, 3, 2]])
        expected = [1, 2, 2, 3, 5]
        self.assertEqual(actual, expected)

    def test_sort_dice_hold_2(self):
        actual = yahtzee.sort_dice([[1, 6], [2, 3, 2]])
        expected = [1, 2, 2, 3, 6]
        self.assertEqual(actual, expected)

    def test_sort_dice_max_hold_4(self):
        actual = yahtzee.sort_dice([[1, 6, 2, 5], [3]])
        expected = [1, 2, 3, 5, 6]
        self.assertEqual(actual, expected)

    def test_sort_dice_no_hold_same_min_value(self):
        actual = yahtzee.sort_dice([[], [1, 1, 1, 1, 1]])
        expected = [1, 1, 1, 1, 1]
        self.assertEqual(actual, expected)

    def test_sort_dice_max_hold_same_max_value(self):
        actual = yahtzee.sort_dice([[6, 6, 6, 6], [6]])
        expected = [6, 6, 6, 6, 6]
        self.assertEqual(actual, expected)
