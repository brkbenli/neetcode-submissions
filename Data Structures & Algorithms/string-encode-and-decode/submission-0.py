class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for i in range(len(strs)):
            newStr += strs[i]
            newStr += "|"
        print(newStr)
        return newStr
    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        output = []
        while r < len(s):
            if s[r] == "|":
                output.append(s[l:r])
                r += 1
                l = r
            r += 1
        return output
