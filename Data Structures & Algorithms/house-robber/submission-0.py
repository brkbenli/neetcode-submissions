class Solution:
    def rob(self, nums: List[int]) -> int:
        

        memo = {}
        def recurse(i):
            # base case
            if i >= len(nums):
                return 0

            res = max(recurse(i + 1), nums[i] + recurse(i + 2))
            memo[i] = res

            return res
        return recurse(0)
