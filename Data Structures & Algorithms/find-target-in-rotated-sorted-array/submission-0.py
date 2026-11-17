class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while r > l:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        print(l, nums[l])
        k = (l + target) % len(nums) - 1
        print(k)
        if nums[k] == target:
            return k
        else:
            return -1