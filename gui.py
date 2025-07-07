import tkinter as tk
from game_logic import Game

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.game = Game()
        self.buttons = []
        self.build_board()
        
    def build_board(self):
        for i in range(3):
            row=[]
            for j in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 36), width=5, height=2,
                                command=lambda x=i, y=j: self.on_click(x, y))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)
            
    def on_click(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.board[row][col])
            winner = self.game.check_winner()
            if winner:
                self.end_game(winner)

    def end_game(self, winner):
        for row in self.buttons:
            for btn in row:
                btn.config(state='disabled')
        print("Winner:", winner)

    def run(self):
        self.root.mainloop()