class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False        
        
        stack_k = []
        min_i = nums[0]
        min_J = [min_i]
        print ("min_J1: ", min_J)
        for i in range(1, len(nums)):
            min_J += [min(min_J[i-1] , nums[i])]
        print ("min_J2: ", min_J)
        for j in range(len(nums)-1, 0, -1):
            if nums[j]>min_J[j]:
                while stack_k and stack_k[-1] <= min_J[j]:
                    stack_k.pop()
                if stack_k and stack_k[-1] < nums[j]:
                    return True
                else:
                    stack_k += [nums[j]]
        return False            