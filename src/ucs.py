
from asyncio.windows_events import NULL

class UCS:
    def __init__(self, board):
        self.board = board
        self.open = []
        self.closed = []
        self.lowest_cost = 0
    
    def search(self):
        print("OG board")
        self.board.printBoard()

        # node object: (current node, parent, cost [f(n)], total_cost[g(n)])
        self.open.append((self.board, None, 0, 0))
        current_node = self.board
        total_cost = 0
        goal = None
        while(len(self.open) > 0):
            # Sorting the OPEN list from lowest cost
            sorted_open = sorted(self.open, key=lambda x: x[2])
            current_node = sorted_open[0][0]
            current_node.getChildren()
            children = current_node.children
            total_cost += 1
            for child in children:
                isVisited = False
                if(len(self.closed) > 0):
                    for visited in self.closed:
                        if(child.equals(visited[0])):
                            isVisited = True
                            break
                if(isVisited):
                    continue
                else:
                    child_node = (child, current_node, child.cost, total_cost)
                    self.open.append(child_node)

            # Moving the current node to CLOSED
            self.closed.append(self.open.pop(0))
            if(self.closed[-1][0].goal()):
                goal = self.closed[-1][0]
                break
            print()
            current_node.printBoard()

            
        print()
        if(goal is not None):
            goal.printBoard()
            print("[cost: {}]".format(goal.cost))
        else:
            print("Unsolvable noob")
        print("-------------------------------------------------------")

    def printList(self, list):
        print("List length: {}".format(len(list)))
        for node in list:
            print("[cost: {}, total_cost: {}]".format(node[2], node[3]))
            node[0].printBoard()
         