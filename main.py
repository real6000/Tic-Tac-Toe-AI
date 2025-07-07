#main.py

def main():
    while True:
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

        replay = input("Play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
