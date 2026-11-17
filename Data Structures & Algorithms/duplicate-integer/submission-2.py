class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         myHash = {}
         for i in range(len(nums)):
            if nums[i] not in myHash:
                myHash[nums[i]] = i
            else:
                return True
            
         return False