from tictactoe import TicTacToe
    
filename = "board.txt"
board_str = open(filename, "r").read()
game = TicTacToe(board_str)
if game.isGameOver():
    print(f"The winner is {game.checkWinner()}!")
else:
    print("There is no winner!")
