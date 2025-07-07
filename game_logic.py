class Game:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        # rows & columns
        for i in range(3):
            if self.board[i][0] != "" and all(self.board[i][j] == self.board[i][0] for j in range(3)):
                return self.board[i][0]
            if self.board[0][i] != "" and all(self.board[j][i] == self.board[0][i] for j in range(3)):
                return self.board[0][i]
        # diagonals
        if self.board[0][0] != "" and all(self.board[i][i] == self.board[0][0] for i in range(3)):
            return self.board[0][0]
        if self.board[0][2] != "" and all(self.board[i][2 - i] == self.board[0][2] for i in range(3)):
            return self.board[0][2]
        # draw
        if all(self.board[i][j] != "" for i in range(3) for j in range(3)):
            return "Draw"
        return None