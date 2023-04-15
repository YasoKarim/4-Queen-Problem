board = [[0] * 4 for i in range(4)]

N = len(board)

# Test if safe to place queen here or not

def safe(board, row , col):

    # Check if exist in row    
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check previous main Diagonal 
    for i , j in zip(range(row, -1, -1), range(col, -1 ,-1)):
        if board[i][j] == 1:
            return False
    
    # Check previous counter Diagonal
    for i , j in zip(range(row, N, -1), range(col, -1 ,-1)):
        if board[i][j] == 1:
            return False
    
    return True        

def SolveFourQueen(board, col):
    
    # base Case
    # We reached our goal 
    if col >= N:
        return True 

    # we test each row then test if we can put on the second column if not then backtrack
    for i in range(N):
        if safe(board, i, col):
            board[i][col] = 1
            
            # check if we can insert another queen on second column
            if SolveFourQueen(board, col + 1):
                return True
            
            board[i][col] = 0
    return False
    
# Function to print the board
def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print("\n")        

print("\nIntial Goal\n")
print_board(board)

# Function to detect if it can be solved or not
def solve():
    if not SolveFourQueen(board,0):
        print("Solution not found")
    print("\nGoal Board: \n")
    print_board(board)    

solve()

input('Press ENTER to exit')
