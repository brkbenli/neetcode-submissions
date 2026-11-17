class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = 0
        r = len(s) - 1
        while r > l:
            if s[r] == s[l]:
                l += 1
                r -= 1
            else:
                return False
        return True