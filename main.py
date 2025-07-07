#main.py

from board import Board
from ai import get_best_move

def get_human_move(board):
    while True:
        try:
            move = input("Enter your move (row and column 1-3, e.g. '2 3'): ")
            row, col = map(int, move.strip().split())
            if row in [1,2,3] and col in [1,2,3]:
                if board.is_empty(row-1, col-1):
                    board.make_move(row-1, col-1, "X")
                    break
                else:
                    print("That spot is taken. Try again.")
            else:
                print("Invalid input. Use numbers from 1 to 3.")
        except ValueError:
            print("Invalid format. Enter row and column separated by space.")

def main():
    print("Tic Tac Toe! You are X. AI is O.")
    while True:
        board = Board()
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

        replay = input("Play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
