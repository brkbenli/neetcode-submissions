class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for i in strs:
            newStr += str(len(i)) + "#" + i
        return newStr
        
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            print(res)
            length = int(s[i:j])
            res.append(s[j + 1: j + length + 1])
            i = length + j + 1
        return res
                