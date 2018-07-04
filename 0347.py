class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqHashmap = {}
        freqList = [None] * ( len(nums) + 1 )
        result = [] 
        for i in nums:
            freqHashmap[i] = freqHashmap.get(i, 0) + 1
        for key in freqHashmap.keys():
            freq = freqHashmap[key]
            if freqList[freq] == None:
                freqList[freq] = []
            freqList[freq].append(key)
        m = 0
        for j in freqList[::-1]:    
            if j != None:
                m += len(j)
                result.extend(j)
            if m >= k:
                break            
        return result[0:k]