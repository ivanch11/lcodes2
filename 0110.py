# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root)[1]
    def recur(self, node):
        if node == None:
            return (0, True)
        lHei, lBal = self.recur(node.left)
        rHei, rBal = self.recur(node.right)
        return 1+max(lHei, rHei), lBal and rBal and abs(lHei-rHei)<=1