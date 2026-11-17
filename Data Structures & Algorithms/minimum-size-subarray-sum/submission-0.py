class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        minSumLen = len(nums)
        currSum = 0
        flag = False
        while r < len(nums):
            currSum += nums[r]
            while currSum >= target:
                minSumLen = min(r - l + 1, minSumLen)
                currSum -= nums[l]
                l += 1
                flag = True
            r += 1

        if flag:
            return minSumLen 
        else: return 0
