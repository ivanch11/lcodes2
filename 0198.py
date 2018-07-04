class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curmax = 0
        prevmax = 0
        for n in nums:
            tempmax = curmax
            curmax = max( prevmax + n , curmax)
            prevmax = tempmax
        return curmax