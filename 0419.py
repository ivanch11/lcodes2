class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ships = 0
        for row in range( len(board) ):
            for col in range( len(board[0]) ):
                if row > 0 and board [row - 1][col] == "X":
                    continue
                if col > 0 and board [row][col - 1] == "X":
                    continue
                if board[row][col] == "X":
                    ships += 1
        return ships