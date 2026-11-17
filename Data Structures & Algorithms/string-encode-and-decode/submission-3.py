class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for i in range(len(strs)):
            newStr += strs[i]
            newStr += "|"
        print(newStr)
        return newStr
    def decode(self, s: str) -> List[str]:
        
        emp = ""
        output = []
        for i in range(len(s)):
            if s[i] == "|":
                output.append(emp)
                emp = ""
                continue
            emp += s[i]
        return output
