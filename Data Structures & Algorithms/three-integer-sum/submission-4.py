class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                # if target > 0
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    break
        return output