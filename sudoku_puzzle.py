# Credits to freecodecamp:  12 Beginner Python Projects (youtube) and kying18 (github)
from pprint import pprint

def find_next_empty(puzzle):
    # find the next row, col on the puzzle that's not filled yet ---> rep with -1
    # return row, col tuple (or (None,None) if there is none)
    # we are zero indexing, therefore, keeping in mind that we are going to use 0-8 for our indices

    for r in range(9):
        for c in range(9): # range(9) = 0,1,2,...,8
            if puzzle[r][c] == -1:
                return r,c 
            
    return None,None       # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle,guess,row,col): 
    # the four parameters that we need for validation of the guess in the row/col
    # returns value True or False, based on if the guess is valid or not respectively

    # starting with the row:
    row_vals  =  puzzle[row] # the row in [] indicates the value on this index of this puzzle
    if guess in row_vals:    # if the row_vals is equal to our inserted number then return false 
        return False

    # now for the columns:
    # col_vals = [] --> indicates empty list
    # for i in range(9):
    #     col_vals.append(puzzle[i][col]) --> puzzle[i][col] can be vizualized as 2D matrix 
    col_vals = [puzzle[i][col] for i in range(9)]    # using list comprehension
    if guess in col_vals:
        return False    
    
    # now the tricky part is the square as we have to find the starting index of the row of the 3x3 matrix 
    # and the starting index of the column , then we shall iterate over the 3 values in the row/col
    # iterate means repeat the process 3 times for all the chunks of the puzzle i.e. the 3x3 squares

    row_start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1,.... i.e. we opt for whole number and omit the decimal(the reminder part) 
    col_start = (col // 3) * 3 

    for r in range(row_start,row_start + 3):
        for c in range(col_start,col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    # if we get here, these checks pass
        return True
 

def solve_sudoku(puzzle):
    # we shall be using backtracking for the solution of the sudoku puzzle
    # our puzzle is a list of lists where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if the solution exist)

    # step 1:choose somewhere in the puzzle to make a guess

    row,col = find_next_empty(puzzle)

    # step 1.1: If no space left then we shall run some validation checks to check whether our inputs are valid or not

    if row is None:
        return True  # this means we have already solved our puzzle
    
    # step 2: In case there is space or an empty block to insert a number, then we shall make a guess between 1 and 9 
    for guess in range(1, 10): # range (1,10)  is 1,2,3...9
        #step 3: check if our guess is valid or not
        if is_valid(puzzle,guess,row,col):
            # step 3.1: if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True
        
        # step 5: if not valid OR
        # if our guess does not solve the puzzle, then we need to backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess

    # step 6: if we have tried every possible guess and none of them works then we conclude the puzzle as UNSOLVABLE!
    return False

if __name__ == '__main__': # you can modify the sudoku puzzle below
    example_sudoku_board = [
        [7, -1, -1,   4, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   6, -1, 9,   -1, -1, 7],
        [9, 3, 2,   -1, -1, 7,   -1, -1, -1],

        [-1, 2, -1,   7, 6, -1,   8, -1, 5],
        [4, -1, -1,   5, -1, -1,   -1, 2, 3],
        [-1, 8, -1,   -1, 1, -1,   -1, 7, 9],

        [1, -1, -1,   -1, 2, 5,   7, 6, -1],
        [-1, -1, -1,  3, -1, -1,   -1, -1, 2],
        [-1, 4, -1,   9, -1, -1,   -1, -1, 8]
    ]
    print(solve_sudoku(example_sudoku_board))
    pprint(example_sudoku_board)

