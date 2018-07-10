class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        tries = {}
        for w in words:
            t = tries
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t["#"] = "#"
        
        res = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board, tries, row, col, res, "")
        return list(res)
    
    def dfs(self, board, tries, row, col, res, path):
        if "#" in tries:
            res.add(path)
        if row<0 or row>len(board)-1 or col<0 or col>len(board[0])-1:
            return
        c2 = board[row][col]        
        if c2 in tries:
            board[row][col] = "&"
            t2 = tries[c2]
            self.dfs(board, t2, row+1, col, res, path+c2)
            self.dfs(board, t2, row-1, col, res, path+c2)
            self.dfs(board, t2, row, col+1, res, path+c2)
            self.dfs(board, t2, row, col-1, res, path+c2)
            board[row][col] = c2        