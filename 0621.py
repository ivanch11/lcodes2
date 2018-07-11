class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import queue
        pq = queue.PriorityQueue()        
        freq = [0]*26
        for c in tasks:
            freq[ord(c) - ord("A")] -= 1
        for f in freq:
            if f != 0:
                pq.put(f)
        time = 0
        while (not pq.empty()):
            i = 0
            temp = []
            while (i<=n):
                if (not pq.empty()):
                    f_sub = pq.get() + 1
                    if f_sub < 0:
                        temp.append( f_sub )
                time += 1
                i += 1
                if (len(temp) == 0):
                    break
            #print("temp1:",temp)    
            for _ in range(len(temp)):
                pq.put(temp[0])
                temp.pop(0)
            #print("temp2:",temp)                
        return time