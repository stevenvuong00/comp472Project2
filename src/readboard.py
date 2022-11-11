import numpy as np 

# method to read an input into a 6x6 board
def readBoard(input):
    board = np.array(list(input)).reshape((6,6))
    print(board)

input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
readBoard(input1)