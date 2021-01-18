from unittest import TestCase
import yahtzee
from unittest.mock import patch


class TestRecordScore(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_record_score_single_numbers_one_match(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [1, 2, 2, 3, 6]
        yahtzee.record_score(sd, ss)
        expected = ['player1', 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['6'])
    def test_record_score_single_numbers_4_match(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [2, 6, 6, 6, 6]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, 24, -1, -1, -1, -1, -1, -1, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['7'])
    def test_record_score_3_of_a_kind(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [2, 2, 2, 3, 6]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, 15, -1, -1, -1, -1, -1, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['8'])
    def test_record_score_4_of_a_kind(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [1, 1, 1, 1, 6]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['9'])
    def test_record_score_full_house(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [3, 3, 3, 5, 5]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, 25, -1, -1, -1, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['10'])
    def test_record_score_small_straight(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [2, 3, 3, 4, 5]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, 30, -1, -1, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['11'])
    def test_record_score_large_straight(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [1, 2, 3, 4, 5]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 40, -1, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['12'])
    def test_record_score_first_yahtzee(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [3, 3, 3, 3, 3]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 50, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['12'])
    def test_record_score_second_yahtzee(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 50, -1]
        sd = [6, 6, 6, 6, 6]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 150, -1]
        actual = ss
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['12'])
    def test_record_score_zero(self, mock_input):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        sd = [2, 3, 3, 4, 4]
        yahtzee.record_score(sd, ss)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, -1]
        actual = ss
        self.assertEqual(actual, expected)
