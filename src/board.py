import numpy as np
from toolz import dicttoolz
from vehicle import Vehicle


class Board:
    io_is_done_flag = False

    def __init__(self, input=None, fuel={}, parent=None, initial_config=None):
        # TODO Will need a method initially to parse the fuel into a dict
        # self.board = np.array(list(input[0])).reshape((6,6)) for testing rn
        self.grid = np.array(list(input)).reshape((6, 6))
        self.vehicles = {}  # dict so we can get value O(1)
        self.children = []
        self.parent = parent
        self.cost = 0
        self.possible_moves = []
        # self.applied_moves = ""
        self.current_fuel = {}  # keep track of the fuel of THIS board, will be passed down to the next boards
        self.generate_cars(fuel)
        self.change_fuel()
        self.original_input = input
        self.original_fuel = dict(fuel)
        self.initial_config = initial_config

        # IO spaghetti
        if parent is None and Board.io_is_done_flag is False:
            print('Initial board configuration: ' + str(self.initial_config))
            print()
            self.print_board()
            print()
            print("Car fuel available: " + str(dict(self.current_fuel)))
            print()
            Board.io_is_done_flag = True

    # update self.grid with NEW car pos
    def update_grid(self, car):
        positions = car.position
        for pos in self.vehicle_old_pos:
            self.grid[pos[0], pos[1]] = '.'
        for pos in positions:
            self.grid[pos[0], pos[1]] = car.name

    def change_fuel(self):
        for key in self.vehicles.keys():
            self.current_fuel[key] = self.vehicles[key].fuel

    # method to print grid
    def print_board(self):
        print(self.grid)

    def generate_cars(self, fuel=None):
        # fuel --> dict of all car and fuel
        self.vehicles = {}
        for i in range(6):
            for j in range(6):
                # check if there's a vehicle with that letter already or empty
                if self.grid[i][j] == "." or self.grid[i][j] in self.vehicles:
                    continue
                else:
                    # default fuel for that specific car --> check in dict
                    # generating car with fuel not 100
                    keys_of_cars_changed_fuel = fuel.keys()
                    if self.grid[i][j] in keys_of_cars_changed_fuel:
                        self.vehicles[self.grid[i][j]] = Vehicle(self.grid[i][j], self, fuel[self.grid[i][j]])
                    # default fuel for that specific car 
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
            self.changed_fuel = {}
            while self.vehicles[key].can_move_down(self):
                distance += 1
                self.apply_move(key, 'down', distance)
            self.reset()
            distance = 0
            self.changed_fuel = {}
            while self.vehicles[key].can_move_up(self):
                distance += 1
                self.apply_move(key, 'up', distance)
            self.reset()
        elif self.vehicles[key].orientation == 'X':
            distance = 0
            self.changed_fuel = {}
            while self.vehicles[key].can_move_left(self):
                distance += 1
                self.apply_move(key, 'left', distance)
            self.reset()
            distance = 0
            self.changed_fuel = {}
            while self.vehicles[key].can_move_right(self):
                distance += 1
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
        self.children.append((new_grid, movement, dict(self.current_fuel)))
        # return vehicle_key + ' ' + move + ' ' + str(distance)

    def reset(self):
        self.grid = np.array(list(self.original_input)).reshape((6, 6))
        self.current_fuel = dict(self.original_fuel)
        self.generate_cars(self.current_fuel)

    # check if 2 boards: self and another board are equal
    def equals(self, grid):
        return np.array_equal(self.grid, grid)

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
