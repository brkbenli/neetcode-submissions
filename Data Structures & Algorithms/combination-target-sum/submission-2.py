class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []
        
        def backtrack(i):
            if i >= len(nums) or sum(sol) > target:
                if sum(sol) == target:
                    res.append(sol[:])
                return
            # use value
            sol.append(nums[i])
            backtrack(i)
            sol.pop()

            # skip
            backtrack(i + 1)

        backtrack(0)
        return res
                