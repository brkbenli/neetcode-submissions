class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        memo = {}
        def recurse(i, amount):
            if i >= len(coins) or amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if (i, amount) in memo:
                return memo[(i, amount)]

            # take
            take = 1 + recurse(i, amount - coins[i])
            # skip
            skip = recurse(i + 1, amount)

            res = min(take, skip)

            memo[(i, amount)] = res
            return res
        return recurse(0, amount) if recurse(0, amount) != float('inf') else -1
