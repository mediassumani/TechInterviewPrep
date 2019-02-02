'''
Question 4:
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

   return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
from collections import deque

def level_order(root):
    ''' Using BFS to traverse and get each data from the node'''

    return_list = []
    list_of_queues = ([root])

    while len(list_of_queues) > 0:
        curr_node = list_of_queues.popleft()
        return_list.append([node.data])

        if curr_node.left:
            list_of_queues.append(curr_node.left)
        if curr_node.right:
            list_of_queues.append(curr_node.right)

    return list_of_queues
