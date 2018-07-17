class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqHash = {}
        for c in s:
            freqHash[c] = freqHash.get(c, 0) + 1
        for i, c in enumerate(s):
            if freqHash[c] == 1:
                return i
        return -1