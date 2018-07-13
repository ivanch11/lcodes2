# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue = -1*2**31
        self.dfs(root)
        return self.maxValue
    
    def dfs(self, node):
        if node == None:
            return 0
        left = max(0, self.dfs(node.left) )
        right = max(0, self.dfs(node.right))
        self.maxValue = max(self.maxValue, left + right + node.val)
        return max(left, right) + node.val

class Solution2:
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxValue = -1*2**31
                
        dfs(root)
        
        def dfs(node):
            if node == None:
                return 0
            left = max(0, dfs(node.left) )
            right = max(0, dfs(node.right))
            maxValue = max(maxValue, left + right + node.val)
            return max(left, right) + node.val        
        return maxValue
    
