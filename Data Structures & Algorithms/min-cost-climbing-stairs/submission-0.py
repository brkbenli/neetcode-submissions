class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def recurse(i):
            # base case
            if i >= len(cost):
                return 0

            # memo table
            if i in memo:
                return memo[i]

            # recurse
            res = min(cost[i] + recurse(i + 1), cost[i] + recurse(i + 2))

            memo[i] = res
            return res

        return min(recurse(0), recurse(1))