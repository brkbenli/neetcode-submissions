class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = {}
        count = 1
        for i in range(len(nums)):
            if nums[i] not in myHash:
                myHash[nums[i]] = count
            else:
                myHash[nums[i]] += count
        
        sorted_hash = dict(sorted(myHash.items(), key=lambda item: item[1], reverse=True))
        
        newList = []
        for key in sorted_hash:
            if k > len(newList):
                newList.append(key)
            else:
                break


        return newList
            
