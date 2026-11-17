class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol = []
        res = []
        def backtrack(target, i):
            if sum(sol) == target:
                res.append(sol[:])
                return
            if i >= len(nums) or sum(sol) > target:
                return

            # use first
            sol.append(nums[i])
            backtrack(target, i)

            sol.pop()
            backtrack(target, i + 1)
        backtrack(target, 0)
        return res
            