class Solution:  
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """        
        if not board:
            return
        rowLen = len(board)
        colLen = len(board[0])
        
        for row in range(rowLen):
            for col in range(colLen):
                lives = self.sumLive(board, row, col)
                if board[row][col] & 1 == 1 and lives >= 2 and lives <= 3:
                    board[row][col] = 0b11
                elif board[row][col] & 1 == 0 and lives ==3:
                    board[row][col] = 0b10
        for row in range(rowLen):
            for col in range(colLen):
                board[row][col]>>=1        
                
    def sumLive(self, board, row, col):
        rowLen = len(board)
        colLen = len(board[0])
        
        lives = 0
        for r in range( max(row - 1, 0), min(row + 2, rowLen )):
            for c in range( max(col - 1, 0), min(col + 2, colLen )):
                lives += board[r][c] & 1
        
        return lives - (board[row][col] & 1)