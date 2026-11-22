class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = max(nums)

        currSum = 0
        for i in nums:
            currSum += i
            if currSum < 0:
                currSum = 0
                continue

            print(currSum)
            res = max(res, currSum)
        return res
