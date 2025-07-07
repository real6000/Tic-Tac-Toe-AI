# main.py

from board import Board
from ai import get_best_move

def get_human_move(board):
    while True:
        try:
            move = input("Enter your move (row and column: 1 1): ").split()
            if len(move) != 2:
                print("Invalid input. Enter two numbers.")
                continue
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if 0 <= row <= 2 and 0 <= col <= 2 and board.make_move(row, col, "X"):
                return
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Use numbers.")

def main():
    board = Board()
    print("Tic Tac Toe! You are X. AI is O.")
    board.display()

    while True:
        get_human_move(board)
        board.display()

        if board.is_winner("X"):
            print("You win!")
            break
        if board.is_full():
            print("It's a draw!")
            break

        row, col = get_best_move(board)
        board.make_move(row, col, "O")
        print("AI moves:")
        board.display()

        if board.is_winner("O"):
            print("AI wins!")
            break
        if board.is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
