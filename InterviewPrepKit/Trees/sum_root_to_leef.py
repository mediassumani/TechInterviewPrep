class Solution(object):
    def dfs(self, node, string_value, result):
        
        string_value += str(node.val)

        # check if a node has no children
        if not node.left and not node.right:
            result += [string_value]
        
        # grab all children on the left of the current root
        if node.left:
            self.dfs(node.left, string_value, result)
           
        # grab all children on the right of the current root
        if node.right:
            self.dfs(node.right, string_value, result)
            
    def sumNumbers(self, root):
        
        if not root:
            return 0    
        res = []
        self.dfs(root, '', res)
        return sum(int(val) for val in res)
