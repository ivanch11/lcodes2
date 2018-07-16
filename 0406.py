class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        height = []
        pdict = {}
        
        for i in range(len(people)):
            p = people[i]
            h = p[0]
            k = p[1]
            if h in pdict:
                pdict[h] += [[k, i]]
            else:
                pdict[h] = [[k, i]]
                height += [h]
        print (pdict)
        print (height)
        height.sort()
        
        for sameHeight in height[::-1]:
            pdict[sameHeight].sort()
            print (pdict[sameHeight])
            for p in pdict[sameHeight]:
                print (p[0])
                k = p[0]
                index = p[1]                
                res.insert(k, people[index])
        return res