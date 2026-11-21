class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        count = 0
        def recurse(i, amount):
            if amount == 0:
                return count
            if amount < 0 or i >= len(coins):
                return float('inf')
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            take = 1 + recurse(i, amount - coins[i])
            skip = recurse(i + 1, amount)

            res = min(take, skip)
            
            memo[(i, amount)] = res

            return res
        res = recurse(0, amount)
        return -1 if res == float('inf') else res
        