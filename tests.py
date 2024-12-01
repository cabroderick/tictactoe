import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def test_invalid_board(self):
        board = "xoxo\nxoxo\nxoxo\nxoxo "
        try:
            game = TicTacToe(board)
            self.assertTrue(False)
        except ValueError as e:
            self.assertTrue(True)

    def test_is_game_over_true(self):
        board = "x   \nx   \nx   \nx   "
        game = TicTacToe(board)
        self.assertTrue(game.isGameOver())

    def test_is_game_over_false(self):
        board = "x   \nx   \nx   \n    "
        game = TicTacToe(board)
        self.assertFalse(game.isGameOver())

    def test_any_moves_left_true(self):
        board = "xoxo\nxoxo\nxoxo\nxox "
        game = TicTacToe(board)
        self.assertTrue(game.anyMovesLeft())

    def test_any_moves_left_false(self):
        board = "xoxo\nxoxo\nxoxo\nxoxo"
        game = TicTacToe(board)
        self.assertFalse(game.anyMovesLeft())
        
    def test_vertical_win_x(self):
        board = "x   \nx   \nx   \nx   "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "x")
    
    def test_vertical_win_o(self):
        board = "o   \no   \no   \no   "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "o")
    
    def test_horizontal_win_o(self):
        board = "oooo\n    \n    \n    "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "o")
    
    def test_horizontal_win_x(self):
        board = "xxxx\n    \n    \n    "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "x")
    
    def test_diagonal_win_x_top_left_to_bottom_right(self):
        board = "x   \n x  \n  x \n   x"
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "x")
    
    def test_diagonal_win_o_top_left_to_bottom_right(self):
        board = "o   \n o  \n  o \n   o"
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "o")
    
    def test_diagonal_win_x_bottom_left_to_top_right(self):
        board = "   x\n  x \n x  \nx   "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "x")
    
    def test_diagonal_win_o_bottom_left_to_top_right(self):
        board = "   o\n  o \n o  \no   "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "o")
    
    def test_corners_win_x(self):
        board = "x  x\n    \n    \nx  x"
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "x")

    def test_corners_win_o(self):
        board = "o  o\n    \n    \no  o"
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "o")

    def test_2x2_box_win_x(self):
        board = " xx \n xx \n    \n    "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "x")
    
    def test_2x2_box_win_o(self):
        board = " oo \n oo \n    \n    "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "o")
    
    def test_no_winner(self):
        board = "ox  \n ox \n  ox\nox  "
        game = TicTacToe(board)
        self.assertEqual(game.checkWinner(), "")
