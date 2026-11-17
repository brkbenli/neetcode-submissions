class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        sol = []
        def backtrack(i, target):
            if sum(sol) == target:
                res.add(tuple(sol[:]))
            if i >= len(nums) or sum(sol) > target:
                return
            
            
            sol.append(nums[i])
            backtrack(i, target)

            sol.pop()
            backtrack(i + 1, target)
        backtrack(0, target)
        return [list(x) for x in res]
        print(res)