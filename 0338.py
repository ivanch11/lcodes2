class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bitCount = [0]
        for i in range(1, num + 1):
            bitCount.append( bitCount[i & i-1] + 1 )
        return bitCount