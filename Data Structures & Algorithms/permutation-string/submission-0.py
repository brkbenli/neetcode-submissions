class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        zeros1 = [0] * 26
        zeros2 = [0] * 26

        if len(s1) > len(s2):
            return False
        
        for i in range(len(s1)):
            zeros1[ord(s1[i]) - ord("a")] += 1
        l = 0
        r = 0
        while r < len(s2):
            print(r - l + 1)
            if r - l + 1 <= len(s1):
                zeros2[ord(s2[r]) - ord("a")] += 1
            else:
                zeros2[ord(s2[r]) - ord("a")] += 1
                zeros2[ord(s2[l]) - ord("a")] -= 1
                l += 1
            r += 1
            print(zeros1, "1")
            print(zeros2)
            if zeros1 == zeros2:
                return True
        return False
