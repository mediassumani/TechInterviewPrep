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

def levelOrder(self, root):
    if root is None:
        return []

    return_list = [[root.val]]
    list_of_queues = deque([root])

    while len(list_of_queues) > 0:
        curr_node = list_of_queues.popleft()
        temp = []
        if curr_node.left:
            temp.append(curr_node.left.val)
            list_of_queues.append(curr_node.left)
        if curr_node.right:
            temp.append(curr_node.right.val)
            list_of_queues.append(curr_node.right)
        if len(temp) != 0:
            return_list.append(temp)

    return return_list
