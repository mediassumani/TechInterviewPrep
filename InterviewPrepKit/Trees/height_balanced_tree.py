'''

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

'''
    def getDepth(self, node):
        
        left_depth = 0
        right_depth = 0
        curr = node
        
        if (node.left is None) and (node.right is None):
            return 0
        
        if curr.left:
            left_depth = self.getDepth(curr.left)
            
        if curr.right:
            right_depth = self.getDepth(curr.right)
            
        return max(left_depth, right_depth) + 1
        
        
   def isBalanced(self, root):

         if not root:
             return False
        
         if (root.left is None) and (root.right is None):
             return True
        
         if (root.left is None) or (root.right is None):
             return True
        
         max_left_depth = self.getDepth(root.left)
         max_right_depth = self.getDepth(root.right)
        
         if (max_left_depth - max_right_depth) > 1 or (max_right_depth - max_left_depth) > 1:
             return False
        
         return True
    
