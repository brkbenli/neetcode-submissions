class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        myDict = {}
        for i in range(len(nums)):
            if nums[i] not in myDict:
                myDict[nums[i]] = nums[i]
                
            else:
                return True
        return False