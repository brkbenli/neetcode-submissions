class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        for i in range(len(nums)):
            myHash[nums[i]] = i
        
        
        for i in range(len(nums)):
            if target - nums[i] in myHash:
                return [i, myHash[target - nums[i]],]