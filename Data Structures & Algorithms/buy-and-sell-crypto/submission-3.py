class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        currProf = 0
        r = 1
        while r < len(prices):
            print(prices[l], prices[r])
            if 0 < prices[r] - prices[l]:
                currProf = max(prices[r] - prices[l], currProf)
                r += 1
            else:
                l = r
                r += 1
                
        return currProf