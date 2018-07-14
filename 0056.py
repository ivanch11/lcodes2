# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key = lambda x: x.start)
        merge=[]
        for inter in intervals:
            if merge and merge[-1].end >= inter.start:
                merge[-1].end = max(merge[-1].end, inter.end)
            else:
                merge.append(inter)
        return merge