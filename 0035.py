class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """      
        start = 0
        end = len(nums) - 1               
        if nums == None or target < nums[0]:
            return 0
        if target > nums[end]:
            return end + 1        
        while start <= end:            
            mid = (start + end) // 2
            if target < nums[mid]:
                if start == mid:
                    return mid
                end = mid - 1
            elif target > nums[mid]:
                if mid == end:
                    return mid + 1
                start = mid + 1
            else:
                return mid       