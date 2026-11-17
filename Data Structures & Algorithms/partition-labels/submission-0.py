class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        
        lastIndex = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in lastIndex:
                lastIndex[s[i]] = i
        print(lastIndex)
        output = []

        i = 0
        while i < len(s):
            print("begins")
            seen = set()
            size = 0
            end = lastIndex[s[i]]
            print(i, s[i], size, "check1")
            while i < end:
                print(i)
                seen.add(s[i])
                size += 1
                print(max(seen))
                for j in seen:
                    end = max(end, lastIndex[j])
                
                print(seen, end, "check2")

                i += 1
            i += 1
            output.append(size + 1)
            
            print(i, "see i")
        return output
            

            
                


