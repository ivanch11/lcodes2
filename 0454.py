class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        freq = collections.defaultdict(int)
        for a in A:
            for b in B:
                freq[a+b] += 1
        for c in C:
            for d in D:
                res += freq[-c-d]
        return res