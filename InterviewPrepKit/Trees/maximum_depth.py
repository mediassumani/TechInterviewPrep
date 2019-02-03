# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def maxDepth(self, root):
    ''' Using DFS to traverse the tree at each level'''
    if root is None:
        return 0

    else:
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)


        if left_depth > right_depth:
            return left_depth+1
        else:
            return right_depth+1
