class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0 or len(nums) == 0:
            return False
        freqHash = {}
        for i in range(len(nums)):
            if freqHash.get(nums[i], 0):
                return True
            freqHash[nums[i]] = 1
            if i - k >= 0:
                freqHash[nums[i-k]] = 0
        return False