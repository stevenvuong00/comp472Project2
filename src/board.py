import numpy as np 
import copy

class Board:
    def __init__(self, input = None):
        # TODO process car fuel
        # self.board = np.array(list(input[0])).reshape((6,6)) for testing rn
        # will change back when the input is the line we read from the input file
        self.grid = np.array(list(input)).reshape((6,6))
        self.vehicles = {} # dict so we can get value O(1)
        self.children = []
        self.parent = None
        self.cost = 0

    def updateGrid(self, car):
        positions = car.position

        for pos in positions:
            self.grid[pos[0], pos[1]] = car.name

    # method to print grid
    def printBoard(self):
        print(self.grid)
    
    # need to pass car A
    def goal(self):
        # check if car at exit is A and if the orientation is correct
        if self.grid[2][5] == 'A' and self.vehicles['A'].orientation == 'X':
            print("goal state reached!")

    # go through every car, generate all possible moves and boards --> new different state for every move
    def getChildren(self):
        for key in self.vehicles.keys():
            if self.vehicles[key].orientation == 'X':
                if self.vehicles[key].canMoveRight():
                    copy = self.copy() # used to get next board
                    while copy.vehicles[key].canMoveRight():
                        copy.vehicles[key].right() # movement in copy board
                        copy.updateGrid(copy.vehicles[key])
                        child = copy.copy() # create copy of parent board
                        self.children.append(child) # add child board to parent board

                if self.vehicles[key].canMoveLeft():
                    copy = self.copy() # used to get next board
                    while copy.vehicles[key].canMoveLeft():
                        copy.vehicles[key].left() # movement in copy board
                        copy.updateGrid(copy.vehicles[key])
                        child = copy.copy()
                        self.children.append(child)

            if self.vehicles[key].orientation == 'Y':
                if self.vehicles[key].canMoveDown():
                    copy = self.copy() # used to get next board
                    while copy.vehicles[key].canMoveDown():
                        copy.vehicles[key].down() # movement in copy board
                        copy.updateGrid(copy.vehicles[key])
                        child = copy.copy()
                        self.children.append(child)                    

                if self.vehicles[key].canMoveUp():
                    copy = self.copy() # used to get next board
                    while copy.vehicles[key].canMoveUp():
                        copy.vehicles[key].up() # movement in child board
                        copy.updateGrid(copy.vehicles[key])
                        child = copy.copy()
                        self.children.append(child) 

    # copy the board
    def copy(self):
        return copy.deepcopy(self)
