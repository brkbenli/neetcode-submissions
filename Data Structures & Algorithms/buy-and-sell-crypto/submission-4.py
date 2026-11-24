class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        maxFound = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                maxFound = max(maxFound, prices[r] - prices[l])
            else:
                l = r
            
        return maxFound
