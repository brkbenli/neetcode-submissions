class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        subs = []
        nums.sort()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while k > j:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    if [nums[i], nums[j], nums[k]] not in subs:
                        subs.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1
        return subs

                    