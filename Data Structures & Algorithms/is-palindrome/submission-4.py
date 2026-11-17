class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.lower()
        pali = ""
        for i in s:
            if i.isalpha():
                pali += i.lower()
        
        l = 0
        r = len(pali) - 1
        while r > l:
            if pali[l] == pali[r]:
                r -= 1
                l += 1
            else:
                return False
        return True