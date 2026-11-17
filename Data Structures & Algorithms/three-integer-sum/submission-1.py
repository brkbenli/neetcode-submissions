class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                if nums[i] + nums[l] + nums[r] == 0:
                    output.append([nums[i],nums[l], nums[r]])
                    break
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return output
            