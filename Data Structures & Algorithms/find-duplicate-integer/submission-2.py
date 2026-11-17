class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s, f = 0, 1

        while nums[s] != nums[f]:
            s += 1
            f += 2
            if s >= len(nums):
                s = s % len(nums)
            if f >= len(nums):
                f = f % len(nums)
        return nums[s]