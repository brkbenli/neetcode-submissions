class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # state - buying or selling? - boolean
        # if buy i + 1
        # if sell i + 2 (includes cooldown)
        
        memo = {}
        def recurse(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in memo:
                return memo[(i, buying)]
            
            if buying:
                buy = recurse(i + 1, not buying) - prices[i]
                cooldown = recurse(i + 1, buying)
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = recurse(i + 2, not buying) + prices[i]
                cooldown = recurse(i + 1, buying)
                memo[(i, buying)] = max(sell, cooldown)

            return memo[(i, buying)]

        return recurse(0, True)

            
