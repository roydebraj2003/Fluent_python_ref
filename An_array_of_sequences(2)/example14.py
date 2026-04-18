#Example 2-14. A list with three lists of length 3 can represent a tic-tac-toe board

board = [['_'] * 3 for i in range(3)]

board[2][1] = 'X'

print(board)

b = [['_'] * 3] * 3 # Each row is referenced again
b[2][1] = 'O' # Every row gets changed
print(b)
