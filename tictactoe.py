import re

class TicTacToe:
    def __init__(self, board_str: str):
        pattern = "^[xo ]{4}\n[xo ]{4}\n[xo ]{4}\n[xo ]{4}$" # Regex pattern to validate board input
        if not re.match(pattern, board_str):
            raise ValueError("The inputted board is not valid!")

        rows = board_str.split("\n")
        self.board = [list(row) for row in rows] # Generate a 2D array from the inputted board string

    def checkWinner(self):
        """
        Need to validate for five win conditions:
        1. Vertical
        2. Horizontal
        3. Diagonal
        4. All Four Corners
        5. 2x2 box
        """
        players = ['x', 'o']
        for player in players:
            for pos in range(0, 4):
                if self.board[0][pos] == self.board[1][pos] == self.board[2][pos] == self.board[3][pos] == player: # Vertical
                    return player
                
            if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] == player: # Diagonal top left to bottom right
                return player

            if self.board[3][0] == self.board[2][1] == self.board[1][2] == self.board[0][3] == player: # Diagonal bottom left to top right
                return player

            for row in self.board:
                if row == [player] * 4: # Horizontal
                    return player
                
            if self.board[0][0] == self.board[0][-1] == self.board[-1][0] == self.board[-1][-1] == player: # All Four Corners
                return player
            
            """
            Valid 2x2 combinations:
            (0,0), (0,1), (1,0), (1,1)
            (1,0), (1,1), (2,0), (2,1)
            (2,0), (2,1), (3,0), (3,1)
            (0,1), (0,2), (1,1), (1,2)
            (1,1), (1,2), (2,1), (2,2)
            (2,1), (2,2), (3,1), (3,2)
            (0,2), (0,3), (1,2), (1,3)
            (1,2), (1,3), (2,2), (2,3)
            (2,2), (2,3), (3,2), (3,3)
            """
            for row in range(0,3):
                for col in range(0,3):
                    if self.board[row][col] == self.board[row][col+1] == self.board[row+1][col] == self.board[row+1][col+1] == player:
                        return player

        # No Winner
        return ""

    def anyMovesLeft(self):
        for row in self.board:
            for space in row:
                if space == " ":
                    return True
        return False

    def isGameOver(self):
        winner = self.checkWinner()
        return winner != ""
    