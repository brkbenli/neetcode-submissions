class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        currMax = 0
        l = 0
        r = 1
        while r < len(prices):
            if currMax < (prices[r] - prices[l]):
                currMax = max(prices[r] - prices[l], currMax)
            elif prices[r] - prices[l] < 0:
                l = r
            r += 1
        return currMax