import numpy as np
import copy
from toolz import dicttoolz
from vehicle import Vehicle

class Board:
    def __init__(self, input=None):
        # TODO process car fuel
        # self.board = np.array(list(input[0])).reshape((6,6)) for testing rn
        # will change back when the input is the line we read from the input file
        self.grid = np.array(list(input)).reshape((6, 6))
        self.vehicles = {}  # dict so we can get value O(1)
        self.children = []
        self.parent = None
        self.cost = 0
        self.possible_moves = []
        self.applied_moves = ""
        self.generate_cars()
        self.original_input = input
        self.vehicle_old_pos = []

    # update self.grid with NEW car pos
    def update_grid(self, car):
        positions = car.position
        for pos in self.vehicle_old_pos:
            self.grid[pos[0], pos[1]] = '.'
        for pos in positions:
            self.grid[pos[0], pos[1]] = car.name

    # method to print grid
    def print_board(self):
        print(self.grid)

    def generate_cars(self):
        self.vehicles = {}
        for i in range(6):
            for j in range(6):
                # check if there's a vehicle with that letter already or empty
                if self.grid[i][j] == "." or self.grid[i][j] in self.vehicles:
                    continue
                else:
                    self.vehicles[self.grid[i][j]] = Vehicle(self.grid[i][j], self)

    # check if the board is at a goal state
    def goal(self):
        # check if car at exit is A and if the orientation is correct
        return self.vehicles['A'].orientation == 'X' and self.grid[2][5] == 'A'

    def get_children(self):
        dicttoolz.keymap(self.check_moves, self.vehicles)

    def check_moves(self, key):
        # add while for multi space moves
        if self.vehicles[key].orientation == 'Y':
            distance = 0
            while self.vehicles[key].can_move_down(self):
                distance += 1
                # self.applied_moves = self.apply_move(key, 'D', distance)
                self.apply_move(key, 'down', distance)
            self.reset()
            distance = 0
            while self.vehicles[key].can_move_up(self):
                distance += 1
                # self.applied_moves = self.apply_move(key, 'U', distance)
                self.apply_move(key, 'up', distance)
            self.reset()
        elif self.vehicles[key].orientation == 'X':
            distance = 0
            while self.vehicles[key].can_move_left(self):
                distance += 1
                # self.applied_moves = self.apply_move(key, 'L', distance)
                self.apply_move(key, 'left', distance)
            self.reset()
            distance = 0
            while self.vehicles[key].can_move_right(self):
                distance += 1
                # self.applied_moves = self.apply_move(key, 'R', distance)
                self.apply_move(key, 'right', distance)
            self.reset()

    def apply_move(self, vehicle_key, move, distance):
        self.vehicle_old_pos = self.vehicles.get(vehicle_key).get_pos(self)
        self.vehicles[vehicle_key].move(self, move)
        self.update_grid(self.vehicles[vehicle_key])
        self.leave_parking()

        # print('moved ' + vehicle_key + ' ' + move)
        # self.print_board()

        new_grid = np.copy(self.grid)
        movement = vehicle_key + ' ' + move.rjust(5) + ' ' + str(distance)
        self.children.append((new_grid, movement))
        # return vehicle_key + ' ' + move + ' ' + str(distance)

    def reset(self):
        self.grid = np.array(list(self.original_input)).reshape((6, 6))
        self.generate_cars()
        # self.applied_moves = None


    def get_normal_form(self):
        return self.grid

    # check if 2 boards: self and another board are equal
    def equals(self, grid):
        return np.array_equal(self.grid, grid)

    # copy the board
    def copy(self):
        return copy.deepcopy(self)

    # method to remove car other than A if it is at position [2][5] and it is horizontal
    def leave_parking(self):
        if self.grid[2][5] == 'A':
            return
        if self.grid[2][5] != '.' and self.vehicles[self.grid[2][5]].orientation == 'X':
            for pos in self.vehicles[self.grid[2][5]].position:
                self.grid[pos[0]][pos[1]] = '.'

    def grid_to_string(self):
        grid = ""
        for list in self.grid:
            grid += "".join(list)

        return grid

    def fuel_info(self):
        fuel = ""
        for key in self.vehicles:
            fuel += key + str(self.vehicles[key].fuel) + " "
            fuel += self.vehicles[key].fuel + " "
        
        return fuel

    # Heuristic 1: number of blocked vehicles
    def h1(self):
        list = []
        posA = self.vehicles['A'].position
        # check on the right of A
        for i in range(6):
            if i > posA[1][1] and self.grid[2][i] != '.':  # posa[1][1] is the rightmost column of car A
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
            if i > posA[1][1] and self.grid[2][i] != '.':  # posa[1][1] is the rightmost column of car A
                list.append(self.grid[2][i])
        return len(list)

    # Heuristic 3: same as h1 but with a multiplying constant
    def h3(self, constant):
        list = []
        posA = self.vehicles['A'].position
        # check on the right of A
        for i in range(6):
            if i > posA[1][1] and self.grid[2][i] != '.':  # posa[1][1] is the rightmost column of car A
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
            if i > posA[1][1] and self.grid[2][i] != '.':  # posa[1][1] is the rightmost column of car A
                list.append(self.grid[2][i])
        # convert list to set
        list = set(list)
        print(list)
        for letter in list:  # letter = vehicle name
            if self.vehicles[letter].orientation == 'Y':
                # free car
                if self.vehicles[letter].can_move_up() and self.vehicles[letter].can_move_down():
                    print("car has 2 free move")
                    total += 1
                if (self.vehicles[letter].can_move_up() and not self.vehicles[letter].can_move_down()):
                    print("car has 1 free move")
                    total += 2
                if not self.vehicles[letter].can_move_up() and self.vehicles[letter].can_move_down():
                    print("car has 1 free move")
                    total += 2
                if not self.vehicles[letter].can_move_up() and not self.vehicles[letter].can_move_down():
                    print("car has no free move")
                    total += 2
            else:
                if self.vehicles[letter].can_move_right() or self.grid[2][5] == letter:
                    print("car can move right")
                    total += 1
                elif not self.vehicles[letter].can_move_right():
                    print("car cant move right")
                    total += 2
        return total
