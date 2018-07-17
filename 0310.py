class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        adj = []
        for _ in range(n):
            adj += [set()]
        
        for e in edges:
            i = e[0]
            j = e[1]
            adj[i].add(j)
            adj[j].add(i)
        
        leaves = []
        for i, v in enumerate(adj):            
            if len(v) == 1:
                leaves += [i]
        print ("leaves1: ", leaves)
               
        while n > 2:
            newLeaves = []
            n -= len(leaves)
            for l in leaves:
                j = adj[l].pop()
                adj[j].remove(l)
                if len(adj[j]) == 1:
                    newLeaves += [j]
            leaves = newLeaves
            print ("leaves: ", leaves)
        return leaves                