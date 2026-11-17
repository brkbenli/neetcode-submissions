class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maxCap = sum(weights)
        minCap = max(weights)

        print(maxCap, minCap)

        def canShip(cap):
            currCap = cap
            ships = 1
            for i in range(len(weights)):
                if currCap - weights[i] < 0:
                    ships += 1
                    currCap = cap
                currCap -= weights[i]
            return ships <= days  
            
        res = maxCap
        left = minCap
        right = maxCap
        while right >= left:
            mid = (right + left) // 2
            if canShip(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
            
        