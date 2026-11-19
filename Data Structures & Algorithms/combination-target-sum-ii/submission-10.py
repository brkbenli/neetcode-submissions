class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        sol = []
        candidates.sort()
        def backtrack(i):
            tot = sum(sol)
            if i == len(candidates) or tot > target:
                if tot == target:
                    res.add(tuple(sol[:]))
                return

            # use curr val
            sol.append(candidates[i])
            backtrack(i + 1)

            sol.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1)
        backtrack(0)

        return [list(i) for i in res]

    