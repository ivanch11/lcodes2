class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        len_nums = len(nums)
        
        if len_nums == 0:
            return [[]]
        
        nums.sort()
        used = [False] * len_nums
        new_num = []       
        
        def dfs():  
            #print ('len_nums:', len_nums)
            #print ('len(new_num):', len(new_num))
            if len(new_num) == len_nums:
                #print ('result 1: ', result)
                #print ('new_num:', new_num)
                k = new_num[:]
                result.append(k)
                #print ('result 2: ', result)
                return
            for i in range (len_nums):
                
                if used[i] or (i>0 and nums[i-1] == nums[i] and not used[i-1]):
                    continue
                used[i] = True
                new_num.append(nums[i])
                #print ('new_num: X0', new_num)
                dfs()
                #print ('i', i)
                #print ('new_num: X1', new_num)
                new_num.pop()
                #print ('new_num: X2', new_num)
                used[i] = False        

        dfs()        

        return result                