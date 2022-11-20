import numpy as np


class Vehicle:
    def __init__(self, name, board, fuel=100):
        self.name = name
        self.position = self.get_pos(board)
        self.orientation = self.get_orientation()
        self.fuel = fuel

    def get_pos(self, board):
        position = []
        for i in range(6):
            for j in range(6):
                if board.grid[i][j] == self.name:
                    position.append([i, j])
        return position

    def get_orientation(self):
        # check same row
        if self.position[0][0] == self.position[1][0]:
            return 'X'
        else:
            return 'Y'

    # need to check head from top of the car, leftmost element of the pos list
    # check fuel, orientation, if going out of board, and if next pos is free
    # remove 1 from each ROW
    def can_move_up(self, current_board):
        return self.fuel > 0 \
               and self.orientation == 'Y' \
               and self.position[0][0] - 1 >= 0 \
               and current_board.grid[self.position[0][0] - 1][self.position[0][1]] == '.'

    # check the last element of the pos list
    def can_move_down(self, current_board):
        return self.fuel > 0 \
               and self.orientation == 'Y' \
               and self.position[-1][0] + 1 < 6 \
               and current_board.grid[self.position[-1][0] + 1][self.position[0][1]] == '.'

    # check first element of the pos list (left most pos of the car)
    def can_move_left(self, current_board):
        return self.fuel > 0 \
               and self.orientation == 'X' \
               and self.position[0][1] - 1 >= 0 \
               and current_board.grid[self.position[0][0]][self.position[0][1] - 1] == '.'

    # check LAST element of the pos list (right most pos of the car)
    def can_move_right(self, current_board):
        # need check col of last pos if its less than 6
        return self.fuel > 0 \
               and self.orientation == 'X' \
               and self.position[-1][1] + 1 < 6 \
               and current_board.grid[self.position[0][0]][self.position[-1][1] + 1] == '.'

    def move(self, current_board, direction):
        # remove from grid
        for pos in self.position:
            current_board.grid[pos[0]][pos[1]] = '.'

        # new position
        if direction == 'right':
            for pos in self.position:
                pos[1] = pos[1] + 1
        elif direction == 'left':
            for pos in self.position:
                pos[1] = pos[1] - 1
        elif direction == 'up':
            for pos in self.position:
                pos[0] = pos[0] - 1
        elif direction == 'down':
            for pos in self.position:
                pos[0] = pos[0] + 1
        # fuel and grid update
        self.fuel -= 1
        current_board.change_fuel()

    # change state of CURRENT board
    def up(self, current_board):
        # need to check head from top
        if self.can_move_up(current_board):
            # remove from grid
            for pos in self.position:
                current_board.grid[pos[0]][pos[1]] = '.'

            # change to new pos
            for pos in self.position:
                pos[0] = pos[0] - 1
            self.fuel -= 1
            current_board.update_grid(self)
        else:
            print("cant move this car up")

    def down(self, current_board):
        # check the bottom of the car 
        if self.can_move_down(current_board):
            # remove from grid
            for pos in self.position:
                current_board.grid[pos[0]][pos[1]] = '.'

            for pos in self.position:
                pos[0] = pos[0] + 1
            self.fuel -= 1
            current_board.update_grid(self)
        else:
            print("cant move this car down")

    def left(self, current_board):
        # check the left of the car (left most index)
        if self.can_move_left(current_board):
            # remove from grid
            for pos in self.position:
                current_board.grid[pos[0]][pos[1]] = '.'

            for pos in self.position:
                pos[1] = pos[1] - 1
            self.fuel -= 1
            current_board.update_grid(self)
        else:
            print("cant move this car left")

    def right(self, current_board):
        # check the right of the car (left most index)
        if self.can_move_right(current_board):
            # remove from grid
            for pos in self.position:
                current_board.grid[pos[0]][pos[1]] = '.'

            for pos in self.position:
                pos[1] = pos[1] + 1
            self.fuel -= 1
            current_board.update_grid(self)
        else:
            print("cant move this car right")

    def print_vehicle(self):
        print(self.name, end=' ')
        print(self.position, end=' ')
        print(self.fuel)
