class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find a value where index of value - 1 is larger
        l = 0
        r = len(nums) - 1
        while r >= l:
            middle = (l + r) // 2
            print(middle)
            if nums[middle] < nums[middle - 1] or middle == len(nums) - 1 or middle == 0:
                return nums[middle]
            
            elif nums[middle] < nums[middle + 1]:
                l = middle + 1
            else:
                r = middle - 1
        return nums[0]