import math

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.current_winner = None
        
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        # Check column
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in col]):
            return True

        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False
    

def minimax(state, player):
    max_player = 'X'  # AI
    other_player = 'O' if player == 'X' else 'X'

    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (len(state.available_moves()) + 1) if other_player == max_player else -1 * (len(state.available_moves()) +1)}

    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -math.inf}
    else:
        best = {'position': None, 'score': math.inf}

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax(state, other_player)
        state.board[possible_move] = ' '
        state.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
    return best

def play():
    t = TicTacToe()
    player_letter = 'O'
    ai_letter = 'X'
    t.print_board()
    
    while t.empty_squares():
        #player move
        valid_move = False
        while not valid_move:
            move = input("Your move (0-8): ")
            try:
                move = int(move)
                if move in t.available_moves():
                    valid_move = True
                    t.make_move(move, player_letter)
                else:
                    print("Invalid move. Try again.")
            except:
                print("Please enter a number between 0 and 8.")

        t.print_board()
        
        if t.current_winner:
            print("You win!")
            return

        if not t.empty_squares():
            print("Tie game!")
            return
        
        #AI MOVE
        print("AI is thinking...")
        move = minimax(t, ai_letter)['position']
        t.make_move(move, ai_letter)
        t.print_board()
        
        if t.current_winner:
            print("AI wins!")
            return
        
    print("It's a tie!")
    
if __name__ == '__main__':
    play()