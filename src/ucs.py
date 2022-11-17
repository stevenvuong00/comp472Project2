
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
        self.open.append((self.board, None, 0))
        current_node = self.board
        total_cost = 0
        x = 0
        goal = None
        while(len(self.open) > 0):
            # Sorting the OPEN list from lowest cost
            # sorted_open = sorted(self.open, key=lambda x: x[2])
            current_node = self.open[0][0]
            current_node.getChildren()
            children = current_node.children
            total_cost += 1
            x += 1
            in_open = None
            for child in children:
                visited = [node for node in self.closed if child.equals(node[0])]
                if not visited:
                    # in_open = [node for node in self.open if child.equals(node[0])]
                    for index, node in enumerate(self.open):
                        if(child.equals(node[0])):
                            in_open = [node, index]
                    if not in_open:
                        child_node = (child, current_node, total_cost)
                        self.open.append(child_node)
                    else:
                        if(in_open[0][2] > total_cost):
                            self.open.pop(in_open[1])
                            self.open.append((child, current_node, total_cost))

            # Moving the current node to CLOSED
            self.closed.append(self.open.pop(0))
            if(self.closed[-1][0].goal()):
                goal = self.closed[-1]
                break
            print()
            
            current_node.printBoard()

            
        print()
        if(goal is not None):
            goal[0].printBoard()
            print("[total cost: {}]".format(goal[2]))
            print('search length: {}'.format(x))
        else:
            print("Unsolvable noob")
        print("-------------------------------------------------------")

    def printList(self, list):
        print("List length: {}".format(len(list)))
        for node in list:
            print("[cost: {}, total_cost: {}]".format(node[2], node[3]))
            node[0].printBoard()
         