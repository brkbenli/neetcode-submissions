class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else: hashMap[nums[i]] = 1
        print(hashMap)
        output = []
        while k > 0:
            output.append(max(hashMap))
            hashMap.pop(max(hashMap))
            k -= 1
        return output