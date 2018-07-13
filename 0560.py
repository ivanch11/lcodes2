class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {0:1}
        sum = 0
        count = 0
        for n in nums:
            sum += n            
            count += freq.get(sum - k, 0)
            freq[sum] = freq.get(sum, 0) + 1
        return count        