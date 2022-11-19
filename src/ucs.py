import numpy as np

from board import Board

import time
from collections import deque


class UCS:
    def __init__(self, board):
        self.board = board
        self.open = deque()
        self.closed = []
        self.visited_boards = set()
        self.lowest_cost = 0
        self.solution_path = []
        self.solution_cost = 0

    def search(self):
        start = time.time()
        print("Searching...")

        # print("OG board")
        # self.board.print_board()
        # print()

        # node object: (current node, parent, cost [f(n)], total_cost[g(n)])
        self.open.append((self.board.grid, None, 0, 0, 0))
        print(self.open)
        # total_cost = 0
        x = 0
        goal = None

        # while len(self.open) > 0:
        while x <= 9:
            print()
            print("VISITING NEW BOARD ", x)
            x += 1
            # self.open = sorted(self.open, key=lambda k: k[2])
            # Remove first element from open
            current_node = self.open.popleft()
            current_board = Board(current_node[0])
            print("Current cost : ", current_node[2])
            print("CURRENT BOARD: ", current_board.grid)
            print("generating children OF THIS BOARD")
            current_board.get_children()
            children = current_board.children
            in_open = None
            
            # Visited nodes
            # Moving the current node to CLOSED
            self.closed.append(current_node)
            self.visited_boards.add(self.array_to_string(current_board.grid))
            if Board(self.closed[-1][0]).goal():
                goal = self.closed[-1]
                self.getSolutionPath()
                break


            print("nb of kids: ", len(children))
            for child in children:
                print()
                print("-----------------------")
                print("printing child")
                print(child)
                # visited = [node for node in self.closed if np.array_equal(child, node[0])]
                in_open = None
                if not self.array_to_string(child) in self.visited_boards:
                    print("open list")
                    print(self.open)
                    # check if current child board is found in the open list, if so, get that node + it's index
                    for index, node in enumerate(self.open):
                        if np.array_equal(child, node[0]):
                            in_open = [node, index]

                    # in_open = [node for node in self.open if np.array_equal(child, node[0])]    
                    
                    if not in_open:
                        print("this child is not in open, and not in closed, appending to open g(n): ", current_node[3] + 1 )
                        self.open.append((child, current_board, current_node[3] + 1, current_node[3] + 1, 0))
                    else:
                        print()
                        print("CURRENT BOARD: new child already in open, check if g(n) is lower")
                        print("g(n) of in open: ", in_open[0][3])
                        print("g(n) of potential child: ", current_node[3] + 1)
                        # current_board.print_board()
                        print("inopen")
                        print(in_open[0], in_open[1])
                        print(child)
                        if in_open[0][2] > current_node[3] + 1:
                            popped = self.open.pop(in_open[1])
                            self.open.append((child, current_board, current_node[3] + 1, current_node[3] + 1, 0))
                        else:
                            print("no popping, the one in open list is cheaper cost")
                            # continue
                else:
                    print("already visited in closed list")     
                    print("open list")
                    print(self.open)
                    # continue           

        print()
        if goal is not None:
            # Board(goal[0]).print_board()
            print("[total cost: {}]".format(goal[2]))
            end = time.time()
            return end - start
            # print('search length: {}'.format(x))
        else:
            print("Unsolvable noob")
        print("-------------------------------------------------------")

    def filter_visited(self, child_node):
        return [node for node in self.closed if not child_node.equals(node[0])]

    def printList(self, list):
        print("List length: {}".format(len(list)))
        for node in list:
            print("[cost: {}, total_cost: {}]".format(node[2], node[3]))
            node[0].printBoard()
         
    def getSolutionPath(self):
        # Start with the solution and backtrack to the start state
        goal = self.closed[-1]
        self.solution_path.append((goal[0], goal[2], goal[3], goal[4]))
        parent = goal[1]

        while parent != None:
            for node in self.closed:
                if parent.equals(node[0]):
                    self.solution_path.append((node[0], node[2], node[3], node[4]))
                    parent = node[1]
                    break
        
        self.solution_path.reverse()
        print("\nSolution Path: ")
        for node in self.solution_path:
            print(node[0])
            print("{} {} {} {} ".format(node[1], node[2], node[3], self.array_to_string(node[0])))
        print("Solution cost: ", len(self.solution_path) - 1, " moves")

    def array_to_string(self, array):
        grid = ""
        for list in array:
            grid += "".join(list)

        return grid
