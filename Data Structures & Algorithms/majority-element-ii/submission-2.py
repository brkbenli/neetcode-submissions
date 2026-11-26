class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counts = Counter(nums)

        res = []
        for key, val in counts.items():
            if len(nums) // 3 < val:
                res.append(key)
        return res