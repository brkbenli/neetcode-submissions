class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        currSum = 0

        r, l = 0, 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
            else:
                currSum += prices[r] - prices[l]
                l += 1
            r += 1
        return currSum