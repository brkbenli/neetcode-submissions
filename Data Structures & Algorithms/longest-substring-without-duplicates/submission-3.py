class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
            hashSet = set()
            maxLen = 0
            l, r = 0, 0

            # loop through s
            while r < len(s):
                # get the max length
                # if char not in set, add it
                if s[r] not in hashSet:
                    hashSet.add(s[r])
                else:
                    while s[r] in hashSet:
                        hashSet.remove(s[l])
                        l += 1
                    hashSet.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
            return maxLen

                
