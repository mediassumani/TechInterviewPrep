'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        if root == None:
            return []
        else:
            results = results + self.inorderTraversal(root.left)
            results = results + [root.val]
            results = results + self.inorderTraversal(root.right)

        return results
