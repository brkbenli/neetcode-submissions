class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            print(seen)
            if s[r] in seen:
                while s[r] in seen:
                    print(l)
                    print(s[l])
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])
            maxLen = max(len(seen), maxLen)
        return maxLen
