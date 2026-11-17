class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap: hashMap[nums[i]] += 1
            else: hashMap[nums[i]] = 1
        output = []
        for key, value in hashMap.items():
            output.append([value, key])
        output.sort()

        res = []
        while k > 0:
            res.append(output.pop()[1])
            k -= 1
        return res