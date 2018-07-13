class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            #if i>0 and nums[i] == nums[i-1]:
            i += 1
            j = i + 1
            k = len(nums) - 1
            print ("i,j,k: ", i,j,k)
            while j<k:
                if nums[i]+nums[j]+nums[k] == 0:
                    print ("i,j,k 2: ", i,j,k)
                    result.append([ nums[i], nums[j], nums[k] ])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]: 
                        k -= 1
                elif nums[j]+nums[k] > nums[i]:
                    k -= 1
                else:
                    j += 1
        return result  