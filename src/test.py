import numpy as np 
from board import Board
from vehicle import Vehicle
from ucs import UCS

input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
# input1 = '..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J..'
# input1 = '..I..LBBI.KLGHAAK.GHDDK.G..JEEFF.J..'
board1 = Board(input1)
print("Og board")
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
            
# board1.getChildren()
# print("generated children")
# children = board1.children
# # print(children)
# for child in children:
#     print("child board")
#     child.printBoard()

# children[0].getChildren()
# children2 = children[0].children
# for child in children2:
#     print("child board")
#     child.printBoard()

solver1 = UCS(board1)
solver1.search()

