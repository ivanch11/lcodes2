class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        height = len(matrix)
        width = len(matrix[0])
        row, col = height - 1, 0
        while row >= 0 and col < width:
            if target < matrix[row][col]:
                row -= 1
            elif target > matrix[row][col]:
                col += 1
            else:
                return True
        return False