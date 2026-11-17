class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        memo = {}
        def recurse(mi, ni):

            # base cases
            if mi == m - 1 and ni == n - 1:
                return 1
            if mi >= m or ni >= n:
                return 0

            # memo table
            if (mi, ni) in memo:
                return memo[(mi, ni)]

            # recurse
            res1 = recurse(mi + 1, ni)
            res2 = recurse(mi, ni + 1)

            memo[(mi, ni)] = res1 + res2
            return res1 + res2
        return recurse(0,0)
