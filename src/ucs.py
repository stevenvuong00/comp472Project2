from board import Board
import queue
from heapq import *
from queue import PriorityQueue
import time
from threading import Timer, Thread
import multiprocessing
from multiprocessing import *
import numpy as np 

class UCS:
    def __init__(self, board):
        self.board = board
        self.open = []                 
        self.closed = []
        self.closed_grids = []
        # self.pq = PriorityQueue()
        # self.nodes = []
        self.solution_path = []
        self.solution_cost = 0
        self.p = Thread(target=self.search, name="UCS", args=({}))
        # self.timeout = False 
        # self.return_dict = {"success":False, "execution":0}     

    # def search(self):
    #     start_time = time.time()
    #     print("Searching...")

    #     # Push initial state into PQ
    #     # CURRENTBoard, parent fn, gn, hn, 
    #     self.pq.put((self.board, self.board.parent, 0, 0, 0))
    #     self.open.append((self.board, self.board.parent, 0, 0, 0))
    #     current_node = self.board

    def search(self):
        # node object: (current node, parent, cost [f(n)], total_cost[g(n)])
        start_time = time.time()
        self.open.append((self.board, None, 0, 0))
        current_node = self.board
        total_cost = 0
        # self.board.printBoard()

        # Push initial state into open
        # node object: (current node, parent, cost [f(n)], total_cost[g(n)])
        self.open.append((self.board, None, 0, 0))

        # While there are states in the open list --> keep searching
        while len(self.open) > 0:
            # Remove first element from OPEN
            currentNode = self.open.pop(0)
            print(currentNode)
            # print(currentNode[0].printBoard())
            print(len(self.open))
            self.board = currentNode[0]
            print(self.board.printBoard())

            # Add to visited nodes --> CLOSED list
            self.closed.append(currentNode)
            self.closed_grids.append(currentNode[0])

            # Check if node is the goal state
            if self.board.goal():
                execution_time = time.time() - start_time
                print("GOOOOOOALLLL")

            # Get children of current state
            children = self.board.getChildren()
            print(children)
            # # Only keep the children than are not in open or closed list
            # for child in children:
            #     # child visited already --> TODO: compare path
            #     if self.visited(self, child):
            #         print("Node has been visited already")
            #     # not visited yet --> create new node and add to open 
            #     else :
            #         child_node = (child, currentNode, currentNode[2] + 1, currentNode[3] + 1)
            #         self.open.append(child_node)

            #         self.open = sorted(self.open, key=lambda x: x[2])
            #         currentNode = self.open[0][0]



        # while(current_node.goal() is not True):
        #     current_node.getChildren()
        #     children = current_node.children # board objects
        #     total_cost += 1
        #     isVisited = False
        #     print("children:")
        #     for child in children:
        #         child.printBoard()
        #         print()
        #         # checking if children state has already been visited
        #         if(len(self.closed) > 0):
        #             for visited in self.closed:
        #                 if child.equals(visited[0]):
        #                     isVisited = True
        #                     break
        #         # new node and add to open list
        #         if(isVisited is False):
        #             child_node = (child, current_node, child.cost, total_cost)
        #             self.open.append(child_node)
        #         isVisited = False
        #     # print(" ITERATION ")
        #     # self.printList(self.open)

        #     # Moving the current node to CLOSED
        #     print("self open length before pop {}".format(len(self.open)))
        #     self.closed.append(self.open.pop())
        #     print("self open length after pop {}".format(len(self.open)))

        #     # Sorting the OPEN list from lowest cost
        #     sorted_open = sorted(self.open, key=lambda x: x[2])
        #     current_node = sorted_open[0][0]
        #     # print(" CURRENT NODE: ")
        #     # current_node.printBoard()
        #     print()
        # # current_node.print_board

    def printList(self, list):
        for node in list:
            if node != None:
                node[0].printBoard()
    
    # grid: board that we want to check if in closed list or not
    def visited(self, grid):
        if len(self.closed_grids) > 0:
            for visitedGrid in self.closed_grids:
                if np.array_equal(grid, visitedGrid):
                    return True
            # the grid is not in closed list
            return False
        return False    
