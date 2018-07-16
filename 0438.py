class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pHash = {}
        start = 0
        end = 0
        res = []
        
        for c in p:
            pHash[c] = pHash.get(c, 0) + 1
        counter = len(pHash)
        
        while end < len(s):
            #print ("end: ", end)
            
            #print ("pHash.get(s[end], None) : ", pHash.get(s[end], None))
            #print ("pHash.get(s[end], None) != None : ", pHash.get(s[end], None) != None)
            #print ("s[end] in pHash : ", s[end] in pHash)
            #if s[end] in pHash:
            if pHash.get(s[end], None) != None:
                pHash[s[end]] -= 1
                if pHash[s[end]] == 0:
                    counter -= 1
            end += 1
            #print ("start1: ", start)
            while counter == 0:
                #print ("start2: ", start)
                #print ("pHash.get(s[start]) != None : ", pHash.get(s[start]) != None)
                #print ("s[start] in pHash : ", s[start] in pHash)
                #if s[start] in pHash:
                if pHash.get(s[start]) != None:
                    #print ("pHash[s[start]] 1: ", pHash[s[start]])
                    pHash[s[start]] += 1
                    #print ("pHash[s[start]] 2: ", pHash[s[start]])
                    if pHash[s[start]] > 0:
                        #print ("pHash[s[start]] > 0 :", pHash[s[start]] > 0)
                        counter += 1
                if end - start == len(p):
                    #print ("res + [start] : ", res + [start])
                    res = res + [start]
                start += 1
                #print ("counter: ", counter)
        return res