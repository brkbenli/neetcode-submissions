class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        res = set()
        sol = []
        nums.sort()
        def backtrack(i):
            if i >= len(nums):
                res.add(tuple(sol[:]))
                return
            
            # include
            sol.append(nums[i])
            backtrack(i + 1)

            # dont include
            sol.pop()
            backtrack(i + 1)
        backtrack(0)
        return [list(i) for i in res]
        