import numpy as np 
from board import Board

board = np.array(range(0, 36)).reshape((6,6))
f = open('Sample/sample-input.txt')
for line in f:
    if line[0] == '#' or line[0] == "\n":
        continue
    input = line.strip().split(" ")
    # board = np.array(list(input[0])).reshape((6,6))
    board = Board(input[0])
    board.printBoard()

    # create vehicles of the board

    # will be part of vehicle class
    fuel = input[1:]
    print(fuel)








