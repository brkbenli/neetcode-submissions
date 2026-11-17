class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1)

        s1arr = [0] * 26
        for i in range(len(s1)):
            s1arr[ord(s1[i]) - ord("a")] += 1

        s2arr = [0] * 26
        for i in range(len(s1)):
            s2arr[ord(s2[i]) - ord("a")] += 1

        while r < len(s2):
            if s1arr == s2arr:
                return True
            print(l, r)
            print(s2arr)
            s2arr[ord(s2[r]) - ord("a")] += 1
            print(s2arr)
            s2arr[ord(s2[l]) - ord("a")] -= 1
            print(s2arr)
            r += 1
            l += 1

            

        return False