class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l = 0
        r = 0
        res = 0
        count = {}
        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
                
            print(r, "r")
            print(l, "l")
            print(max(count.values()))
            print(count)
            
            if (r - l + 1) - max(count.values()) <= k:
                r += 1
                res = max(res, r - l)
            else:
                count[s[l]] -= 1
                l += 1
               
        return res