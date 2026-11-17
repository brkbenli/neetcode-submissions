class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            if nums[slow] == nums[fast] and slow != fast:
                break
            slow += 1
            slow = slow % (len(nums))

            fast += 2
            fast = fast % (len(nums))
        return nums[slow]
