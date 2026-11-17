class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif target > mid:
                left = mid + 1
            elif target < mid:
                right = mid - 1
            else:
                break
        return -1
            