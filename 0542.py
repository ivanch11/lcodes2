class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return [[]]
        dist = [[2**31-1 for m in matrix[0]] for n in matrix]
        #print (dist)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    dist[row][col] = 0
                else:
                    if row > 0:
                        dist[row][col] = min(dist[row][col], dist[row-1][col] + 1)
                    if col > 0:
                        dist[row][col] = min(dist[row][col], dist[row][col-1] + 1)
        for row in range(len(matrix)-1,-1,-1):
            for col in range(len(matrix[0])-1,-1,-1):
                if row < len(matrix)-1:
                    dist[row][col] = min(dist[row][col], dist[row+1][col] + 1)
                if col < len(matrix[0])-1:
                    dist[row][col] = min(dist[row][col], dist[row][col+1] + 1)
        return dist