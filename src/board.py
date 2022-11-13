import numpy as np 
import copy

class Board:
    def __init__(self, input = None):
        # self.board = np.array(list(input[0])).reshape((6,6)) for testing rn
        # will change back when the input is the line we read from the input file
        self.grid = np.array(list(input)).reshape((6,6))
        self.vehicles = {} # dict so we can get value O(1)
        self.children = []
        self.parent = None

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

    # go through every car, generate all possible moves --> new different state for every move
    def generateSuccessors(self):
        # try to move all cars, if can move, create new board, then move the car there
        # make deep copy of both the board and the vehicles
        # for new boards, set currentboard as the parent board
        for key in self.vehicles.keys():
            if self.vehicles[key].orientation == 'X':
                # move until cant anymore --> how to implement this IMPORTANT
                self.vehicles[key].printVehicle()

                if self.vehicles[key].canMoveRight():
                    child = self.copy() # create copy of parent board
                    child.vehicles[key].right() # movement
                    child.updateGrid(child.vehicles[key]) # reprint the board
                    self.children.append(child) # add child board to parent board

                if self.vehicles[key].canMoveLeft():
                    child = self.copy()
                    child.vehicles[key].left() # movement
                    child.updateGrid(child.vehicles[key])
                    self.children.append(child)

            elif self.vehicles[key].orientation == 'Y':
                # move until cant anymore --> how to implement this
                self.vehicles[key].printVehicle()

                if self.vehicles[key].canMoveDown():
                    child = self.copy()
                    child.vehicles[key].down() # movement
                    child.updateGrid(child.vehicles[key])
                    self.children.append(child)                    

                if self.vehicles[key].canMoveUp():
                    child = self.copy()
                    
                    child.vehicles[key].up() # movement
                    child.updateGrid(child.vehicles[key])
                    self.children.append(child)  

    # copy the board
    def copy(self):
        return copy.deepcopy(self)
