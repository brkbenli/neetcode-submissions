class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for i in strs:
            encoded += "#" + str(len(i)) + "~" + i

        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        output = []
        while i < len(s):
            # first check if value is # and if i is not last element
            
            number = ""
            if s[i] == "#" and i != len(s) - 1 and s[i + 1].isdigit():
                i += 1
                while s[i] != "~":
                    number += s[i]
                    print(s[i], i)
                    i += 1
            print(number)
            print(i)
            i += 1
            output.append(s[i : i + int(number)])
            i += int(number)
        return output
