class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profSum = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profSum += prices[r] - prices[l]
                l = r
            r += 1
        return profSum
            