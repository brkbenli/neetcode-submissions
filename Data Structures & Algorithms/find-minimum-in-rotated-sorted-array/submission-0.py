class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while r >= l:
            middle = (l + r) // 2
            print(nums[middle])
            print(l, r)
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            elif nums[middle] < nums[middle - 1]:
                return nums[middle]
            elif nums[r] < nums[l]:
                l = middle + 1
            else:
                r = middle - 1
        return -1