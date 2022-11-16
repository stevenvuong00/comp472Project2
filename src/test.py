import numpy as np 
from board import Board
from vehicle import Vehicle
from ucs import UCS

input1 = 'BBIJ....IJCC..AALMGDDKLMGH.KL.GHFFL.' # modified to test
input2 = '..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J..'
input3 = 'C.B...C.BHHHAADD........EEGGGF.....F'
input4= '....F...B.F.AABCF....C.....C....EE..'
board1 = Board(input1)
board2 = Board(input2)
board3 = Board(input3)
board4 = Board(input4)
print("Og board")
board1.printBoard()

# PROBABLY NEED TO REFACTOR THIS INTO A METHOD IN BOARD
# Problem: circular import for board and vehicle 
def createVehicles(board):
    for i in range(6):
        for j in range(6):
            # check if there's a vehicle with that letter already or empty
            if board.grid[i][j] == "." or board.grid[i][j] in board.vehicles:
                continue
            else:
                board.vehicles[board.grid[i][j]] = Vehicle(board.grid[i][j], board)
    # return board

createVehicles(board1)
# board1.getChildren()
# print("generated children")
# children = board1.children
# # print(children)
# for child in children:
#     print("child board")
#     child.printBoard()
#     print(child.cost)

# UCS(createVehicles(board1)).search()

# board = createVehicles(board3)
# board.vehicles['D'].right()
# board.printBoard()
# board.vehicles['D'].right()
# board.printBoard()
# board.vehicles['D'].leaveParking()
# board.printBoard()
# print(board1.equals(board2))
# print(board1.equals(board3))

# print("h1(n): {}".format(board1.h1()))
# print("h2(n): {}".format(board1.h2()))
# print("h3(n): {}".format(board1.h3(3)))
print("h4(n): {}".format(board1.h4()))
