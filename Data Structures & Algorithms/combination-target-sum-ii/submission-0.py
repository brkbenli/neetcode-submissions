class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        sol = []

        candidates.sort()
        
        def backtrack(target, i):
            if sum(sol) == target:
                res.add(tuple(sol[:]))
                return

            if i >= len(candidates) or target < sum(sol):
                return

            sol.append(candidates[i])

            # backtrack
            backtrack(target, i + 1)

            sol.pop()

            backtrack(target, i + 1)
            
        
        backtrack(target, 0)
        print(res)
        return [list(x) for x in res]
