import numpy as np 
from board import Board
from vehicle import Vehicle
import copy

input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
board1 = Board(input1)
print("Og board")
board1.printBoard()

# PROBABLY NEED TO REFACTOR THIS INTO A METHOD IN BOARD
# Problem: circular import for board and vehicle 
for i in range(6):
    for j in range(6):
        # check if there's a vehicle with that letter already or empty
        if board1.grid[i][j] == "." or board1.grid[i][j] in board1.vehicles:
            continue
        else:
            board1.vehicles[board1.grid[i][j]] = Vehicle(board1.grid[i][j], board1)
            
# car keys
# print(board1.vehicles.keys())

# getting all the vehicles in a board
# for key in board1.vehicles.keys():
#     board1.vehicles[key].printVehicle()

board1.generateSuccessors()
print("generated children")
children = board1.children
# print(children)
for child in children:
    print("child board")
    child.printBoard()

# # Testing moving 2 tiles at once
# board2 = Board(input1)
# # board2.printBoard()
# for i in range(6):
#     for j in range(6):
#         # check if there's a vehicle with that letter already or empty
#         if board2.grid[i][j] == "." or board2.grid[i][j] in board2.vehicles:
#             continue
#         else:
#             board2.vehicles[board2.grid[i][j]] = Vehicle(board2.grid[i][j], board2)
# for key in board2.vehicles.keys():
#     board2.vehicles[key].printVehicle()

# carg = board2.vehicles['G']
# carg.up()
# board2.printBoard()
