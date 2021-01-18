from unittest import TestCase
import yahtzee
from unittest.mock import patch
import io


@patch('sys.stdout', new_callable=io.StringIO)
class TestPrintSheet(TestCase):

    def test_print_sheet_empty(self, mock_stdout):
        ss = ['player1', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        ts = -1
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player1\n1. Aces:\n2. 2s:\n3. 3s:\n4. 4s:\n5. 5s:\n6. 6s:\n7. 3 of a kind:\n' \
                   '8. 4 of a kind:\n9. Full House:\n10. Small Straight:\n11. Large Straight:\n12. Yahtzee:\n' \
                   '13. Chance:\nSum of Upper Section:\nBonus:\nSum of Lower Section:\nTotal Score:' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_sheet_player_name_player2(self, mock_stdout):
        ss = ['player2', -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        ts = -1
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player2\n1. Aces:\n2. 2s:\n3. 3s:\n4. 4s:\n5. 5s:\n6. 6s:\n7. 3 of a kind:\n' \
                   '8. 4 of a kind:\n9. Full House:\n10. Small Straight:\n11. Large Straight:\n12. Yahtzee:\n' \
                   '13. Chance:\nSum of Upper Section:\nBonus:\nSum of Lower Section:\nTotal Score:' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_sheet_1_unfilled_no_bonus(self, mock_stdout):
        ss = ['player1', 3, 6, 6, 4, 5, 6, 0, 0, -1, 0, 0, 50, 13]
        ts = -1
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player1\n1. Aces:3\n2. 2s:6\n3. 3s:6\n4. 4s:4\n5. 5s:5\n6. 6s:6\n7. 3 of a kind:0\n' \
                   '8. 4 of a kind:0\n9. Full House:\n10. Small Straight:0\n11. Large Straight:0\n12. Yahtzee:50\n' \
                   '13. Chance:13\nSum of Upper Section:30\nBonus:0\nSum of Lower Section:\nTotal Score:' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_sheet_full_lower(self, mock_stdout):
        ss = ['player1', -1, -1, -1, -1, -1, -1, 0, 0, 25, 30, 40, 50, 18]
        ts = -1
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player1\n1. Aces:\n2. 2s:\n3. 3s:\n4. 4s:\n5. 5s:\n6. 6s:\n7. 3 of a kind:0\n' \
                   '8. 4 of a kind:0\n9. Full House:25\n10. Small Straight:30\n11. Large Straight:40\n12. Yahtzee:50\n'\
                   '13. Chance:18\nSum of Upper Section:\nBonus:\nSum of Lower Section:163\nTotal Score:' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_sheet_full_upper_no_bonus(self, mock_stdout):
        ss = ['player1', 3, 6, 6, 4, 5, 6, -1, -1, -1, -1, -1, -1, -1]
        ts = -1
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player1\n1. Aces:3\n2. 2s:6\n3. 3s:6\n4. 4s:4\n5. 5s:5\n6. 6s:6\n7. 3 of a kind:\n' \
                   '8. 4 of a kind:\n9. Full House:\n10. Small Straight:\n11. Large Straight:\n12. Yahtzee:\n' \
                   '13. Chance:\nSum of Upper Section:30\nBonus:0\nSum of Lower Section:\nTotal Score:' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_sheet_full_upper_with_bonus(self, mock_stdout):
        ss = ['player1', 6, 12, 18, 20, 10, 30, -1, -1, -1, -1, -1, -1, -1]
        ts = -1
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player1\n1. Aces:6\n2. 2s:12\n3. 3s:18\n4. 4s:20\n5. 5s:10\n6. 6s:30\n7. 3 of a kind:\n' \
                   '8. 4 of a kind:\n9. Full House:\n10. Small Straight:\n11. Large Straight:\n12. Yahtzee:\n' \
                   '13. Chance:\nSum of Upper Section:96\nBonus:35\nSum of Lower Section:\nTotal Score:' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_sheet_complete_with_bonus_1_yahtzee(self, mock_stdout):
        ss = ['player1', 3, 8, 3, 12, 20, 24, 0, 0, 0, 0, 0, 50, 13]
        ts = 168
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player1\n1. Aces:3\n2. 2s:8\n3. 3s:3\n4. 4s:12\n5. 5s:20\n6. 6s:24\n7. 3 of a kind:0\n' \
                   '8. 4 of a kind:0\n9. Full House:0\n10. Small Straight:0\n11. Large Straight:0\n12. Yahtzee:50\n' \
                   '13. Chance:13\nSum of Upper Section:70\nBonus:35\nSum of Lower Section:63\nTotal Score:168' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_sheet_complete_2_yahtzee(self, mock_stdout):
        ss = ['player1', 3, 8, 3, 12, 20, 24, 0, 0, 25, 0, 0, 150, 13]
        ts = 293
        yahtzee.print_sheet(ss, ts)
        expected = '-------------------------\nYahtzee Score Sheet\n-------------------------\n' \
                   'Player:player1\n1. Aces:3\n2. 2s:8\n3. 3s:3\n4. 4s:12\n5. 5s:20\n6. 6s:24\n7. 3 of a kind:0\n' \
                   '8. 4 of a kind:0\n9. Full House:25\n10. Small Straight:0\n11. Large Straight:0\n12. Yahtzee:150\n' \
                   '13. Chance:13\nSum of Upper Section:70\nBonus:35\nSum of Lower Section:188\nTotal Score:293' \
                   '\n-------------------------\n'
        self.assertEqual(mock_stdout.getvalue(), expected)
