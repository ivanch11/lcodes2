class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        rowLen = len(dungeon)
        colLen = len(dungeon[0])
        minReq = [1]*colLen
        #minReq = [[1]*colLen]*rowLen
        #print (minReq)
        temp = 0 # store minimal requirement HP to enter right 
        for row in range(rowLen-1,-1,-1):
            
            for col in range(colLen-1,-1,-1):
                if row == len(dungeon)-1 and col == len(dungeon[0]) -1:
                    temp = max(1 - dungeon[-1][-1], 1)
                    minReq[-1] = temp
                    continue
                right = 2**31 -1
                down  = 2**31 -1      
                if row < rowLen-1:
                    down = max(minReq[col] - dungeon[row][col], 1)   
                if col < colLen-1:
                    right  = max(temp - dungeon[row][col], 1)
                temp = min(right, down)       
                
                minReq[col] = temp 
        return minReq[0]