from re import I
from board import Board
import time
from queue import PriorityQueue
import numpy as np


class GBFS:
    def __init__(self, board, puzzle_count, heuristic):
        self.board = board
        self.open = PriorityQueue()
        self.closed = []
        self.visited_boards = set()
        self.lowest_cost = 0
        self.solution_path = []
        self.solution_cost = 0
        self.heuristic = heuristic
        # self.output_search_file = "../output_files/gbfs-" + self.heuristic + "-search-" + str(puzzle_count) + ".txt"
        self.output_search_file = "output_files/gbfs-" + self.heuristic + "-search-" + str(puzzle_count) + ".txt"
        self.summary_data = [str(puzzle_count), "GBFS", self.heuristic]  # See below
        # ['#', Algorithm', 'Heuristic', 'Length of the Solution','Length of the Search Path', 'Execution Time']

    def search(self):
        heuristic = self.heuristic
        start = time.time()

        # root node: (h(n), current node, parent, f(n), g(n), movement, fuel)
        hn = self.board.apply_heuristic(heuristic)
        gn = 0
        fn = hn + gn
        self.open.put((fn, self.board, None, gn, hn, "", self.board.current_fuel))

        search_path_length = 0  # search path length
        goal = None

        f_search = open(self.output_search_file, "w")

        while not self.open.empty():
            search_path_length += 1
            # Remove first element from open
            fn, current_board, parent_board, gn, hn, move, current_fuel = self.open.get()
            current_node = (fn, current_board, parent_board, gn, hn, move, current_fuel)

            current_board.get_children()
            children = current_board.children
            parent_gn = gn
            # Visited nodes: Moving the current node to CLOSED
            self.closed.append(current_node)
            self.visited_boards.add(self.array_to_string(current_board.grid))

            f_search.write("{} {} {}\t{} {}".format(fn, gn, hn,
                                                    self.array_to_string(current_board.grid),
                                                    self.process_fuel(current_fuel)))
            f_search.write("\n")

            if self.closed[-1][1].goal():
                goal = self.closed[-1]
                self.get_solution_path()
                break

            for child in children:
                # check if the generated child is in closed list 
                if not self.array_to_string(child[0]) in self.visited_boards:
                    in_open = False
                    for open_node in self.open.queue:
                        if np.array_equal(open_node[1].grid, child[0]):
                            in_open = True
                            break
                    if in_open is False:
                        child_board = Board(child[0], child[2], child[0])
                        hn = child_board.apply_heuristic(heuristic)
                        gn = 0
                        fn = hn + gn
                        child_hn = child_board.apply_heuristic(heuristic)
                        child_gn = parent_gn + 1
                        child_fn = child_hn + child_gn
                        child_board.fn = child_fn
                        child_board.gn = child_gn
                        self.open.put((child_fn, child_board, current_node[1], child_gn, child_hn, child[1], child[2]))

        end = time.time()
        runtime = str(end - start)

        if goal is not None:
            print()
            print('Runtime: ' + runtime)
            print('Search path length: {}'.format(search_path_length))
            print()
            goal[1].print_board()
            f_search.close()
        else:
            print("No solution")
            self.summary_data.append("No solution")
        print("-------------------------------------------------------")
        self.summary_data.append(str(search_path_length))
        self.summary_data.append(runtime)
        return self.summary_data

    def get_solution_path(self):
        # Start with the solution and backtrack to the start state
        goal = self.closed[-1]
        goal_board = goal[1]
        goal_movement = goal[5]
        goal_fuel = goal[6]
        # goal (fn, board, parent board, gn, hn, movement, fuel)
        self.solution_path.append((goal_board, goal_movement, goal_fuel))
        parent = goal[2]

        while parent is not None:
            for node in self.closed:
                if parent.equals(node[1].grid):
                    self.solution_path.append((node[1], node[5], node[6]))
                    parent = node[2]
                    break

        self.solution_path.reverse()
        self.solution_path.pop(0)
        summary = []
        solution = []
        for node in self.solution_path:
            summary.append(node[1])
            solution.append("{}\t{} {}".format(node[1], self.array_to_string(node[0].grid), self.process_fuel(node[2])))

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
