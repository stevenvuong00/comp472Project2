import numpy as np 
from board import Board
from vehicle import Vehicle

board = np.array(range(0, 36)).reshape((6,6))
def createVehicles(board):
    for i in range(6):
        for j in range(6):
            # check if there's a vehicle with that letter already or empty
            if board.grid[i][j] == "." or board.grid[i][j] in board.vehicles:
                continue
            else:
                board.vehicles[board.grid[i][j]] = Vehicle(board.grid[i][j], board)

f = open('Sample/sample-input.txt')
for line in f:
    if line[0] == '#' or line[0] == "\n":
        continue
    input = line.strip().split(" ")
    # board = np.array(list(input[0])).reshape((6,6))
    board = Board(input[0])
    createVehicles(board)
    board.printBoard()
    print("h4(n): {}".format(board.h4()))
    # create vehicles of the board

    # will be part of vehicle class
    fuel = input[1:]
    print(fuel)





