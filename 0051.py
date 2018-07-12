class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queens, diff, plus):
            p = len(queens)
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in diff and p+q not in plus:
                    dfs(queens + [q], diff + [p-q], plus + [p+q])
        result = []
        dfs([], [], [])
        
        return [[ "."*col + "Q" + "."*(n-col-1) for col in row] for row in result]                