'''
Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

'''
from collections import deque
from binarytree import BinarySearchTree

class Node(object):

    def __init__(self, cost):
        """Initialize this binary tree node with the given data."""
        self.data = cost
        self.children = []
        self.parent = None


def get_cheapest_cost(root):
    
    queue = deque([root])
    
    while len(queue) > 0:
        
        curr_node = queue.popleft()
        if curr_node.children:

            for child in curr_node.children:
                queue.append(child)
    
def main():

    root = Node(0)
    get_cheapest_cost(root)

if __name__ == "__main__":
    main()

    

    
    
