class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        diffDict = collections.defaultdict(list)
        for s in strings:
            key = self.genKey(s)
            diffDict[key].append(s)
        print ("diffDict.values(): ", diffDict.values())
        print ("list(diffDict.values()): ", list(diffDict.values()))
        print ("[diffDict.values()]: ", [diffDict.values()])
        return list(diffDict.values())
    
    def genKey(self, s):
        print ("s:", s)
        keyString = "0"
        for i in range(1, len(s)):
            keyString +=  "," + str( ( ord(s[i]) - ord(s[i-1]) )%26 )
        print("keyString: ", keyString)
        return keyString            