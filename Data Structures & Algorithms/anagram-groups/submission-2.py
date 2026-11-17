class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        
        for i in range(len(strs)):
            anagram = [0] * 26
            for j in strs[i]:
                anagram[ord(j) - ord('a')] += 1
            
            if tuple(anagram) in hashmap:
                hashmap[tuple(anagram)] += [strs[i]]
            else:
                hashmap[tuple(anagram)] = [strs[i]]
        sublist = []
        for i in hashmap.values():
            sublist.append(i)
        return sublist