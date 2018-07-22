class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for n in nums:
            diff ^= n
        diff &= -diff
        ans = [0, 0]
        for n in nums:
            if n & diff:
                ans[0] ^= n
            else:
                ans[1] ^= n
        return ans