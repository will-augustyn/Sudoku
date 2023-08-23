from boardClass import Board
from boardClass import box_ids

def back_propogation_solver(board):
    """Solve a sodoku using backpropogation. Options index keeps track of 
    which sodoku tile you're on. Current moves keeps track of which numbers you
    have treid for a given tile."""
    if board.next_empty() == None:
        print("Solved!")
        print(board)
        return True 
    else:
        next_empty = board.next_empty()
        row = next_empty[0]
        col = next_empty[1]
        for x in range(1, 10):
            if board.check_placement(row, col, x) == True:
                board.nums[row][col] = x
                new_b = back_propogation_solver(board)
                if new_b == True:
                    return True 
        board.nums[row][col] = 0
        return False
    
def stochastic_solver(board):
    options = []