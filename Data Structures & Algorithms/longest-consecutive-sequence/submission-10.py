class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = set(nums)
        maxVal = 0
        for i in nums:
            if i - 1 not in hashset:
                count = 0
                currval = i
                while currval in hashset:
                    count += 1
                    currval += 1
                maxVal = max(maxVal, count)
        return maxVal
