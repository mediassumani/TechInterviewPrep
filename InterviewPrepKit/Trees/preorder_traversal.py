'''
Given a binary tree, return the preorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        if root is None:
            return []
        else:
            results = results + [root.val]
            results = results + self.preorderTraversal(root.left)
            results = results + self.preorderTraversal(root.right)
        return results
