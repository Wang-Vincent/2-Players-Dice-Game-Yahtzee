from unittest import TestCase
import yahtzee


class TestCalculateTotal(TestCase):
    def test_calculate_total_empty(self):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        actual = yahtzee.calculate_total(ss)
        expected = -1
        self.assertEqual(actual, expected)

    def test_calculate_total_1_unfill(self):
        ss = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, -1, 0, 0, 50, 13]
        actual = yahtzee.calculate_total(ss)
        expected = -1
        self.assertEqual(actual, expected)

    def test_calculate_total_with_upper_bonus(self):
        ss = ['player1', 3, 8, 3, 12, 20, 24, 0, 0, 25, 0, 0, 50, 13]
        actual = yahtzee.calculate_total(ss)
        expected = 193
        self.assertEqual(actual, expected)

    def test_calculate_total_no_upper_bonus(self):
        ss = ['player1', 3, 8, 3, 12, 0, 0, 0, 0, 25, 0, 0, 50, 13]
        actual = yahtzee.calculate_total(ss)
        expected = 114
        self.assertEqual(actual, expected)
