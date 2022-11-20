import numpy as np
from board import Board
from ucs import UCS
from vehicle import Vehicle

# input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.' # modified to test
# input1 = 'BB.G.H...G.HAAMMKK..FCCIDDF..I..F...'
input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
input2 = '..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J..'
# input2 = 'BB.G.HE..G.HEAAG.I..FCCIDDF..I..F...'

input3 = 'C.B...C.BHHHAADD........EEGGGF.....F'
input4 = '....F...B.F.AABCF....C.....C....EE..'

input5 = 'BBBBBBKKKKKKAAECZD..ECZD......FFFFFF'
input6 = 'BBBBBBKKKKKK.AA.....ECZD..ECZDFFFFFF'
input7 = '.............AA.....................'

fuel = {'A': 99, 'M': 99}
# board1 = Board(input1, fuel)
# print(board1.current_fuel)
# board1.print_board()
# move one car down
# board1.check_moves('M')
# print(board1.current_fuel)
# board1.print_board()
# board2_test = Board(input1, board1.current_fuel)
# print(board1.current_fuel)
board1 = Board(input1)
board2 = Board(input2)
board3 = Board(input3)
board4 = Board(input4)
board5 = Board(input5)
board6 = Board(input6)
board7 = Board(input7)

# UCS(board1).search()
# UCS(board3).search()
print(UCS(board5).search())
# UCS(board2).search()
# UCS(board6).search()
# UCS(board7).search()
# UCS(board4).search()
# print(UCS(board2).search())

# car1 = Vehicle('A', board1, 99)
# car1.print_vehicle()




