class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_set = set()
        i, j = 0, 0
        longest = 0
        while (j < n):
            if s[j] not in max_set:
                max_set.add(s[j])
                j += 1
                longest = max(longest, j - i)
            else:
                max_set.remove(s[i])
                i += 1
        return longest    