#board.py

class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        
    def display(self):
        print("\n")
        for i in range(3):
            row = " | ".join(self.grid[i])
            print(f" {row} ")
            if i < 2:
                print("---+---+---")
        print("\n")
        
    def make_move(self, row, col, player):
        if self.grid[row][col] == " ":
            self.grid[row][col] = player
            return True
        return False
    
    def is_winner(self, player):
        #check rows, columns
        for i in range(3):
            if all(self.grid[i][j] == player for j in range(3)):
                return True
            if all(self.grid[j][i] == player for j in range(3)):
                return True
        # Diagonals
        if all(self.grid[i][i] == player for i in range(3)):
            return True
        if all(self.grid[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def is_full(self):
        return all(self.grid[i][j] != " " for i in range(3) for j in range(3))

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.grid[i][j] == " "]