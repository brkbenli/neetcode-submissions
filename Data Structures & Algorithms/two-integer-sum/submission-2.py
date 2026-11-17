class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
        
        
        for i in hashmap:

            if len(nums) == 2:
                return [0, 1]
            elif target - i in hashmap:
                return [hashmap[i], hashmap[(target - i)] ]

        