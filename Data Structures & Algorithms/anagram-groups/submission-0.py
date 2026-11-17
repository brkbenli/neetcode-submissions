class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # list representing numbers
        hashmap = {}

        # count letters in string
        for i in strs:
            letterNum = [0] * 26
            for j in i:
                letterNum[ord(j) - 97] += 1


            newHash = tuple(letterNum)
            if newHash not in hashmap:
                newHash = tuple(letterNum)
                hashmap[newHash] = [i]
            else:
                newHash = tuple(letterNum)
                hashmap[newHash].append(i)
        array = []
        for i in hashmap:
            array.append(hashmap[i])

        return array
            
                

        
        