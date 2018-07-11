class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freq = {}
        for c_s in s:
            c_k = freq.get(c_s)
            if c_k:
                freq[c_s] += 1
            else:
                freq[c_s] = 1
        for c_t in t:
            c_k = freq.get(c_t)
            if c_k != None:
                if c_k > 1:
                    freq[c_t] -= 1
                else:
                    del freq[c_t]
            else:
                return False
        return True