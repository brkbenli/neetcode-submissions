class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def isvalid(k):
            # using k its gonna check if k value works
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / k)
            if count <= h:
                return True
            else:
                return False


        # ceiling of i / 2 
        l = 1
        r = max(piles)
        res = max(piles)
        while r >= l:
            middle = (r + l) // 2
            if isvalid(middle):
                res = min(res, middle)
                r = middle - 1
            else:
                l = middle + 1
        return res
            
            

        