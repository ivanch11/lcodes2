class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        preDict = collections.defaultdict(set)
        neight = collections.defaultdict(set)
        for nextN, prevN in prerequisites:
            preDict[nextN].add(prevN)
            neight[prevN].add(nextN)
        candidate = [i for i in range(numCourses) if i not in preDict]
        #print("candidate: ", candidate)
        res = []
        while candidate:
            node = candidate.pop()
            for n in neight[node]:
                preDict[n].remove(node)
                if not preDict[n]:
                    candidate += [n]
            res += [node]
            #print ("preDict: ", preDict)
            preDict.pop(node, None)
        return res if len(res) == numCourses else []