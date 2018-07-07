class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        result = []
        
        def dfs(hrs, mins, n, start_index):
            if hrs >= 12 or mins > 59:
                return
            if  n == 0:
                result.append( str(hrs)+ ":"+ "0" * (mins < 10) + str(mins) )
                return
            for i in range (start_index, 10):
                if i < 4:
                    dfs(hrs | (1<<i), mins, n-1, i+1)
                else:
                    dfs(hrs, mins | (1<<i - 4), n-1, i+1)
        
        dfs(0, 0, num, 0)
        
        return result