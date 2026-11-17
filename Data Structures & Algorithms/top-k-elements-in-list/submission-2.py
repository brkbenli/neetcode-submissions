class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap: hashMap[nums[i]] += 1
            else: hashMap[nums[i]] = 1
        output = []
        for _ in range(k):
            maxKey = max(hashMap, key=hashMap.get)
            output.append(maxKey)
            hashMap.pop(maxKey)
            
            
        return output