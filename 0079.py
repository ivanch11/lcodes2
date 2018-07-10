class Solution:    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, word, row, col):              
                    return True
        return False
    
    def dfs(self, board, word, row, col):
        
        res = False
        length_word = len(word)
        if length_word == 0:
            return True                        

        if row < 0 or row > len(board) - 1 or col < 0 or col > len(board[0]) - 1:

            return False       
        tmp = "&"
        
        if board[row][col] == word[0]:
            tmp = board[row][col]
            board[row][col] = "#" 
            
            res = self.dfs(board, word[1:], row - 1, col) or self.dfs(board, word[1:], row + 1, col) or \
                  self.dfs(board, word[1:], row, col - 1) or self.dfs(board, word[1:], row, col + 1)
            board[row][col] = tmp
        return res     
           