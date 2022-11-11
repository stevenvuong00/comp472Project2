import numpy as np 

board = np.array(range(0, 36)).reshape((6,6))
f = open('sample-input.txt')
for line in f:
    if line[0] == '#' or line[0] == "\n":
        continue
    input = line.strip().split(" ")
    board = np.array(list(input[0])).reshape((6,6))
    print(board)
    fuel = input[1:]
    print(fuel)








