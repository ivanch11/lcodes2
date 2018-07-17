class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        future_tank = 0
        tank = 0
        start = 0
        for i, g in enumerate(gas):
            tank += gas[i] - cost[i]
            if tank < 0:
                future_tank += tank
                tank = 0
                start = i + 1
        return -1 if tank + future_tank < 0 else start