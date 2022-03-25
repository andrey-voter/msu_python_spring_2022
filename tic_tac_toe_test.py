import unittest
from tic_tac_toe import TicTac
# Test cases to test Tictac methods


class Test_tic_tac_toe(unittest.TestCase):

    def setUp(self):
        self.Tictac = TicTac()

    # validate_input() method - given number from [1, 9],
    # return 0 to continue the game
    def test_validate_input_correct_number(self):
        self.Tictac.board = list(range(1, 10))
        self.assertEqual(self.Tictac.validate_input('1'), 0)

    # validate_input() method - given number not from [1, 9],
    # return 1 to ask player to input again
    def test_validate_input_incorrect_number(self):
        self.assertEqual(self.Tictac.validate_input('100'), 1)

    # validate_input() method - given not a number,
    # return 1 to ask player to input again
    def test_validate_input_not_number(self):
        self.assertEqual(self.Tictac.validate_input('aaa'), 1)

    # validate_input() method - given a number from [1, 9],
    # but the cell is already busy
    # return 1 to ask player to input again
    def test_validate_input_busy_cell(self):
        self.Tictac.board[int('2') - 1] = 'X'
        self.assertEqual(self.Tictac.validate_input('2'), 1)
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - all cells are busy and there is no winner
    # - then it is a draw, return 1 to stop the game
    def test_check_winner_draw(self):
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
        self.assertEqual(self.Tictac.check_winner(), 1)
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - all cells are free -
    # then the game has just started!
    # return 0 to continue the game
    def test_check_winner0(self):
        self.assertEqual(self.Tictac.check_winner(), 0)

    # check_winner() method - 'X' has won the first way,
    # return 'X' to stop the game and show the winner
    def test_check_winner1(self):
        for i in (0, 1, 2):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - 'X' has won the second way,
    # return 'X' to stop the game and show the winner
    def test_check_winner2(self):
        for i in (3, 4, 5):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - 'X' has won the third way,
    # return 'X' to stop the game and show the winner
    def test_check_winner3(self):
        for i in (6, 7, 8):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - 'X' has won the fourth way,
    # return 'X' to stop the game and show the winner
    def test_check_winner4(self):
        for i in (0, 3, 6):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - 'X' has won the fifth way,
    # return 'X' to stop the game and show the winner
    def test_check_winner5(self):
        for i in (1, 4, 7):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - 'X' has won the sixth way,
    # return 'X' to stop the game and show the winner
    def test_check_winner6(self):
        for i in (2, 5, 8):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - 'X' has won the seventh way,
    # return 'X' to stop the game and show the winner
    def test_check_winner7(self):
        for i in (0, 4, 8):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))

    # check_winner() method - 'X' has won the eighth way,
    # return 'X' to stop the game and show the winner
    def test_check_winner8(self):
        for i in (2, 4, 6):
            self.Tictac.board[i] = 'X'
        self.assertEqual(self.Tictac.check_winner(), 'X')
        self.Tictac.board = list(range(1, 10))


if __name__ == "__main__":
    unittest.main()
