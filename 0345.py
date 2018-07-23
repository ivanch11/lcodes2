class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) -1
        ans = s
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while left < right:
            while left <= right and s[left] not in vowels:
                left += 1
            while left <= right and s[right] not in vowels:
                right -= 1
            if left < right:
                #print (ans[:left] + ans[right] + ans[left + 1:right] \
                #    + ans[left]+ ans[right + 1:])
                
                ans = ans[:left] + ans[right] + ans[left + 1:right] \
                    + ans[left]+ ans[right + 1:]
                #s[left], s[right] = s[right], s[left]
                #print ("ans:", ans)
                left += 1
                right -= 1
        return ans                