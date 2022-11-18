import numpy as np

from board import Board


def print_list(node_list):
    print("List length: {}".format(len(node_list)))
    for node in node_list:
        print("[cost: {}, total_cost: {}]".format(node[2], node[3]))
        node[0].print_board()


class UCS:
    def __init__(self, board):
        self.board = board
        self.open = []
        self.closed = []
        self.lowest_cost = 0

    def search(self):
        print("OG board")
        self.board.print_board()

        # node object: (current node, parent, cost [f(n)], total_cost[g(n)])
        self.open.append((self.board.grid, None, 0))

        total_cost = 0
        x = 0
        goal = None

        while len(self.open) > 0:
            self.open = sorted(self.open, key=lambda k: k[2])
            # Sorting the OPEN list from lowest cost
            # sorted_open = sorted(self.open, key=lambda x: x[2])
            current_board = Board(self.open[0][0])
            current_board.get_children()
            children = current_board.children
            total_cost += 1
            # x += 1 # TODO for search path length
            in_open = None
            # test_list = filter(self.filter_visited, children)
            # print(test_list)
            for child in children:
                visited = [node for node in self.closed if np.array_equal(child, node[0])]
                if not visited:
                    # in_open = [node for node in self.open if child.equals(node[0])]
                    for index, node in enumerate(self.open):
                        if np.array_equal(child, node[0]):
                            in_open = [node, index]

                    if not in_open:
                        self.open.append((child, current_board, total_cost))
                    else:
                        if in_open[0][2] > total_cost:
                            self.open.pop(in_open[1])
                            self.open.append((child, current_board, total_cost))

            # Moving the current node to CLOSED
            self.closed.append(self.open.pop(0))
            if Board(self.closed[-1][0]).goal():
                goal = self.closed[-1]
                break
            # print()
            # current_board.print_board()

        print()
        if goal is not None:
            Board(goal[0]).print_board()
            print("[total cost: {}]".format(goal[2]))
            print('search length: {}'.format(x))
        else:
            print("Unsolvable noob")
        print("-------------------------------------------------------")

    def filter_visited(self, child_node):
        return [node for node in self.closed if not child_node.equals(node[0])]

