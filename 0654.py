class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def findMax(start, end):
            print ("start end:", start, " ", end)
            if start == end:                
                return TreeNode(nums[start])
            max_num = max(nums[start : end+1])
            maxIndex = nums.index(max_num)
            node = TreeNode(max_num)
            if start < maxIndex:
                node.left = findMax(start, maxIndex - 1)
            if maxIndex < end:
                node.right = findMax(maxIndex + 1, end)
            return node
        
        return findMax(0, len(nums) - 1)