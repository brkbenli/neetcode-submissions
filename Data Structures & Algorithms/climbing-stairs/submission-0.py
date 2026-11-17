class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def recurse(i):
            # base case
            if i == n:
                return 1
            elif i > n:
                return 0
            
            # memo check
            if i in memo:
                return memo[i]

            # recurse
            step1 = recurse(i + 1)
            step2 = recurse(i + 2)

            sol = step1 + step2

            memo[i] = sol
            return sol
        return recurse(0)