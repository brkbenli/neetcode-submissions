class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        currMin, currMax = 1, 1

        for i in nums:
            if i == 0:
                currMin, currMax = 1, 1
                continue
            temp = currMax * i
            currMax = max(currMax * i, currMin * i, i)
            currMin = min(currMin * i, temp, i)
            res = max(res, currMax)

        return res
        