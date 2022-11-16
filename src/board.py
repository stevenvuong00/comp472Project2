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

    # update self.grid with NEW car pos
    def updateGrid(self, car):
        positions = car.position

        for pos in positions:
            self.grid[pos[0], pos[1]] = car.name

    # method to print grid
    def printBoard(self):
        print(self.grid)
    
    # check if the board is at a goal state
    def goal(self):
        # check if car at exit is A and if the orientation is correct
        return self.vehicles['A'].orientation == 'X' and self.grid[2][5] == 'A' 
             
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
                        child.cost += 1
                        child.leaveParking()
                        self.children.append(child) # add child board to parent board

                if self.vehicles[key].canMoveLeft():
                    copy = self.copy() # used to get next board
                    while copy.vehicles[key].canMoveLeft():
                        copy.vehicles[key].left() # movement in copy board
                        copy.updateGrid(copy.vehicles[key])
                        child = copy.copy()
                        child.cost += 1
                        self.children.append(child)

            if self.vehicles[key].orientation == 'Y':
                if self.vehicles[key].canMoveDown():
                    copy = self.copy() # used to get next board
                    while copy.vehicles[key].canMoveDown():
                        copy.vehicles[key].down() # movement in copy board
                        copy.updateGrid(copy.vehicles[key])
                        child = copy.copy()
                        child.cost += 1
                        self.children.append(child)                    

                if self.vehicles[key].canMoveUp():
                    copy = self.copy() # used to get next board
                    while copy.vehicles[key].canMoveUp():
                        copy.vehicles[key].up() # movement in child board
                        copy.updateGrid(copy.vehicles[key])
                        child = copy.copy()
                        child.cost += 1
                        self.children.append(child) 

    # check if 2 boards: self and another board are equal
    def equals(self, board):
        return np.array_equal(self.grid, board.grid)

    # copy the board
    def copy(self):
        return copy.deepcopy(self)

    # method to remove car other than A if it is at position [2][5] and it is horizontal
    def leaveParking(self):
        if(self.grid[2][5] == 'A'):
            return
        if(self.grid[2][5] != '.' and self.vehicles[self.grid[2][5]].orientation == 'X'):
            vehicle_name = self.grid[2][5]
            for pos in self.vehicles[self.grid[2][5]].position:
                self.grid[pos[0]][pos[1]] = '.'
            self.vehicles.pop(vehicle_name)
    
    # Heuristic 1: number of blocked vehicles
    def h1(self):
        list = []
        posA = self.vehicles['A'].position
        # check on the right of A
        for i in range(6):
            if i > posA[1][1] and self.grid[2][i] != '.': # posa[1][1] is the rightmost column of car A
                list.append(self.grid[2][i])
        # convert list to set
        list = set(list)
        return len(list) 

    # Heuristic 2: number of blocked positions
    def h2(self):
        list = []
        posA = self.vehicles['A'].position
        # check on the right of A
        for i in range(6):
            if i > posA[1][1] and self.grid[2][i] != '.': # posa[1][1] is the rightmost column of car A
                list.append(self.grid[2][i])
        return len(list)      

    # Heuristic 3: same as h1 but with a multiplying constant
    def h3(self, constant):
        list = []
        posA = self.vehicles['A'].position
        # check on the right of A
        for i in range(6):
            if i > posA[1][1] and self.grid[2][i] != '.': # posa[1][1] is the rightmost column of car A
                list.append(self.grid[2][i])
        # convert list to set
        list = set(list)
        return constant * len(list) 
    
    # Heuristic 4: Check for blocked vehicles, importance to them
    # vertical free --> 1
    # vertical blocked --> 2
    # horizontal free --> 1
    # horizontal blocked --> 2
    def h4(self):
        total = 0
        list = []
        posA = self.vehicles['A'].position
        # check on the right of A
        for i in range(6):
            if i > posA[1][1] and self.grid[2][i] != '.': # posa[1][1] is the rightmost column of car A
                list.append(self.grid[2][i])
        # convert list to set
        list = set(list)
        print(list)
        for letter in list: # letter = vehicle name
            if self.vehicles[letter].orientation == 'Y':
                # free car
                if self.vehicles[letter].canMoveUp() and self.vehicles[letter].canMoveDown():
                    print("car has 2 free move")
                    total += 1
                if (self.vehicles[letter].canMoveUp() and not self.vehicles[letter].canMoveDown()):
                    print("car has 1 free move")
                    total += 2
                if not self.vehicles[letter].canMoveUp() and self.vehicles[letter].canMoveDown():
                    print("car has 1 free move")
                    total += 2
                if not self.vehicles[letter].canMoveUp() and not self.vehicles[letter].canMoveDown():
                    print("car has no free move")
                    total += 2
            else:
                if self.vehicles[letter].canMoveRight() or self.grid[2][5] == letter:
                    print("car can move right")
                    total += 1
                elif not self.vehicles[letter].canMoveRight():
                    print("car cant move right")
                    total += 2
        return total