class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)        
        if nr == 0:
            return 0
        nc = len(grid[0])
        if nc == 0:
            return 0
        
        def dfs(row, col):            
            if (row < 0 or row >= nr or col < 0 or col >= nc or grid[row][col] == "0"):
                return
            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        island_No = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    island_No += 1
                    dfs(r, c)
        return island_No