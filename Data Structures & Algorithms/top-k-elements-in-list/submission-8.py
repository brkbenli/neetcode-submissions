class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        hMap = Counter(nums)

        
        output = []
        for i in range(len(nums)):
            output.append([])

        for key, value in hMap.items():
            output[value - 1].append(key)
            
        outputarr = []
        for i in range(len(output) - 1, -1, -1):
            for j in range(len(output[i])):

                outputarr.append(output[i][j])
                if len(outputarr) == k:
                    return outputarr
                

        


