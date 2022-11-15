import numpy as np 
from board import Board
from vehicle import Vehicle

input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
input2 = '..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J..'
# input1 = '..I..LBBI.KLGHAAK.GHDDK.G..JEEFF.J..'
board1 = Board(input1)
board2 = Board(input2)


# print("Og board")
# board1.printBoard()

# PROBABLY NEED TO REFACTOR THIS INTO A METHOD IN BOARD
# Problem: circular import for board and vehicle 
for i in range(6):
    for j in range(6):
        # check if there's a vehicle with that letter already or empty
        if board1.grid[i][j] == "." or board1.grid[i][j] in board1.vehicles:
            continue
        else:
            board1.vehicles[board1.grid[i][j]] = Vehicle(board1.grid[i][j], board1)
 
closed = [board1.grid] # list of closed grids
closed.append(board2.grid)

board2 = Board(input1) # new child


for grid in closed:
    if np.array_equal(grid, board2.grid):
        print("hello")