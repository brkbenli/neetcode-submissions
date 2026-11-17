class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0

        hashmap = {}
        res = 0
        while r < len(s):
            
            # counter in hashmap
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] += 1


            if max(hashmap.values()) - sum(hashmap.values()) + k >= 0:
                
                r += 1
            
            else:
                while max(hashmap.values()) - sum(hashmap.values()) + k < 0:
                    l += 1
                    hashmap[s[l]] -= 1
            res = max(res, r - l)
        return res