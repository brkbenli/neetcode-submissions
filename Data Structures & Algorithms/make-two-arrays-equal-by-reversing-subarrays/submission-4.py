class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(target)):
            if target[i] not in hashmap1:
                hashmap1[target[i]] = 1
            else:
                hashmap1[target[i]] += 1

            if arr[i] not in hashmap2:
                hashmap2[arr[i]] = 1
            else:
                hashmap2[arr[i]] += 1
        return True if hashmap1 == hashmap2 else False