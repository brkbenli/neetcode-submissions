class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = set()
        print(nums)
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
                    output.add((nums[i], nums[l], nums[r]))
                    l += 1
                    
        return list(output)