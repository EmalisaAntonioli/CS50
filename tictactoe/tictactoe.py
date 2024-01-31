"""
Tic Tac Toe Player
"""

import math
import random
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    no_of_moves = sum(row.count(EMPTY) for row in board)
    if no_of_moves % 2 == 1:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Deep copy the board to leave the original unchanged
    new_board = copy.deepcopy(board)

    # Check if the move is valid
    if new_board[action[0]][action[1]] is not EMPTY:
        raise Exception ("Invalid move")
    
    # Perform action
    player_ = player(board)
    new_board[action[0]][action[1]] = player_

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
        # Check if X won
    for row in board:
        if row.count(X) == 3:
            return X

    for i in range(3):
        if all(board[j][i] == X for j in range(3)):
            return X
        
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]

    if diagonal_1.count(X) == 3 or diagonal_2.count(X) == 3:
        return X
        
    # Check if O won
    for row in board:
        if row.count(O) == 3:
            return O

    for i in range(3):
        if all(board[j][i] == O for j in range(3)):
            return O
        
    if diagonal_1.count(O) == 3 or diagonal_2.count(O) == 3:
        return X
        
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if all cells are filled 
    if not any(EMPTY in row for row in board):
        return True

    if winner(board): return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_ = winner(board)
    if winner_ == X: return 1
    if winner_ == O: return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    # Check if the opposition could win in one move and make that move
    check_opposition_ = check_opposition(board)
    if check_opposition_:
        return check_opposition_

    # Else make a move with the most preferred score
    if player(board) == X:
        return max_value(board, -10, 10)[0]
    else:
        return min_value(board, -10, 10)[0]
    
def check_opposition(board):
    # Checks if the coming move could be a terminal one for the opposition
    # Return the action that belongs to that

    # Get the opposite player of whose turn it actually is
    player_ = None
    player_ = O if player(board) == X else X

    # See if any of the current possible actions could lead to a win for the opposition
    for action in actions(board):
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player_

        if terminal(new_board): return action

    # Return None if no terminal boards were found
    return None

    
def max_value(board, max_score, min_score):
    # Return when a terminal board is found
    if terminal(board): return(None, utility(board))
    # Initiate best move instance
    best_move = (None, None)

    for action in actions(board):
        # Get the lowest possible score for the next move, as this is what the opponent will choose
        score = min_value(result(board, action), max_score, min_score)[1]

        # Check if this score is the highest thus far
        if score > max_score:
            max_score = score
            
        best_move = (action, score)

        # Prune when max_score exceeds or equals min_score
        # Not entirely sure about this
        if max_score >= min_score:
            break

    return best_move

def min_value(board, max_score, min_score):
    # Return when a terminal board is found
    if terminal(board): return(None, utility(board))

    # Initiate best move instance
    best_move = (None, None)

    for action in actions(board):
        # Get the lowest possible score for the next move, as this is what the opponent will choose
        score = max_value(result(board, action), max_score, min_score)[1]


        # Check if this score is the highest thus far
        if score < min_score:
            min_score = score
            
        best_move = (action, score)

        # Prune when max_score exceeds or equals min_score
        if min_score <= max_score:
            break

    return best_move
