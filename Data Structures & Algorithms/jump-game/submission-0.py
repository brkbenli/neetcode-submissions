class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        currValIndex = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            print(currValIndex, i)
            if currValIndex - i <= nums[i]:
                currValIndex = i

        if currValIndex == 0:
            return True
        return False