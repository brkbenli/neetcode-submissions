class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        newSet = set()
        for i in nums:
            if i not in newSet:
                newSet.add(i)
        length = 0
        maxLength = 0
        newSet = list(newSet)
        for i in range(0, len(newSet) - 1):
            if (newSet[i] + 1) == newSet[i + 1]:
                length += 1
                maxLength = max(maxLength, length)

        return maxLength + 1
        print(newSet)