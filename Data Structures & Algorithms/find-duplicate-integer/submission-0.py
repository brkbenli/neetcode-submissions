class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashlist = []
        print(nums)
        for i in range(len(nums)):
            if nums[i] not in hashlist:
                hashlist.append(nums[i])
            else:
                return nums[i]
        