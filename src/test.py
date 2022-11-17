import numpy as np 
from board import Board
from vehicle import Vehicle
from ucs import UCS
from gbfs import GBFS

input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.' 
# input1 = 'BB.G.H...G.HAAMMKK..FCCIDDF..I..F...'
input2 = '..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J..'
input3 = 'C.B...C.BHHHAADD........EEGGGF.....F'
input4= '....F...B.F.AABCF....C.....C....EE..'
board1 = Board(input1)
board2 = Board(input2)
# board3 = Board(input3)
# board4 = Board(input4)
# print("Og board")
# board1.printBoard()

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
    return board

createVehicles(board1)
# createVehicles(board2)

UCS(board1).search()

# print("h1(n): {}".format(board1.h1()))
# print("h2(n): {}".format(board1.h2()))
# print("h3(n): {}".format(board1.h3(3)))
# print("h4(n): {}".format(board1.h4()))

# GBFS(board1).search()
# GBFS(board2).search()
