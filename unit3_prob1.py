# SPECIFICATION:
#
# check_sudoku() determines whether its argument is a valid Sudoku
# grid. It can handle grids that are completely filled in, and also
# grids that hold some empty cells where the player has not yet
# written numbers.
#
# First, your code must do some sanity checking to make sure that its
# argument:
#
# - is a 9x9 list of lists
#
# - contains, in each of its 81 elements, an integer in the range 0..9
#
# If either of these properties does not hold, check_sudoku must
# return None.
#
# If the sanity checks pass, your code should return True if all of
# the following hold, and False otherwise:
#
# - each number in the range 1..9 occurs only once in each row 
#
# - each number in the range 1..9 occurs only once in each column
#
# - each number the range 1..9 occurs only once in each of the nine
#   3x3 sub-grids, or "boxes", that make up the board
#
# This diagram (which depicts a valid Sudoku grid) illustrates how the
# grid is divided into sub-grids:
#
# 5 3 4 | 6 7 8 | 9 1 2
# 6 7 2 | 1 9 5 | 3 4 8
# 1 9 8 | 3 4 2 | 5 6 7 
# ---------------------
# 8 5 9 | 7 6 1 | 4 2 3
# 4 2 6 | 8 5 3 | 7 9 1
# 7 1 3 | 9 2 4 | 8 5 6
# ---------------------
# 9 6 1 | 5 3 7 | 0 0 0
# 2 8 7 | 4 1 9 | 0 0 0
# 3 4 5 | 2 8 6 | 0 0 0
# 
# Please keep in mind that a valid grid (i.e., one for which your
# function returns True) may contain 0 multiple times in a row,
# column, or sub-grid. Here we are using 0 to represent an element of
# the Sudoku grid that the player has not yet filled in.

# check_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# check_sudoku should return True
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# check_sudoku should return True
hard = [[1,0,0,0,0,7,0,9,0],
        [0,3,0,0,2,0,0,0,8],
        [0,0,9,6,0,0,5,0,0],
        [0,0,5,3,0,0,9,0,0],
        [0,1,0,0,8,0,0,0,2],
        [6,0,0,0,0,4,0,0,0],
        [3,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,7],
        [0,0,7,0,0,0,3,0,0]]

def check_sudoku(grid):
    pass_test = False
    if (rows_columns(grid) and check_value(grid)):
        pass_test = True
    else:
        return None
    if (check_rep_row(grid) and check_rep_col(grid) and check_rep_subgrid(grid)):
        pass_test = True
        return pass_test
    else:
        return False
    
def rows_columns(grid):
    if len(grid) != 9:
        return None
    for item in grid:
        if len(item) != 9:
            return None
    return True  

def check_value(grid):
    count_pass = True
    for item in grid:
#        print(item)
        for num in item:
#            print(num)
            if (num < 0 or num > 9):
                count_pass = None
    return count_pass

def check_rep_row(grid):
    no_rep = True
    for item in grid:
        for i in range(len(item)):
            for j in range((i+1), len(item)):
                if item[i] != 0 and item[i] == item[j]:
                    no_rep = False    
    return no_rep

def check_rep_col(grid):
    no_rep = True
    list_col = []
    for i in range(len(grid)):
        for item in grid:
            list_col.append(item[i])
        print(list_col)
        for i in range(len(list_col)): #not good b/c repetitive - check_rep_row(grid)
            for j in range((i+1), len(list_col)):
                if list_col[i] != 0 and list_col[i] == list_col[j]:
                    no_rep = False
        list_col = []
    return no_rep
        
def check_rep_subgrid(grid):
    no_rep = True
    list_subgrid = []
    grid_subgrid = []
    #kind of combo of both rep_row and rep_col but only partial in any given direction
    for a in range(int(math.sqrt(len(grid)))):
        b = a + 1
        for c in range(int(math.sqrt(len(grid)))):
            d = c + 1
            for i in range(a*(int(math.sqrt(len(grid)))), b*(int(math.sqrt(len(grid))))):
                for j in range(c*(int(math.sqrt(len(grid)))), d*(int(math.sqrt(len(grid))))):
                    list_subgrid.append(grid[i][j])
            #print(list_subgrid)
            grid_subgrid.append(list_subgrid)
            list_subgrid = []
    #print(grid_subgrid)    
    return check_rep_row(grid_subgrid)

print check_sudoku(ill_formed) # --> None
print check_sudoku(valid)      # --> True
print check_sudoku(invalid)    # --> False
print check_sudoku(easy)       # --> True
print check_sudoku(hard)       # --> True

