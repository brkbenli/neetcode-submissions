class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        import sys
        memo = {}
        def recurse(i, j):
            sys.setrecursionlimit(100000)
            if i < 0 or j >= len(s) or i > j:
                return ""

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i:j + 1] == s[i:j+1][::-1]:
                memo[(i, j)] = s[i:j + 1]
                return s[i:j + 1]
            
            # just left
            res1 = recurse(i + 1, j)
            # just right
            res2 = recurse(i, j - 1)
            # left and right
            
            res = max(res1, res2, key=len)

            memo[(i, j)] = res
            return res

        recurse(0, len(s) - 1)
        valLen = ""
        for value in memo.values():
            if len(value) >= len(valLen):
                valLen = value

        return valLen
            

            