import numpy as np 

class Board:
    def __init__(self, input):
        # self.board = np.array(list(input[0])).reshape((6,6)) for testing rn
        # will change back when the input is the line we read from the input file
        self.grid = np.array(list(input)).reshape((6,6))
        self.vehicles = []
        self.vehicleNames = []
        self.children = []

    def regenerateGrid(self, car):
        positions = car.position

        for pos in positions:
            self.grid[pos[0], pos[1]] = car.name

    # method to read an input into a 6x6 board
    def printBoard(self):
        print(self.grid)
    
    def vehicles():
        print("list of remaining vehicles")
