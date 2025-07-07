import tkinter as tk
from game_logic import Game
import ai  # your ai.py

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.game = Game()
        self.buttons = []
        self.build_board()

        self.status_label = tk.Label(self.root, text="Your turn (X)", font=("Arial", 16))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        self.restart_button = tk.Button(self.root, text="Restart", font=("Arial", 14), command=self.restart)
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=10)
        self.restart_button.config(state="disabled")

        self.root.resizable(False, False)

    def build_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(self.root, text="", font=('Arial', 36), width=5, height=2,
                                command=lambda x=i, y=j: self.on_click(x, y))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def on_click(self, row, col):
        if self.game.make_move(row, col):
            self.animate_button(self.buttons[row][col], self.game.board[row][col])
            winner = self.game.check_winner()
            if winner:
                self.end_game(winner)
            else:
                self.status_label.config(text="AI is thinking...")
                self.root.after(500, self.ai_move)  # small delay for effect

    def ai_move(self):
        best_move = ai.get_best_move(self.game)
        if best_move:
            r, c = best_move
            self.game.make_move(r, c)
            self.animate_button(self.buttons[r][c], self.game.board[r][c])
            winner = self.game.check_winner()
            if winner:
                self.end_game(winner)
            else:
                self.status_label.config(text="Your turn (X)")

    def animate_button(self, button, text):
        # Simple fade in animation of button text color from light gray to black
        def step(i=0):
            if i > 10:
                button.config(text=text, fg="black")
                return
            gray_value = 100 + i*15
            color = f"#{gray_value:02x}{gray_value:02x}{gray_value:02x}"
            button.config(text=text, fg=color)
            self.root.after(30, lambda: step(i+1))
        step()

    def end_game(self, winner):
        for row in self.buttons:
            for btn in row:
                btn.config(state='disabled')
        if winner == "Draw":
            self.status_label.config(text="It's a draw!")
        else:
            self.status_label.config(text=f"Winner: {winner}!")
            self.highlight_winner(winner)
        self.restart_button.config(state="normal")

    def highlight_winner(self, winner):
        # Highlight the winning line with color
        lines = []

        # rows
        for i in range(3):
            if all(self.game.board[i][j] == winner for j in range(3)):
                lines.append([(i, j) for j in range(3)])

        # cols
        for j in range(3):
            if all(self.game.board[i][j] == winner for i in range(3)):
                lines.append([(i, j) for i in range(3)])

        # diagonals
        if all(self.game.board[i][i] == winner for i in range(3)):
            lines.append([(i, i) for i in range(3)])

        if all(self.game.board[i][2 - i] == winner for i in range(3)):
            lines.append([(i, 2 - i) for i in range(3)])

        # Apply highlight animation to all winning lines
        for line in lines:
            self.animate_highlight(line)

    def animate_highlight(self, cells):
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        def cycle_color(i=0):
            for (r, c) in cells:
                self.buttons[r][c].config(bg=colors[i % len(colors)])
            self.root.after(300, lambda: cycle_color(i+1))
        cycle_color()

    def restart(self):
        self.game = Game()
        for row in self.buttons:
            for btn in row:
                btn.config(text="", state="normal", bg="SystemButtonFace", fg="black")
        self.status_label.config(text="Your turn (X)")
        self.restart_button.config(state="disabled")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.run()
