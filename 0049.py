class Solution:    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for str in strs:
            freq = [0] * 26
            for c in str:
                freq[ord(c)- ord("a")] += 1
            dict.setdefault(tuple(freq), [] ).append(str)
        return list(dict.values())