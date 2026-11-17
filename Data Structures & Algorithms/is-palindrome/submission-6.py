class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        ss = ""
        for i in s:
            if i.isalnum():
                ss += i
        r = len(ss) - 1
        print("hia")
        while r >= l:
            print("hi")
            print(ss[l], ss[r])
            if ss[l] == ss[r]:

                r -= 1
                l += 1
            else:
                return False


        return True