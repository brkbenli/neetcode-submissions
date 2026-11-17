class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while r >= l:
            mid = (l + r) // 2
            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        point = l - 1
        if nums[-1] >= target and nums[point] <= target:
            l = point
            r = len(nums) - 1
        else:
            l = 0
            r = point - 1
        while r >= l:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
        

