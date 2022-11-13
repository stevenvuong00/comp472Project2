import numpy as np 
from board import Board
from vehicle import Vehicle

input1 = 'BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL.'
board1 = Board(input1)
# board1.printBoard()

# car1 = Vehicle('A', board1)
# car1.printVehicle()

# print(" ")

# car2 = Vehicle('I', board1)
# car2.printVehicle()

for i in range(6):
    for j in range(6):
        # check if there's a vehicle with that letter already or empty
        # if board1.grid[i][j] == "." or board1.grid[i][j] in board1.vehicleNames:
        if board1.grid[i][j] == "." or board1.grid[i][j] in board1.vehicles:
            continue
        else:
            # board1.vehicles.append(Vehicle(board1.grid[i][j], board1))
            # board1.vehicleNames.append(board1.grid[i][j])
            board1.vehicles[board1.grid[i][j]] = Vehicle(board1.grid[i][j], board1)
            
# car keys
print(board1.vehicles.keys())

# getting all the vehicles in a board
for key in board1.vehicles.keys():
    board1.vehicles[key].printVehicle()


# print(" ")
# car1 = board1.vehicles['G']

# car1.printVehicle()
# car1.up()

# print(" ")
# car1.printVehicle()
# board1.regenerateGrid(car1)
# board1.printBoard()

# cari = board1.vehicles['I']
# cari.down()

# board1.regenerateGrid(cari)
# board1.printBoard()


# #RIGHT LEFT TESTING
# print(" ")
# cara = board1.vehicles['A']
# # cara.printVehicle()

# cara.left()
# board1.regenerateGrid(cara)
# board1.printBoard()

# carm = board1.vehicles['M']
# carm.down()
# # carm.printVehicle()

# board1.regenerateGrid(carm)
# board1.printBoard()

# cara = board1.vehicles['A']
# cara.printVehicle()
# cara.right()
# cara.right()
# cara.right()
# # cara.right()
# # cara.left()
# # cara.left()

# board1.regenerateGrid(cara)
# board1.printBoard()
# board1.goal()