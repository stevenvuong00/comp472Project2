
from asyncio.windows_events import NULL

class UCS:
    def __init__(self, board):
        self.board = board
        self.open = []
        self.closed = []
        self.lowest_cost = 0
        self.solution_path = []
        self.solution_cost = 0
    
    def search(self):
        print("OG board")
        # self.board.printBoard()

        # node object: (current node, parent, f(n), g(n), h(n))
        self.open.append((self.board, None, 0, 0, 0))
        current_node = self.board
        # total_cost = 0
        # x = 0
        goal = None
        while(len(self.open) > 0):
            # Sorting the OPEN list from lowest cost
            self.open = sorted(self.open, key=lambda x: x[2])
            current_node = self.open[0]
            current_node[0].getChildren()
            children = current_node[0].children
            # total_cost += 1
            # x += 1
            in_open = None
            for child in children:
                visited = [node for node in self.closed if child.equals(node[0])]
                if not visited:
                    # in_open = [node for node in self.open if child.equals(node[0])]
                    for index, node in enumerate(self.open):
                        if(child.equals(node[0])):
                            in_open = [node, index]
                    if not in_open:
                        child_node = (child, current_node, current_node[2] + 1, current_node[3] + 1, 0)
                        self.open.append(child_node)
                    else:
                        # in_open[0][2] --> g(n) of the same board found in open list
                        if(in_open[0][2] > current_node[3]):
                            self.open.pop(in_open[1])
                            self.open.append((child, current_node, current_node[2] + 1, current_node[3] + 1, 0))

            # Moving the current node to CLOSED
            self.closed.append(self.open.pop(0))
            
            if(self.closed[-1][0].goal()):
                goal = self.closed[-1]
                self.getSolutionPath()
                break
            print()
            
            # current_node[0].printBoard()

            
        print()
        if(goal is not None):
            # goal[0].printBoard()
            print("[total cost: {}]".format(goal[2]))
            # print('search length: {}'.format(x))
        else:
            print("Unsolvable noob")
        print("-------------------------------------------------------")

    def printList(self, list):
        print("List length: {}".format(len(list)))
        for node in list:
            print("[cost: {}, total_cost: {}]".format(node[2], node[3]))
            node[0].printBoard()
         
    def getSolutionPath(self):
        # Start with the solution and backtrack to the start state
        # node: board, fn, gn, hn
        current_node = self.closed[-1]
        parent_node = current_node[1] # goal state parent board
        self.solution_path.append((current_node[0], current_node[2], current_node[3], current_node[4]))

        # print(self.closed)
        while parent_node[1] != None:
            # found parent board in the closed list, that means it's the list that we visited to reach the goal state:
                self.solution_path.append((parent_node[0], parent_node[2], parent_node[3], parent_node[4]))
                parent_node = parent_node[1]

        self.solution_path.reverse()
        print("\n Solution Path: ")
        # for node in self.solution_path:
        #     node[0].printBoard()
        print("Solution cost: ", len(self.solution_path))

