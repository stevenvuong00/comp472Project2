class GBFS:
    def __init__(self, board):
        self.board = board
        self.open= []
        self.closed = []
        self.closed_grids = []
        self.lowest_cost = 0
        self.solution_path = []
        self.solution_cost = 0 

    def search(self):
        # node object: (current node, parent, cost [f(n)], total_cost[g(n)], [h(n)])
        # Push initial state into open list
        self.open.append((self.board, None, 0, 0, self.board.h1()))
        # print(self.open[0])

        # x = 15
        length = 0
        while (len(self.open) > 0):
            # print("iteration ", x)
            # TODO: time stuff
            self.open = sorted(self.open, key=lambda x: x[4])
            length += 1

            # Remove first element from OPEN list
            currentNode = self.open.pop(0)
            print("currentNode: ", currentNode)
            self.board = currentNode[0]
            self.board.printBoard()

            # Add to visited nodes --> CLOSED list
            self.closed.append(currentNode)
            # self.closed_grids.append(currentNode[0])

            # Check if node is the goal state
            if currentNode[0].goal():
                # execution_time = time.time() - start_time
                # get solution path here
                currentNode[0].printBoard()
                print("goal")
                print("search length: ", length)
                return

            # # Get children (next state) of current state
            self.board.getChildren() 
            children = self.board.children

            # Only keep the children that aren't in the open or closed list
            for child in children:
                print()
                print("Child ")
                child.printBoard()

                # Find if the state is in the closed list
                visited = [node for node in self.closed if child.equals(node[0])]
                if not visited:
                    print("child has not been visited yet")

                    # Check if this child is in open list
                    in_open = [node for node in self.open if child.equals(node[0])]

                    # not in open 
                    if not in_open:
                        hn = child.h1()
                        self.open.append((child, currentNode[0], hn, 0, hn))
                        print('completely unvisited state')

                    # if current child is in open --> replace the one in open if hn is smaller for current child
                    else:
                        # TODO: do comparison f(n), g(n), h(n)
                        # Get the state that has the same one as the child
                        print('comparison and remove old one if the new one cost is lower')
                        # print("inopen")
                        # print(inopen)
                        # print(inopen[0][0].printBoard())
                        # print("current child")
                        # print("child h1: ", child.h1())
                        # child.printBoard()

                        # compare current with the one in inopen and replace with lower cost one
                        # compare the h(n) and remove
                        
            # x -= 1

            print("open length: ", len(self.open))
            print("closed length: ", len(self.closed))



