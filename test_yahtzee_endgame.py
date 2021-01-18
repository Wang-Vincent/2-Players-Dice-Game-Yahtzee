from unittest import TestCase
import yahtzee


class TestCreateEndgame(TestCase):

    def test_endgame_all_filled_true(self):
        ss1 = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
        ss2 = ['player2', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
        actual = yahtzee.endgame(ss1, ss2)
        expected = True
        self.assertEqual(expected, actual)

    def test_endgame_false_1_empty(self):
        ss1 = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, 0, 0, 0, 50, 13]
        ss2 = ['player2', 3, 6, 6, 4, 5, 6, 0, 0, 0, -1, 0, 50, 13]
        actual = yahtzee.endgame(ss1, ss2)
        expected = False
        self.assertEqual(expected, actual)

    def test_endgame_false_all_empty(self):
        ss1 = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        ss2 = ['player2', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        actual = yahtzee.endgame(ss1, ss2)
        expected = False
        self.assertEqual(expected, actual)