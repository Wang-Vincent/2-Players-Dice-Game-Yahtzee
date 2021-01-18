from unittest import TestCase
import yahtzee


class TestCreateScoresheet(TestCase):

    def test_create_score_sheet(self):
        player_name = 'player1'
        actual = yahtzee.create_score_sheet(player_name)
        expected = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.assertEqual(expected, actual)
