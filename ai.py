import math

def minimax(board, depth, is_maximizing):   
    winner = board.check_winner()
    if winner == "X":
        return -1  # X loses
    elif winner == "O":
        return 1  # O wins
    elif board.is_full():
        return 0  # Draw
    
    if is_maximizing:
        best_score = -math.inf
        for (row, col) in board.get_available_moves():
            board.make_move(row, col, "O")
            score = minimax(board, depth + 1, False)
            board.undo_move(row, col)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (row, col) in board.get_available_moves():
            board.make_move(row, col, "X")
            score = minimax(board, depth + 1, True)
            board.undo_move(row, col)
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for (row, col) in board.get_available_moves():
        board.make_move(row, col, "O")
        score = minimax(board, 0, False)
        board.undo_move(row, col)
        
        if score > best_score:
            best_score = score
            best_move = (row, col)
        return best_move