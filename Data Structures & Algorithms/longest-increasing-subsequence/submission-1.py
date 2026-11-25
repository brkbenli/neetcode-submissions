class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def recurse(i, prev):
            if i == len(nums):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]
            
            # take
            take = 0
            if prev < nums[i]:
                take = 1 + recurse(i + 1, nums[i])
            # skip
            skip = recurse(i + 1, prev)

            res = max(take, skip)
            memo[(i, prev)] = res
            return res
        return recurse(0, float('-inf'))