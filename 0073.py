class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for r in range(0, len(matrix)):
            if matrix[r][0] == 0:
                col0 = 0
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(len(matrix) - 1, -1, -1):
            for c in range(len(matrix[0]) - 1, 0, -1):
                if matrix[r][0] == 0 or matrix [0][c] == 0:
                    matrix[r][c] = 0
            if col0 == 0:
                matrix[r][0] = 0
        return
                    
                    