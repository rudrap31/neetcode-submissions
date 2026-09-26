class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dfs = [0 for n in range(len(cost))]

        dfs[0], dfs[1] = 0, 0
        
        for i in range(2, len(cost)):
            dfs[i] = min(cost[i-1] + dfs[i-1], cost[i-2] + dfs[i-2])
        
        return dfs[-1]
            