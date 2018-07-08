class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tailList = [0] * len(nums)
        size = 0
        for n in nums:
            l, r = 0, size
            while l < r:
                mid = (l + r) // 2
                if tailList[mid] < n:
                    l = mid + 1                    
                elif n < tailList[mid]:
                    r = mid
                else:
                    r = mid
            tailList[l] = n
            if l + 1 > size:
                size += 1
        return size                    