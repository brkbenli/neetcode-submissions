class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        newSet = set()
        for i in nums:
            if i not in newSet:
                newSet.add(i)
        
        maxLength = 0
        newSet = list(newSet)
        for i in range(0, len(newSet) - 1):
            length = 0
            while newSet[i] + 1 in newSet:
                length += 1
                maxLength = max(maxLength, length)
                i += 1


        return maxLength + 1
        print(newSet)