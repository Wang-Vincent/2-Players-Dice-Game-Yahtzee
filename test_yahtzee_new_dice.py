from unittest import TestCase
import yahtzee

class TestNewDice(TestCase):
    def test_new_dice(self):
        actual = yahtzee.new_dice()
        expected = [[], [0, 0, 0, 0, 0]]
        self.assertEqual(expected, actual)
