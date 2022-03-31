"""The main test module"""
import io
import sys
import unittest
from tic_tac_toe import TicTac


class TestTicTacToe(unittest.TestCase):
    """Test cases to test Tictac methods"""
    def setUp(self):
        self.Tictac = TicTac()
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

    def test_validate_input(self):
        """Test cases to test different input variants"""
        self.Tictac.board = list(range(1, 10))

        # return false to continue the game
        self.assertFalse(self.Tictac.validate_input('1'))

        # return true to ask for new input
        self.assertTrue(self.Tictac.validate_input('100'))

        # return true to ask for new input
        self.assertTrue(self.Tictac.validate_input('aaa'))

        self.Tictac.board[int('2') - 1] = 'X'
        # return true to ask for new input
        self.assertTrue(self.Tictac.validate_input('2'))
        self.Tictac.board = list(range(1, 10))

    def test_check_winner_x(self):
        """Test cases to test different variants of draw and x winning"""
        # check_winner() method - all cells are busy and there is no winner
        # - then it is a draw, return True to stop the game
        for i in range(6):
            if i % 2 == 0:
                self.Tictac.board[i] = 'X'
            else:
                self.Tictac.board[i] = 'O'
        for i in range(6, 9):
            if i % 2 == 0:
                self.Tictac.board[i] = 'O'
            else:
                self.Tictac.board[i] = 'X'
        self.assertTrue(self.Tictac.check_winner())
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - all cells are free -
        # then the game has just started!
        # return False to continue the game
        self.assertFalse(self.Tictac.check_winner())
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the first way,
        # return 'X' to stop the game and show the winner
        for i in (0, 1, 2):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the second way,
        # return 'X' to stop the game and show the winner
        for i in (3, 4, 5):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the third way,
        # return 'X' to stop the game and show the winner
        for i in (6, 7, 8):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the fourth way,
        # return 'X' to stop the game and show the winner
        for i in (0, 3, 6):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the fifth way,
        # return 'X' to stop the game and show the winner
        for i in (1, 4, 7):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the sixth way,
        # return 'X' to stop the game and show the winner
        for i in (2, 5, 8):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the seventh way,
        # return 'X' to stop the game and show the winner
        for i in (0, 4, 8):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the eighth way,
        # return 'X' to stop the game and show the winner
        for i in (2, 4, 6):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    def test_check_winner_o(self):
        """Test cases to test different variants of draw and O winning"""
        # check_winner() method - all cells are busy and there is no winner
        # - then it is a draw, return True to stop the game
        for i in range(6):
            if i % 2 == 0:
                self.Tictac.board[i] = 'O'
            else:
                self.Tictac.board[i] = 'X'
        for i in range(6, 9):
            if i % 2 == 0:
                self.Tictac.board[i] = 'X'
            else:
                self.Tictac.board[i] = 'O'
        self.assertTrue(self.Tictac.check_winner())
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - all cells are free -
        # then the game has just started!
        # return False to continue the game
        self.assertFalse(self.Tictac.check_winner())
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'O' has won the first way,
        # return 'X' to stop the game and show the winner
        for i in (0, 1, 2):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'O' has won the second way,
        # return 'O' to stop the game and show the winner
        for i in (3, 4, 5):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'O' has won the third way,
        # return 'O' to stop the game and show the winner
        for i in (6, 7, 8):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'O' has won the fourth way,
        # return 'O' to stop the game and show the winner
        for i in (0, 3, 6):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'O' has won the fifth way,
        # return 'O' to stop the game and show the winner
        for i in (1, 4, 7):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'O' has won the sixth way,
        # return 'O' to stop the game and show the winner
        for i in (2, 5, 8):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'O' has won the seventh way,
        # return 'O' to stop the game and show the winner
        for i in (0, 4, 8):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))

        # check_winner() method - 'X' has won the eighth way,
        # return 'X' to stop the game and show the winner
        for i in (2, 4, 6):
            self.Tictac.board[i] = 'O'
        self.assertEqual(self.Tictac.check_winner(), 'O')
        self.Tictac.board = list(range(1, 10))


if __name__ == "__main__":
    unittest.main()
