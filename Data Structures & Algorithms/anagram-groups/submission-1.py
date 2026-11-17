class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for i in range(len(strs)):
            k = [0] * 26
            for j in range(len(strs[i])):
                k[ord(strs[i][j]) - ord("a")] += 1
            print(k)
            if tuple(k) in hashMap:
                hashMap[tuple(k)] += [strs[i]]
            else:
                hashMap[tuple(k)] = [strs[i]]
        output = []
        for val in hashMap.values():
            output.append(val)
        return output