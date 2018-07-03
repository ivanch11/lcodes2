class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        if S > 1000 or S < -1000:
            return 0
        
        countList = [0] * 2001
        #nextCountList = [0] * 2001
        countList[ 1000 + nums[0] ] = 1
        countList[ 1000 - nums[0] ] += 1
        for i in range (1 , len( nums ) ):
            nextCountList = [0] * 2001
            for sum in range ( 2001 ):
                if ( countList[ sum ] ):
                    nextCountList[ sum + nums[i] ] += countList[ sum ]
                    nextCountList[ sum - nums[i] ] += countList[ sum ]
            countList = nextCountList
        return countList[S + 1000]