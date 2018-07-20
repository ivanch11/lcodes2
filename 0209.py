class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        p1 = 0
        
        sums = 0  
        minLength = 2**31 - 1
        for p2 in range(len(nums)):
            sums += nums[p2]
            
            while sums >= s:
                
                curLength = p2 + 1 - p1
                #print ("curLength: ", curLength)
                #print ("minLength: ", minLength)
                if minLength > curLength:
                    #print ("minLength > curLength: ", minLength > curLength)
                    minLength = curLength
                    
                sums -= nums[p1]
                p1 += 1
        return  0 if minLength == 2**31 - 1 else minLength