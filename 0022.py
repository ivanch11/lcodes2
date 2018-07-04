class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def combineParenthesis( S = '' , left = 0, right = 0):
            if left < n:
                combineParenthesis(S + '(', left + 1, right)
            if right < left:
                combineParenthesis(S + ')', left, right + 1)
            if left + right == 2 * n:
                result.append(S)
                return                
        combineParenthesis()    
        return result