class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lastIndex = {c: i for i, c in enumerate(s)}
        res = ""
        for i, c in enumerate(s):
            if c not in res:
                while c < res[-1:] and i < lastIndex[ res[-1:] ]:
                    res = res[:-1]
                res += c                
        return res                