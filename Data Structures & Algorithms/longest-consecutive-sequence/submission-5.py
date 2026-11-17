class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        numset = set()
        for i in nums:
            numset.add(i)
        print(numset)

        seqstart = set()
        for i in range(len(nums)):
            if nums[i] - 1 not in numset:
                seqstart.add(nums[i])
        print(seqstart)
        maxseq = 0
        for i in seqstart:
            count = 1
            while i + 1 in numset:
                count += 1
                maxseq = max(maxseq, count)
                i += 1
        return maxseq