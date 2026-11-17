class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        for i in range(len(nums)):
            if target - nums[i] not in myHash:
                myHash[nums[i]] = i
            else:
                newList = [myHash[nums[i] - i], i]
        return newList
                

        