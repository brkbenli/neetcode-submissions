class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l = 0
        r = 0
        res = 0
        count = {}
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            
            if (r - l + 1) - max(count.values()) <= k:
                res = max(res, r - l + 1)
                r += 1
            else:
                count[s[l]] -= 1
                l += 1
               
        return res