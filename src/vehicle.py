import numpy as np 
from board import Board

class Vehicle:
    # input should be 
    def __init__(self, name, board, fuel = 100):
        self.name = name
        self.board = board
        self.oldposition = []
        self.position = self.getPos(board)
        self.orientation = self.setOrientation()
        self.fuel = fuel
        self.moved = False

    def getPos(self, board):
        position = []
        for i in range(6):
            for j in range(6):
                if board.grid[i][j] == self.name:
                    position.append([i,j])
        return position

    def setOrientation(self):
        # check same row
        if self.position[0][0] == self.position[1][0]:
            return 'X'
        else:
            return 'Y'

    def canMoveUp(self):
        # need to check head from top
        # check fuel, orientation, if going out of board, and if next pos is free
        return self.fuel > 0 and self.orientation == 'Y' and self.position[0][0] - 1 >= 0 and self.board.grid[self.position[0][0] - 1][self.position[0][1]] == '.'

    def canMoveDown(self):
        return self.fuel > 0 and self.orientation == 'Y' and self.position[-1][0] + 1 < 6 and self.board.grid[self.position[-1][0] + 1][self.position[0][1]] == '.'

    def canMoveLeft(self):
        return self.fuel > 0 and self.orientation == 'X'  and self.position[0][1] - 1 >= 0 and self.board.grid[self.position[0][0]][self.position[0][1] - 1] == '.'

    def canMoveRight(self):
        # need check col of last pos if its less than 6
        return self.fuel > 0 and self.orientation == 'X'  and self.position[-1][1] + 1 < 6 and self.board.grid[self.position[0][0]][self.position[-1][1] + 1] == '.'

    # same row diff col
    # [2,3]
    # [2,4]
    # [2,5]

    # only row change, col does not change
    # change state of board
    def up(self):
        # need to check head from top
        if self.canMoveUp():
            # remove from grid
            for pos in self.position:
                self.board.grid[pos[0]][pos[1]] = '.'

            # change to new pos
            for pos in self.position:
                pos[0] = pos[0] - 1  
            print('MOVED')
        else:
            print("cant move this car up")  

    def down(self):
        # check the bottom of the car 
        if self.canMoveDown():
            # remove from grid
            for pos in self.position:
                self.board.grid[pos[0]][pos[1]] = '.'

            self.oldposition = self.position.copy()
            for pos in self.position:
                pos[0] = pos[0] + 1  
        else:
            print("cant move this car down")  

    def left(self):
        # check the left of the car (left most index)
        # print("left")
        # print(self.position[-1][1])
        # print("nextpos")
        # print(self.board.grid[self.position[0][0]][self.position[0][0] - 1])
        # print(self.position[0][0])
        # print(self.position[0][1] - 1)
        if self.canMoveLeft():
            # remove from grid
            for pos in self.position:
                self.board.grid[pos[0]][pos[1]] = '.'

            for pos in self.position:
                pos[1] = pos[1] - 1  
        else:
            print("cant move this car left")  

    def right(self):
        # check the right of the car (left most index)
        # need to check if reached goal
        # print("nextpos")
        # # print(self.board.grid[self.position[0][1]][self.position[-1][1]])
        # print(self.position[0][0]) # row
        # print(self.position[-1][1] + 1) # next col
        for pos in self.position:
            print(pos)
            if pos == [2,5]:
                print("reached goal!")

        if self.canMoveRight():
            # remove from grid
            for pos in self.position:
                self.board.grid[pos[0]][pos[1]] = '.'

            for pos in self.position:
                pos[1] = pos[1] + 1  
        else:
            print("cant move this car right")  
            

    def printVehicle(self):
        print(self.name, end = '')
        print(self.position)
        # print(self.fuel)


