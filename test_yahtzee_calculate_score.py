from unittest import TestCase
import yahtzee



class TestCalculateScore(TestCase):
    def test_calculate_score_yahtzee(self):
        actual = yahtzee.calculate_score([1, 1, 1, 1, 1], 12)
        expected = 50
        self.assertEqual(actual, expected)

    def test_calculate_score_no_yahtzee(self):
        actual = yahtzee.calculate_score([1, 1, 1, 1, 3], 12)
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_score_1s_left(self):
        actual = yahtzee.calculate_score([1, 1, 1, 2, 3], 1)
        expected = 3
        self.assertEqual(actual, expected)

    def test_calculate_score_no_1s(self):
        actual = yahtzee.calculate_score([2, 2, 3, 4, 6], 1)
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_score_2s_centre(self):
        actual = yahtzee.calculate_score([1, 1, 2, 2, 6], 2)
        expected = 4
        self.assertEqual(actual, expected)

    def test_calculate_score_6s_right(self):
        actual = yahtzee.calculate_score([1, 1, 2, 2, 6], 6)
        expected = 6
        self.assertEqual(actual, expected)

    def test_calculate_score_3_of_a_kind(self):
        actual = yahtzee.calculate_score([2, 2, 2, 4, 6], 7)
        expected = 16
        self.assertEqual(actual, expected)

    def test_calculate_score_full_house_3_of_a_kind(self):
        actual = yahtzee.calculate_score([2, 2, 2, 6, 6], 7)
        expected = 18
        self.assertEqual(actual, expected)

    def test_calculate_score_no_3_of_a_kind(self):
        actual = yahtzee.calculate_score([2, 2, 4, 4, 6], 7)
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_score_4_of_a_kind(self):
        actual = yahtzee.calculate_score([2, 3, 3, 3, 3], 8)
        expected = 14
        self.assertEqual(actual, expected)

    def test_calculate_score_no_4_of_a_kind(self):
        actual = yahtzee.calculate_score([2, 4, 4, 4, 6], 8)
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_score_full_house_right(self):
        actual = yahtzee.calculate_score([2, 2, 4, 4, 4], 9)
        expected = 25
        self.assertEqual(actual, expected)

    def test_calculate_score_full_house_left(self):
        actual = yahtzee.calculate_score([2, 2, 2, 4, 4], 9)
        expected = 25
        self.assertEqual(actual, expected)

    def test_calculate_score_no_full_house(self):
        actual = yahtzee.calculate_score([2, 2, 2, 4, 6], 9)
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_score_small_straight_left(self):
        actual = yahtzee.calculate_score([1, 2, 3, 4, 4], 10)
        expected = 30
        self.assertEqual(actual, expected)

    def test_calculate_score_small_straight_right(self):
        actual = yahtzee.calculate_score([1, 3, 4, 5, 6], 10)
        expected = 30
        self.assertEqual(actual, expected)

    def test_calculate_score_large_straight_small_straight(self):
        actual = yahtzee.calculate_score([2, 3, 4, 5, 6], 10)
        expected = 30
        self.assertEqual(actual, expected)

    def test_calculate_score_no_small_straight(self):
        actual = yahtzee.calculate_score([2, 4, 4, 5, 6], 10)
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_score_smaller_large_straight(self):
        actual = yahtzee.calculate_score([1, 2, 3, 4, 5], 11)
        expected = 40
        self.assertEqual(actual, expected)

    def test_calculate_score_larger_large_straight(self):
        actual = yahtzee.calculate_score([2, 3, 4, 5, 6], 11)
        expected = 40
        self.assertEqual(actual, expected)

    def test_calculate_score_no_large_straight(self):
        actual = yahtzee.calculate_score([1, 3, 4, 5, 6], 11)
        expected = 0
        self.assertEqual(actual, expected)

    def test_calculate_score_chance(self):
        actual = yahtzee.calculate_score([2, 2, 4, 4, 6], 13)
        expected = 18
        self.assertEqual(actual, expected)

    def test_calculate_score_joker_chance(self):
        actual = yahtzee.calculate_score([6, 6, 6, 6, 6], 13)
        expected = 30
        self.assertEqual(actual, expected)