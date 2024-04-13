import chess
import random
import time

def evaluate_board(board):
    # Very basic evaluation function - counts the material
    score = 0
    for piece in board.piece_map().values():
        score += piece.piece_type
    return score

def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board, depth):
    best_move = None
    max_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, alpha, beta, False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

def play_chess():
    board = chess.Board()
    while not board.is_game_over():
        print(board)
        if board.turn == chess.WHITE:
            move = input("Enter your move (in algebraic notation): ")
            try:
                move = chess.Move.from_uci(move)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Invalid move! Try again.")
                    continue
            except:
                print("Invalid input! Try again.")
                continue
        else:
            print("Computer is thinking...")
            time.sleep(2)
            move = get_best_move(board, 3)
            board.push(move)
    print("Game Over")
    print("Result: " + board.result())

if __name__ == "__main__":
    play_chess()
