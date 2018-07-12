class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for j in range(len(nums)):
            compliment = target - nums[j]
            n = hashmap.get(compliment)
            if n and n != j:
                return [j, n]
        return []          
        