# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return []
        
        self.dfs(res, root, 0)
        
        return res   
    
    def dfs(self,res, node, level):
        if node == None:
            return
        if level >= len(res):
            res.append([])
        res[level].append(node.val)
        self.dfs(res, node.left, level + 1)
        self.dfs(res, node.right, level + 1)          
         