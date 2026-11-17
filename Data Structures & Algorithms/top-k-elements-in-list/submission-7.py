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
        for i in output:
            if i:
                outputarr.append(i)
        print(outputarr)
        final = []
        for i in range(len(outputarr) - 1, len(outputarr) - k - 1, -1):
            for j in range(len(outputarr[i])):
                final.append(outputarr[i][j])
                
    
 
        return final
        


