class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        peri = 0
        totalRow = len(grid)
        totalCol = len(grid[0])
        for row in range(totalRow):
            for col in range(totalCol):
                if grid[row][col]:
                    if row == 0 or grid[row-1][col] == 0:
                        peri += 1
                    if col == 0 or grid[row][col-1] == 0:
                        peri += 1
                    if row == totalRow - 1 or grid[row+1][col] == 0:
                        peri += 1
                    if col == totalCol - 1 or grid[row][col+1] == 0:
                        peri += 1
        return peri                    