class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        reverseStr = newStr[::-1]
        if reverseStr == newStr:
            return True
        else:
            return False