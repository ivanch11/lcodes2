class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_v = 2**31 - 1
        for i in range(0, len(prices)):
            if prices[i] < min_v:
                min_v = prices[i]
            elif profit < prices[i] - min_v:
                profit = prices[i] - min_v
        return profit