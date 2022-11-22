import numpy as np
from board import Board
import time
from collections import deque


class UCS:
    def __init__(self, board, puzzle_count):
        self.board = board
        self.open = deque()
        self.closed = []
        self.visited_boards = set()
        self.lowest_cost = 0
        self.solution_path = []
        self.solution_cost = 0
        self.output_search_file = "../output_files/ucs-search-" + str(puzzle_count) + ".txt"
        # self.output_search_file = "output_files/ucs-search-" + str(puzzle_count) + ".txt"
        self.summary_data = [str(puzzle_count), "UCS", "N/A"]  # See below
        # ['#', Algorithm', 'Heuristic', 'Length of the Solution','Length of the Search Path', 'Execution Time']

    def search(self):
        start = time.time()

        # root node: (current node, parent, f(n), g(n), h(n), movement, fuel)
        self.open.append((self.board.grid, None, 0, 0, 0, "", self.board.current_fuel))
        x = 0  # keep for search path length?
        goal = None

        f_search = open(self.output_search_file, "w")

        while len(self.open) > 0:
            x += 1
            # self.open = sorted(self.open, key=lambda k: k[2])
            # Remove first element from open
            current_node = self.open.popleft()
            current_board = Board(current_node[0], current_node[6], current_node[1])

            current_board.get_children()
            children = current_board.children
            # Visited nodes: Moving the current node to CLOSED
            self.closed.append(current_node)
            self.visited_boards.add(self.array_to_string(current_board.grid))
            f_search.write("{} {} {}\t{} {}".format(current_node[2], current_node[3], current_node[4],
                                             self.array_to_string(current_node[0]),
                                             self.process_fuel(current_node[6])))
            f_search.write("\n")
            if Board(self.closed[-1][0]).goal():
                goal = self.closed[-1]
                self.get_solution_path()
                break

            for child in children:
                # check if the generated child is in closed list 
                if not self.array_to_string(child[0]) in self.visited_boards:
                    in_open = None
                    # check if the generated child is in open list
                    for index, node in enumerate(self.open):
                        if np.array_equal(child[0], node[0]):
                            in_open = [node, index]

                    if not in_open:
                        self.open.append(
                            (child[0], current_board, current_node[3] + 1, current_node[3] + 1, 0, child[1], child[2]))
                        # current_board.applied_moves = None
                    else:
                        if in_open[0][2] > current_node[3] + 1:
                            self.open.pop(in_open[1])
                            self.open.append((child[0], current_board, current_node[3] + 1, current_node[3] + 1, 0,
                                              child[1], child[2]))
                            # current_board.applied_moves = None

        end = time.time()
        runtime = str(end - start)

        if goal is not None:
            print()
            print('Runtime: ' + runtime)
            print('Search path length: {}'.format(x))
            print("[total cost: {}]".format(goal[2]))
            print()
            goal[1].print_board()
            f_search.close()

        else:
            print("No solution")
            self.summary_data.append("No solution")
        print("-------------------------------------------------------")
        self.summary_data.append(str(x))
        self.summary_data.append(runtime)
        return self.summary_data

    def get_solution_path(self):
        # Start with the solution and backtrack to the start state
        goal = self.closed[-1]
        self.solution_path.append((goal[0], goal[5], goal[6]))
        parent = goal[1]

        while parent is not None:
            for node in self.closed:
                if parent.equals(node[0]):
                    self.solution_path.append((node[0], node[5], node[6]))
                    parent = node[1]
                    break

        self.solution_path.reverse()
        self.solution_path.pop(0)
        summary = []
        solution = []
        for node in self.solution_path:
            summary.append(node[1])
            solution.append("{}\t{} {}".format(node[1], self.array_to_string(node[0]), self.process_fuel(node[2])))

        print("\nSolution path length: ", len(self.solution_path), " moves")
        self.summary_data.append(str(len(self.solution_path)))
        print("Solution path: " + str(summary) + "\n")
        list(map(print, solution))

    def array_to_string(self, array):
        grid = ""
        for list in array:
            grid += "".join(list)
        return grid

    def process_fuel(self, fuel):
        fuel_str = ""
        for key in fuel.keys():
            if fuel[key] != 100:
                fuel_str = fuel_str + key + str(fuel[key]) + " "
        return fuel_str
